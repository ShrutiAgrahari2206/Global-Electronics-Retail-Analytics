# Global Electronics Retail Analytics

An end-to-end data analytics project analyzing global electronics retail sales and business performance using Excel, Power BI, DAX, SQL, and Python.

## 📌 Project Overview

This project analyzes a global electronics retail dataset to understand:

* Revenue and profitability
* Product and category performance
* Brand performance
* Customer distribution
* Country and state-level performance
* Store size and revenue relationship
* Top-performing products and customers

The project covers the complete analytics workflow from data cleaning and validation to business insights, exploratory analysis, and dashboard development.

## 🛠️ Tools & Technologies

* **Microsoft Excel** — Data cleaning and validation
* **Power BI** — Data modeling and interactive dashboards
* **DAX** — KPI and business metric calculations
* **SQL** — Business analysis queries
* **Python** — Exploratory Data Analysis (EDA)
* **Pandas** — Data manipulation
* **Matplotlib** — Data visualization

## 📊 Key Performance Indicators

| KPI                      |   Value |
| ------------------------ | ------: |
| Total Revenue            | $55.76M |
| Total Profit             | $32.66M |
| Total Orders             |     26K |
| Total Units Sold         |    198K |
| Average Order Value      |  $2.12K |
| Profit Margin            |  58.58% |
| Total Customers          |     12K |
| Revenue per Square Meter | $602.47 |

## 📈 Power BI Dashboard

The Power BI dashboard contains three analytical pages:

### 1. Executive Overview

Provides a high-level view of:

* Revenue
* Profit
* Orders
* Units Sold
* Average Order Value
* Profit Margin
* Revenue trend
* Revenue by country
* Revenue by category

### 2. Product & Profitability Analysis

Analyzes:

* Revenue by category
* Revenue by brand
* Profit by category
* Profit by subcategory
* Top 10 products by revenue
* Revenue vs Profit relationship
* Profit margin by category

### 3. Customer & Store Analysis

Analyzes:

* Total customers
* Customer distribution by country
* Top 10 customers by revenue
* Revenue by state
* Store size vs revenue
* Revenue per square meter

## 💡 Key Business Insights

* Computers generate the highest revenue and profit among product categories.
* Desktops are the highest-profit product subcategory.
* Adventure Works generates the highest revenue among brands.
* The United States generates the highest revenue among countries.
* California is the highest-revenue state.
* Matthew Flemming is the highest-revenue customer among the top 10 customers.
* Larger stores generally tend to generate higher revenue, although store size alone does not fully explain revenue performance.
* The top revenue-generating products are dominated by desktop PC models.

## 🧹 Data Cleaning & Preparation

Data was cleaned and validated using Excel before analysis.

Key activities included:

* Removing unnecessary leading and trailing spaces
* Checking duplicate records
* Validating primary and transaction keys
* Handling blank values
* Converting date fields to proper date formats
* Validating numeric fields
* Validating product costs and prices
* Checking positive sales quantities
* Validating currency codes
* Creating date-currency keys for exchange-rate analysis

Meaningful blanks, such as undelivered order dates and the online store's missing physical store area, were retained.

## 🧮 Power BI Data Model

The Power BI model connects:

* Customers → Sales
* Products → Sales
* Stores → Sales
* Exchange Rates → Sales
* Date Table → Sales

DAX measures were created for:

* Total Revenue
* Total Cost
* Total Profit
* Profit Margin %
* Total Units Sold
* Total Orders
* Average Order Value
* Total Customers
* Revenue per Square Meter

## 🐍 Python EDA

Python was used for exploratory data analysis and independent analysis of key business metrics.

The Python analysis produced:

* KPI summary
* Monthly revenue trend
* Revenue by category
* Revenue by country
* Revenue by brand
* Profit by category
* Profit by subcategory
* Store size vs revenue
* Top 10 customers by revenue
* Top 10 products by revenue

Python analysis outputs are included in the `Python/Python_Outputs` folder.

## 🗄️ SQL Analysis

SQL queries were created to analyze:

* Revenue
* Cost
* Profit
* Profit margin
* Category performance
* Subcategory performance
* Brand performance
* Country and state performance
* Top products
* Top customers
* Orders and units sold
* Average order value
* Customer distribution
* Monthly revenue trends

## 📁 Project Structure

```text
Global-Electronics-Retail-Analytics
│
├── Dashboard Screenshots
│   ├── Page 1 - Executive Overview.png
│   ├── Page 2 - Product & Profitability Analysis.png
│   └── Page 3 - Customer & Store Analysis.png
│
├── Documentation
│   └── Business Insight.txt
│
├── Power BI
│   └── Global_Electronics_Retail_Analytics.pbix
│
├── Python
│   ├── Global_Electronics_Retail_Analytics.py
│   └── Python_Outputs
│
├── SQL
│   └── Global_Electronics_Retail_Analytics_SQL.sql
│
└── README.md
```

## 📷 Dashboard Screenshots

### Executive Overview

![Executive Overview](Dashboard%20Screenshots/Page%201%20-%20Executive%20Overview.png)

### Product & Profitability Analysis

![Product & Profitability Analysis](Dashboard%20Screenshots/Page%202%20-%20Product%20%26%20Profitability%20Analysis.png)

### Customer & Store Analysis

![Customer & Store Analysis](Dashboard%20Screenshots/Page%203%20-%20Customer%20%26%20Store%20Analysis.png)

## 🎯 Project Outcome

This project demonstrates an end-to-end business analytics workflow involving:

* Data cleaning and validation
* Data modeling
* KPI development
* Exploratory data analysis
* SQL-based business analysis
* Interactive dashboard development
* Business insight generation

The analysis provides a structured view of product, customer, geographic, profitability, and store performance while identifying key revenue and profitability drivers.
