import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# GLOBAL ELECTRONICS RETAIL ANALYTICS - PYTHON EDA
# CLEAN FINAL VERSION
# ============================================================

# ------------------------------------------------------------
# 1. PROJECT PATHS
# ------------------------------------------------------------

PROJECT_PATH = Path(
    r"C:\Users\Lenovo\Desktop\E-Commerce Business Analytics"
)

CLEAN_DATA_PATH = PROJECT_PATH / "Clean data"
PYTHON_PATH = PROJECT_PATH / "Python"
OUTPUT_PATH = PYTHON_PATH / "Python_Outputs"

OUTPUT_PATH.mkdir(exist_ok=True)

# ------------------------------------------------------------
# 2. LOAD DATA
# ------------------------------------------------------------

customers = pd.read_csv(
    CLEAN_DATA_PATH / "Customer_Cleaned.csv",
    encoding="cp1252"
)

products = pd.read_csv(
    CLEAN_DATA_PATH / "Products_Cleaned.csv"
)

sales = pd.read_csv(
    CLEAN_DATA_PATH / "Sales_Cleaned.csv"
)

stores = pd.read_csv(
    CLEAN_DATA_PATH / "Stores_Cleaned.csv"
)

exchange_rates = pd.read_csv(
    CLEAN_DATA_PATH / "Exchange_Rates_Cleaned.csv"
)

print("=" * 70)
print("GLOBAL ELECTRONICS RETAIL ANALYTICS - PYTHON EDA")
print("=" * 70)

# ------------------------------------------------------------
# 3. DATASET OVERVIEW
# ------------------------------------------------------------

print("\nDATASET SHAPES")
print("-" * 70)

print("Customers      :", customers.shape)
print("Products       :", products.shape)
print("Sales          :", sales.shape)
print("Stores         :", stores.shape)
print("Exchange Rates :", exchange_rates.shape)

# ------------------------------------------------------------
# 4. PREPARE DATA TYPES
# ------------------------------------------------------------

sales["Order Date"] = pd.to_datetime(
    sales["Order Date"],
    errors="coerce"
)

sales["Quantity"] = pd.to_numeric(
    sales["Quantity"],
    errors="coerce"
)

# Convert Unit Price and Unit Cost to numeric
# Remove comma separators before conversion

products["UnitPriceUSD"] = (
    products["UnitPriceUSD"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.strip()
)

products["UnitPriceUSD"] = pd.to_numeric(
    products["UnitPriceUSD"],
    errors="coerce"
)

products["UnitCostUSD"] = (
    products["UnitCostUSD"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.strip()
)

products["UnitCostUSD"] = pd.to_numeric(
    products["UnitCostUSD"],
    errors="coerce"
)

# ------------------------------------------------------------
# 5. VALIDATE PRODUCT DATA
# ------------------------------------------------------------

print("\nPRODUCT DATA VALIDATION")
print("-" * 70)

print(
    "Duplicate ProductKey:",
    products["ProductKey"].duplicated().sum()
)

print(
    "Missing UnitPriceUSD:",
    products["UnitPriceUSD"].isna().sum()
)

print(
    "Missing UnitCostUSD:",
    products["UnitCostUSD"].isna().sum()
)

# ------------------------------------------------------------
# 6. MERGE SALES + PRODUCTS
# ------------------------------------------------------------

analysis = sales.merge(
    products[
        [
            "ProductKey",
            "Product Name",
            "Brand",
            "Color",
            "UnitCostUSD",
            "UnitPriceUSD",
            "SubcategoryKey",
            "Subcategory",
            "CategoryKey",
            "Category"
        ]
    ],
    on="ProductKey",
    how="left",
    validate="many_to_one"
)

# ------------------------------------------------------------
# 7. CHECK PRODUCT MATCHING
# ------------------------------------------------------------

print("\nPRODUCT MATCHING VALIDATION")
print("-" * 70)

print(
    "Sales rows:",
    len(sales)
)

print(
    "Rows after Sales + Products merge:",
    len(analysis)
)

print(
    "Missing Product Name after merge:",
    analysis["Product Name"].isna().sum()
)

print(
    "Missing UnitPriceUSD after merge:",
    analysis["UnitPriceUSD"].isna().sum()
)

print(
    "Missing UnitCostUSD after merge:",
    analysis["UnitCostUSD"].isna().sum()
)

# ------------------------------------------------------------
# 8. CALCULATE REVENUE
# ------------------------------------------------------------

analysis["Revenue"] = (
    analysis["Quantity"] *
    analysis["UnitPriceUSD"]
)

# ------------------------------------------------------------
# 9. CALCULATE COST
# ------------------------------------------------------------

analysis["Cost"] = (
    analysis["Quantity"] *
    analysis["UnitCostUSD"]
)

# ------------------------------------------------------------
# 10. CALCULATE PROFIT
# ------------------------------------------------------------

analysis["Profit"] = (
    analysis["Revenue"] -
    analysis["Cost"]
)

# ------------------------------------------------------------
# 11. KPI CALCULATIONS
# ------------------------------------------------------------

total_revenue = analysis["Revenue"].sum()

total_cost = analysis["Cost"].sum()

total_profit = analysis["Profit"].sum()

total_units = analysis["Quantity"].sum()

total_orders = sales["Order Number"].nunique()

total_customers = sales["CustomerKey"].nunique()

average_order_value = (
    total_revenue /
    total_orders
)

profit_margin = (
    total_profit /
    total_revenue
) * 100

# ------------------------------------------------------------
# 12. REVENUE PER SQUARE METER
# ------------------------------------------------------------

total_store_area = stores["Square Meters"].sum()

revenue_per_square_meter = (
    total_revenue /
    total_store_area
)

# ------------------------------------------------------------
# 13. PRINT KPIs
# ------------------------------------------------------------

print("\nKEY PERFORMANCE INDICATORS")
print("-" * 70)

print(
    f"Total Revenue       : ${total_revenue:,.2f}"
)

print(
    f"Total Cost          : ${total_cost:,.2f}"
)

print(
    f"Total Profit        : ${total_profit:,.2f}"
)

print(
    f"Total Units Sold    : {total_units:,.0f}"
)

print(
    f"Total Orders        : {total_orders:,}"
)

print(
    f"Total Customers     : {total_customers:,}"
)

print(
    f"Average Order Value : ${average_order_value:,.2f}"
)

print(
    f"Profit Margin       : {profit_margin:.2f}%"
)

print(
    f"Revenue per Sq Meter: ${revenue_per_square_meter:,.2f}"
)

# ------------------------------------------------------------
# 14. KPI CALCULATION VALIDATION
# ------------------------------------------------------------

print("\nKPI CALCULATION VALIDATION")
print("-" * 70)

print(
    "Revenue - Cost:",
    f"${total_revenue - total_cost:,.2f}"
)

print(
    "Calculated Profit:",
    f"${total_profit:,.2f}"
)

print(
    "Profit Difference:",
    f"${total_profit - (total_revenue - total_cost):,.2f}"
)

# ------------------------------------------------------------
# 15. REVENUE BY CATEGORY
# ------------------------------------------------------------

revenue_category = (
    analysis
    .groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

revenue_category.to_csv(
    OUTPUT_PATH / "Revenue_by_Category.csv"
)

# ------------------------------------------------------------
# 16. PROFIT BY CATEGORY
# ------------------------------------------------------------

profit_category = (
    analysis
    .groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

profit_category.to_csv(
    OUTPUT_PATH / "Profit_by_Category.csv"
)

# ------------------------------------------------------------
# 17. REVENUE BY BRAND
# ------------------------------------------------------------

revenue_brand = (
    analysis
    .groupby("Brand")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

revenue_brand.to_csv(
    OUTPUT_PATH / "Revenue_by_Brand.csv"
)

# ------------------------------------------------------------
# 18. PROFIT BY SUBCATEGORY
# ------------------------------------------------------------

profit_subcategory = (
    analysis
    .groupby("Subcategory")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

profit_subcategory.to_csv(
    OUTPUT_PATH / "Profit_by_Subcategory.csv"
)

# ------------------------------------------------------------
# 19. TOP 10 PRODUCTS BY REVENUE
# ------------------------------------------------------------

top_products = (
    analysis
    .groupby("Product Name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products.to_csv(
    OUTPUT_PATH / "Top_10_Products_by_Revenue.csv"
)

# ------------------------------------------------------------
# 20. SALES + CUSTOMERS
# ------------------------------------------------------------

customer_analysis = analysis.merge(
    customers[
        [
            "CustomerKey",
            "Name",
            "City",
            "State",
            "Country",
            "Continent"
        ]
    ],
    on="CustomerKey",
    how="left",
    validate="many_to_one"
)

# ------------------------------------------------------------
# 21. REVENUE BY COUNTRY
# ------------------------------------------------------------

revenue_country = (
    customer_analysis
    .groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

revenue_country.to_csv(
    OUTPUT_PATH / "Revenue_by_Country.csv"
)

# ------------------------------------------------------------
# 22. TOP 10 CUSTOMERS BY REVENUE
# ------------------------------------------------------------

top_customers = (
    customer_analysis
    .groupby(
        ["CustomerKey", "Name"]
    )["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_customers.to_csv(
    OUTPUT_PATH / "Top_10_Customers_by_Revenue.csv"
)

# ------------------------------------------------------------
# 23. MONTHLY REVENUE TREND
# ------------------------------------------------------------

monthly_revenue = (
    analysis
    .groupby(
        analysis["Order Date"].dt.to_period("M")
    )["Revenue"]
    .sum()
)

monthly_revenue.index = (
    monthly_revenue.index.astype(str)
)

monthly_revenue.to_csv(
    OUTPUT_PATH / "Monthly_Revenue_Trend.csv"
)

# ------------------------------------------------------------
# 24. SALES + STORES
# ------------------------------------------------------------

store_analysis = analysis.merge(
    stores[
        [
            "StoreKey",
            "Country",
            "State",
            "Square Meters",
            "Open Date"
        ]
    ],
    on="StoreKey",
    how="left",
    validate="many_to_one"
)

# ------------------------------------------------------------
# 25. STORE SIZE VS REVENUE
# ------------------------------------------------------------

store_revenue = (
    store_analysis
    .groupby("StoreKey")["Revenue"]
    .sum()
)

store_size = (
    stores
    .set_index("StoreKey")["Square Meters"]
)

store_size_revenue = pd.DataFrame({
    "Store Size": store_size,
    "Revenue": store_revenue
}).dropna()

store_size_revenue.to_csv(
    OUTPUT_PATH / "Store_Size_vs_Revenue.csv"
)

# ------------------------------------------------------------
# 26. KPI SUMMARY
# ------------------------------------------------------------

kpi_summary = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Cost",
        "Total Profit",
        "Total Units Sold",
        "Total Orders",
        "Total Customers",
        "Average Order Value",
        "Profit Margin",
        "Revenue per Square Meter"
    ],
    "Value": [
        total_revenue,
        total_cost,
        total_profit,
        total_units,
        total_orders,
        total_customers,
        average_order_value,
        profit_margin,
        revenue_per_square_meter
    ]
})

kpi_summary.to_csv(
    OUTPUT_PATH / "KPI_Summary.csv",
    index=False
)

# ------------------------------------------------------------
# 27. CHART - REVENUE BY CATEGORY
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

revenue_category.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    OUTPUT_PATH / "Revenue_by_Category.png",
    dpi=300
)

plt.close()

# ------------------------------------------------------------
# 28. CHART - PROFIT BY CATEGORY
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

profit_category.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    OUTPUT_PATH / "Profit_by_Category.png",
    dpi=300
)

plt.close()

# ------------------------------------------------------------
# 29. CHART - TOP 10 BRANDS
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

revenue_brand.head(10).sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Brands by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Brand")
plt.tight_layout()

plt.savefig(
    OUTPUT_PATH / "Top_10_Brands_by_Revenue.png",
    dpi=300
)

plt.close()

# ------------------------------------------------------------
# 30. CHART - TOP 10 PRODUCTS
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

top_products.sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig(
    OUTPUT_PATH / "Top_10_Products_by_Revenue.png",
    dpi=300
)

plt.close()

# ------------------------------------------------------------
# 31. CHART - MONTHLY REVENUE
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

monthly_revenue.plot(kind="line")

plt.title("Monthly Revenue Trend")
plt.xlabel("Year-Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_PATH / "Monthly_Revenue_Trend.png",
    dpi=300
)

plt.close()

# ------------------------------------------------------------
# 32. CHART - REVENUE BY COUNTRY
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

revenue_country.sort_values().plot(
    kind="barh"
)

plt.title("Revenue by Country")
plt.xlabel("Revenue")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig(
    OUTPUT_PATH / "Revenue_by_Country.png",
    dpi=300
)

plt.close()

# ------------------------------------------------------------
# 33. CHART - STORE SIZE VS REVENUE
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

plt.scatter(
    store_size_revenue["Store Size"],
    store_size_revenue["Revenue"]
)

plt.title("Store Size vs Revenue")
plt.xlabel("Store Size (Square Meters)")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig(
    OUTPUT_PATH / "Store_Size_vs_Revenue.png",
    dpi=300
)

plt.close()

# ------------------------------------------------------------
# 34. FINAL VALIDATION
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("FINAL VALIDATION")
print("=" * 70)

print(
    f"Revenue              : ${total_revenue:,.2f}"
)

print(
    f"Cost                 : ${total_cost:,.2f}"
)

print(
    f"Profit               : ${total_profit:,.2f}"
)

print(
    f"Revenue - Cost       : ${total_revenue - total_cost:,.2f}"
)

print(
    f"Profit Difference    : "
    f"${total_profit - (total_revenue - total_cost):,.2f}"
)

print(
    f"Units Sold           : {total_units:,.0f}"
)

print(
    f"Orders               : {total_orders:,}"
)

print(
    f"Customers            : {total_customers:,}"
)

print(
    f"Average Order Value  : ${average_order_value:,.2f}"
)

print(
    f"Profit Margin        : {profit_margin:.2f}%"
)

print(
    f"Revenue / Sq Meter   : "
    f"${revenue_per_square_meter:,.2f}"
)

print("\nOutput folder:")
print(OUTPUT_PATH)

print("\n" + "=" * 70)
print("PYTHON EDA COMPLETED SUCCESSFULLY")
print("=" * 70)
