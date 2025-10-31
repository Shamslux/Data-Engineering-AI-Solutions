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


### 👤 Requester (does this word exist? hahaha)

- **Name:** Sarah McConnell  
- **Position:** Head of Sales Operations  
- **Department:** Business Intelligence & Strategy  
- **Company:** NovaTrade Inc.

---

<img src="https://github.com/user-attachments/assets/3eadb201-c3aa-4149-8529-d20b8e7a1828" alt="Sarah Pixel Portrait" width="200" height="250">

**🎤 Sarah McConnell**  
*Head of Sales Operations – NovaTrade Inc.*

---

> 📁 **Data Upload Notice**  
> I’ve uploaded the file `novatrade_sales_data_xlarge.xlsx` to the `/data` folder in Airflow.
>
> 🧠 **Objectives**  
> • Load data into PostgreSQL (OLAP)  
> • Use tables: `dim_customer`, `dim_product`, `fact_sales`  
> • Enforce FK constraints using `Customer_ID`, `Product_ID`
>
> 📊 **KPIs**  
> - Total revenue by region  
> - Quantity sold per category  
> - Average transaction per customer  
> - Top 10 products (volume & revenue)  
> - Weekday vs weekend patterns  
>
> ❓ **Questions to Answer**  
> - What are our top performing regions and categories in 2024–2025?  
> - Who are our top 50 customers?  
> - Any YoY growth in product lines?  
> - Monthly/seasonal dips?
>
> ⚙️ Please automate this via Airflow.  
> Let me know if you need anything else!

—  
*Sarah*




