![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Spark](https://img.shields.io/badge/Apache_Spark-FFFFFF?style=for-the-badge&logo=apachespark&logoColor=#E35A16)
![PBI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=white)
![GPT](https://img.shields.io/badge/ChatGPT%204o-000000?style=for-the-badge&logo=openai&logoColor=white&label=)

# Introduction

Hi everyone! Shamslux here! This is my personal lab for reviewing some concepts and evolving others. I am putting some personal effort in this lab in order to improve myself as a Analytics Engineer/Data Engineer and 
also for letting a free content for anyone following my repository wishing some ideas for further practice of even some nice content for learning together. 

In order to make it a fun study (and remembering my days playing Aerobiz Supersonic on the Super Nintendo), I am creating some scenarios and cases simulating some business and requests. ChatGPT is helping me creating
some characters, stories, requests, study cases, character image, etc.

I really hope you may find fun together with me doing it. It is not easy, as it is never easy to keep the pace studying, but it is very necessary for us in this field. I am very distant, veeerryyy distant from the position
I would like, and I want to keep improving myself as a professional in the Data field. 

Well, enjoy it!

# Our ficticious company


## 🏢 **NovaTrade Inc.**

**Empowering Business Through Intelligent Distribution**

NovaTrade Inc. is a leading B2B distributor specializing in high-performance **Widgets**, **Gadgets**, **Accessories**, and essential **Tech Components**. Serving thousands of clients across North America, NovaTrade provides businesses with streamlined access to over 100 top-tier products in technology and equipment categories.

Founded on the principles of operational excellence and data-driven strategy, NovaTrade bridges the gap between manufacturers and retailers through an integrated supply chain model powered by real-time analytics, regional market insights, and customer-centric service.

Our clients range from startups to enterprise-level retailers across five strategic regions: **North**, **South**, **East**, **West**, and **Central**. With a dynamic catalog and a focus on reliability, NovaTrade helps partners optimize procurement, forecast demand, and grow with confidence.

---

### 🔍 **What We Do**

* B2B product distribution across multiple categories
* Regional inventory management & fulfillment
* Custom logistics & vendor integration
* Sales performance analytics & insights
* Strategic product recommendations based on demand intelligence

---

### 📊 **Our Impact (2024–2025 Highlights)**

* 💼 Over **100,000 transactions** processed
* 🛒 **2,500+ active business clients**
* 📦 Distribution of **100 unique SKUs** across 6 major product categories
* 🌎 Nationwide presence across 5 core sales regions
* 📈 Real-time sales data used to inform executive decision-making and client-facing dashboards

---

### 🚀 **Mission**

> To power smarter commerce by connecting businesses with the products they need—fast, reliably, and intelligently.

---

# Requests

Here we start documenting what NovaTrade Inc. employees are going to request from our Data team!

## Sales Analytical Information


## 👤 Requester (does this word exist? hahaha)

- **Name:** Sarah McConnell  
- **Position:** Head of Sales Operations  
- **Department:** Business Intelligence & Strategy  
- **Company:** NovaTrade Inc.


Hi team,

This is Sarah McConnell, Head of Sales Operations here at NovaTrade Inc.

I’m reaching out to request your support in ingesting a new Excel spreadsheet named `novatrade_sales_data_xlarge.xlsx` into our analytical data lake. I've uploaded the file to the shared `/data` folder in the Airflow environment.

This dataset contains:

- **100,000 sales records** from January 2024 through December 2025.
- **2,500 unique customers**, including region segmentation across 5 key territories (North, South, East, West, Central).
- **100 distinct products**, categorized under Widgets, Gadgets, Accessories, Tools, Supplies, and Components.

We are preparing a comprehensive multi-year performance analysis for the executive leadership team, and I need the following from the data engineering team:

---

### 📊 Business Requirements

**1. Load the Excel data into our analytical PostgreSQL database (OLAP layer).**
  - Suggested schema:
    - `dim_customer`
    - `dim_product`
    - `fact_sales`

**2. Ensure data integrity:**
  - Deduplicate and clean as needed.
  - Enforce foreign keys using `Customer_ID` and `Product_ID` as natural keys.

**3. Prepare the following monthly aggregated KPIs:**
  - ✅ Total revenue by region
  - ✅ Total quantity sold per product category
  - ✅ Average transaction amount per customer
  - ✅ Top 10 products by revenue and by volume
  - ✅ Daily sales patterns (weekdays vs weekends, seasonality)

**4. Support business questions such as:**
  - What are our top performing regions and categories by revenue in 2024 and 2025?
  - Who are our top 50 revenue-generating customers?
  - Which product lines have the strongest YoY growth?
  - Are there noticeable trends or drops in specific months or quarters?
---

This data will be visualized in our Power BI dashboards and presented during the upcoming strategic planning session. Please structure the pipeline in a way that can be reused and scheduled via Airflow.

Let me know if you need anything else.

Thanks in advance,  
Sarah

