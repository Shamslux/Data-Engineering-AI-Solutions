import os
import re
import sys
import argparse
import random
import string
import pandas as pd
from sqlalchemy import create_engine, text
from dateutil import parser

# -------------------------
# CLI / ENV CONFIG
# -------------------------
def parse_args():
    ap = argparse.ArgumentParser(description="Ingest books.csv -> Postgres with cleaning.")
    ap.add_argument("--csv", dest="csv_path", default=None, help="Path to CSV (e.g.: C:\\...\\data\\books.csv)")
    ap.add_argument("--sep", dest="sep", default="auto", help="Delimiter (',' | '\\t' | 'auto'; default: auto)")
    ap.add_argument("--encoding", dest="encoding", default="utf-8-sig", help="Encoding (default: utf-8-sig)")
    return ap.parse_args()

args = parse_args()

DB_NAME = os.getenv("DB_NAME", "bookstore")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

CSV_PATH = args.csv_path or os.getenv("CSV_PATH")
if not CSV_PATH:
    # fallback: ../data/books.csv (project root)
    here = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(here, os.pardir))
    CSV_PATH = os.path.join(project_root, "data", "books.csv")

# -------------------------
# UTILITIES
# -------------------------
def detect_delimiter(sample_path: str, encoding: str = "utf-8-sig") -> str:
    try:
        with open(sample_path, encoding=encoding, errors="ignore") as f:
            s = f.read(4000)
        return "\t" if s.count("\t") > s.count(",") else ","
    except Exception:
        # fallback
        return ","

def normalize_isbn(s: str | None) -> str | None:
    if not s:
        return None
    s = re.sub(r"[^0-9Xx]", "", s)  # keep digits and X
    return s or None

def parse_date_safe(s: str | None):
    if not s or not str(s).strip():
        return None
    try:
        # accepts "9/1/2004", "09/01/2004", etc.
        dt = parser.parse(str(s), dayfirst=False, yearfirst=False, fuzzy=True)
        return dt.date()
    except Exception:
        return None

def coerce_int(x):
    try:
        if pd.isna(x) or str(x).strip() == "":
            return None
        return int(float(str(x)))
    except Exception:
        return None

def coerce_float(x):
    try:
        if pd.isna(x) or str(x).strip() == "":
            return None
        return float(str(x))
    except Exception:
        return None

def try_read_csv(path: str, sep: str, encoding: str) -> pd.DataFrame:
    """
    Resilient reading:
    1) engine=python, chosen sep, on_bad_lines=skip
    2) sep=None (infer), engine=python
    3) latin1 as encoding fallback
    """
    # 1) main attempt
    try:
        return pd.read_csv(
            path,
            sep=(None if sep == "auto" else sep),
            dtype=str,
            keep_default_na=False,
            engine="python",
            quotechar='"',
            escapechar="\\",
            on_bad_lines="skip",
            encoding=encoding,
        )
    except Exception as e1:
        print(f"[ingest] fallback 1 failed: {e1}")

    # 2) explicitly infer separator
    try:
        return pd.read_csv(
            path,
            sep=None,
            dtype=str,
            keep_default_na=False,
            engine="python",
            quotechar='"',
            escapechar="\\",
            on_bad_lines="skip",
            encoding=encoding,
        )
    except Exception as e2:
        print(f"[ingest] fallback 2 failed: {e2}")

    # 3) latin1 encoding
    try:
        return pd.read_csv(
            path,
            sep=(None if sep == "auto" else sep),
            dtype=str,
            keep_default_na=False,
            engine="python",
            quotechar='"',
            escapechar="\\",
            on_bad_lines="skip",
            encoding="latin1",
        )
    except Exception as e3:
        print(f"[ingest] fallback 3 failed: {e3}")
        raise

def random_suffix(n=6):
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=n))

# -------------------------
# PIPELINE
# -------------------------
def main():
    if not os.path.exists(CSV_PATH):
        print(f"[ingest] CSV not found at {CSV_PATH}", file=sys.stderr)
        sys.exit(1)

    sep = args.sep
    if sep == "auto":
        sep = detect_delimiter(CSV_PATH, args.encoding)

    print(f"[ingest] Reading CSV '{CSV_PATH}' with delimiter '{sep}' (encoding={args.encoding})...")
    df = try_read_csv(CSV_PATH, sep, args.encoding)

    total_lines_csv = len(df)
    print(f"[ingest] Lines read (after skipping bad ones): {total_lines_csv}")

    # Standardize columns
    cols_map = {
        "bookID": "bookID", "bookId": "bookID", "id": "bookID",
        "title": "title",
        "authors": "authors",
        "average_rating": "average_rating",
        "isbn": "isbn",
        "isbn13": "isbn13",
        "language_code": "language_code",
        "num_pages": "num_pages",
        "ratings_count": "ratings_count",
        "text_reviews_count": "text_reviews_count",
        "publication_date": "publication_date",
        "publisher": "publisher",
    }
    df = df.rename(columns={c: cols_map.get(c, c) for c in df.columns})
    for c in cols_map.values():
        if c not in df.columns:
            df[c] = ""

    # Cleaning & types
    df["bookID"] = df["bookID"].apply(coerce_int)
    df["title"] = df["title"].astype(str).str.strip().str.slice(0, 400)
    df["authors_raw"] = df["authors"].astype(str).fillna("").str.strip().str.slice(0, 400)

    df["average_rating"] = df["average_rating"].apply(coerce_float)
    df["isbn"] = df["isbn"].apply(normalize_isbn)
    df["isbn13"] = df["isbn13"].apply(normalize_isbn)

    # Fix possible swaps isbn <-> isbn13
    def fix_isbn_row(row):
        i10, i13 = row.get("isbn"), row.get("isbn13")
        if i10 and len(i10) == 13 and (not i13 or len(i13) != 13):
            row["isbn13"], row["isbn"] = i10, None
        if i13 and len(i13) == 10 and (not i10 or len(i10) != 10):
            row["isbn"], row["isbn13"] = i13, None
        return row

    df = df.apply(fix_isbn_row, axis=1)

    df["language_code"] = df["language_code"].astype(str).fillna("").str.strip().str.slice(0, 10)
    df["num_pages"] = df["num_pages"].apply(coerce_int)
    df["ratings_count"] = df["ratings_count"].apply(coerce_int)
    df["text_reviews_count"] = df["text_reviews_count"].apply(coerce_int)
    df["publication_date"] = df["publication_date"].apply(parse_date_safe)
    df["publisher"] = df["publisher"].astype(str).fillna("").str.strip().str.slice(0, 200)

    # Filter invalid records
    before = len(df)
    df = df[~df["bookID"].isna() & df["title"].astype(bool)]
    after = len(df)
    print(f"[ingest] Valid records: {after} (discarded: {before - after})")

    out = df[[
        "bookID","title","authors_raw","average_rating","isbn","isbn13","language_code",
        "num_pages","ratings_count","text_reviews_count","publication_date","publisher"
    ]].rename(columns={"bookID": "book_id"})

    # DB connection
    engine = create_engine(URI, future=True)

    # DDL
    ddl = """
    CREATE TABLE IF NOT EXISTS books (
      book_id            INTEGER PRIMARY KEY,
      title              VARCHAR(400) NOT NULL,
      authors_raw        VARCHAR(400),
      average_rating     NUMERIC(4,2),
      isbn               VARCHAR(20),
      isbn13             VARCHAR(20),
      language_code      VARCHAR(10),
      num_pages          INTEGER,
      ratings_count      INTEGER,
      text_reviews_count INTEGER,
      publication_date   DATE,
      publisher          VARCHAR(200),
      created_at         TIMESTAMP DEFAULT now()
    );
    """
    with engine.begin() as conn:
        conn.execute(text(ddl))

    # Temporary staging (unique name to avoid conflict in simultaneous runs)
    staging = f"_staging_books_{random_suffix()}"
    with engine.begin() as conn:
        conn.execute(text(f"CREATE TEMP TABLE {staging} (LIKE books INCLUDING ALL);"))

    # Load into staging
    out.to_sql(staging, engine, if_exists="append", index=False)
    print(f"[ingest] Rows loaded into staging: {len(out)}")

    # UPSERT
    upsert = f"""
    INSERT INTO books (book_id,title,authors_raw,average_rating,isbn,isbn13,language_code,
                       num_pages,ratings_count,text_reviews_count,publication_date,publisher)
    SELECT book_id,title,authors_raw,average_rating,isbn,isbn13,language_code,
           num_pages,ratings_count,text_reviews_count,publication_date,publisher
    FROM {staging}
    ON CONFLICT (book_id) DO UPDATE SET
      title = EXCLUDED.title,
      authors_raw = EXCLUDED.authors_raw,
      average_rating = EXCLUDED.average_rating,
      isbn = EXCLUDED.isbn,
      isbn13 = EXCLUDED.isbn13,
      language_code = EXCLUDED.language_code,
      num_pages = EXCLUDED.num_pages,
      ratings_count = EXCLUDED.ratings_count,
      text_reviews_count = EXCLUDED.text_reviews_count,
      publication_date = EXCLUDED.publication_date,
      publisher = EXCLUDED.publisher;
    """
    with engine.begin() as conn:
        conn.execute(text(upsert))
        # res.rowcount may be -1 depending on driver; just inform success
    print("[ingest] UPSERT completed.")

    print("[ingest] Completed successfully.")

if __name__ == "__main__":
    main()
