-- ============================================================
-- Global Electronics Retail Business Analytics
-- SQL Analysis Project
-- Dataset: Maven Analytics - Global Electronics Retailer
-- ============================================================

-- Objective:
-- Analyze sales, revenue, profitability, customers,
-- products, brands, and geographic performance.

-- 1. Total Revenue
SELECT
    SUM(Quantity * UnitPriceUSD) AS Total_Revenue
FROM Sales_Cleaned
JOIN Products_Cleaned
    ON Sales_Cleaned.ProductKey = Products_Cleaned.ProductKey;

-- 2. Total Cost
SELECT
    SUM(Quantity * UnitCostUSD) AS Total_Cost
FROM Sales_Cleaned
JOIN Products_Cleaned
    ON Sales_Cleaned.ProductKey = Products_Cleaned.ProductKey;

-- 3. Total Profit
SELECT
    SUM(Quantity * (UnitPriceUSD - UnitCostUSD)) AS Total_Profit
FROM Sales_Cleaned
JOIN Products_Cleaned
    ON Sales_Cleaned.ProductKey = Products_Cleaned.ProductKey;

-- 4. Profit Margin %
SELECT
    SUM(Quantity * (UnitPriceUSD - UnitCostUSD))
    / NULLIF(SUM(Quantity * UnitPriceUSD), 0) * 100 AS Profit_Margin_Percent
FROM Sales_Cleaned
JOIN Products_Cleaned
    ON Sales_Cleaned.ProductKey = Products_Cleaned.ProductKey;

-- 5. Revenue by Category
SELECT
    p.Category,
    SUM(s.Quantity * p.UnitPriceUSD) AS Total_Revenue
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey
GROUP BY p.Category
ORDER BY Total_Revenue DESC;

-- 6. Revenue by Subcategory
SELECT
    p.Subcategory,
    SUM(s.Quantity * p.UnitPriceUSD) AS Total_Revenue
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey
GROUP BY p.Subcategory
ORDER BY Total_Revenue DESC;

-- 7. Revenue by Brand
SELECT
    p.Brand,
    SUM(s.Quantity * p.UnitPriceUSD) AS Total_Revenue
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey
GROUP BY p.Brand
ORDER BY Total_Revenue DESC;

-- 8. Profit by Category
SELECT
    p.Category,
    SUM(s.Quantity * (p.UnitPriceUSD - p.UnitCostUSD)) AS Total_Profit
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey
GROUP BY p.Category
ORDER BY Total_Profit DESC;

-- 9. Profit by Subcategory
SELECT
    p.Subcategory,
    SUM(s.Quantity * (p.UnitPriceUSD - p.UnitCostUSD)) AS Total_Profit
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey
GROUP BY p.Subcategory
ORDER BY Total_Profit DESC;

-- 10. Top 10 Products by Revenue
SELECT
    p.[Product Name],
    SUM(s.Quantity * p.UnitPriceUSD) AS Total_Revenue
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey
GROUP BY p.[Product Name]
ORDER BY Total_Revenue DESC
LIMIT 10;

-- 11. Top 10 Customers by Revenue
SELECT
    c.CustomerKey,
    c.Name,
    SUM(s.Quantity * p.UnitPriceUSD) AS Total_Revenue
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey
JOIN Customer_Cleaned c
    ON s.CustomerKey = c.CustomerKey
GROUP BY c.CustomerKey, c.Name
ORDER BY Total_Revenue DESC
LIMIT 10;

-- 12. Revenue by Country
SELECT
    c.Country,
    SUM(s.Quantity * p.UnitPriceUSD) AS Total_Revenue
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey
JOIN Customer_Cleaned c
    ON s.CustomerKey = c.CustomerKey
GROUP BY c.Country
ORDER BY Total_Revenue DESC;

-- 13. Revenue by State
SELECT
    c.State,
    SUM(s.Quantity * p.UnitPriceUSD) AS Total_Revenue
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey
JOIN Customer_Cleaned c
    ON s.CustomerKey = c.CustomerKey
GROUP BY c.State
ORDER BY Total_Revenue DESC;

-- 14. Total Orders
SELECT
    COUNT(DISTINCT [Order Number]) AS Total_Orders
FROM Sales_Cleaned;

-- 15. Total Units Sold
SELECT
    SUM(Quantity) AS Total_Units_Sold
FROM Sales_Cleaned;

-- 16. Average Order Value
SELECT
    SUM(s.Quantity * p.UnitPriceUSD)
    / NULLIF(COUNT(DISTINCT s.[Order Number]), 0) AS Average_Order_Value
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey;

-- 17. Total Customers
SELECT
    COUNT(DISTINCT CustomerKey) AS Total_Customers
FROM Sales_Cleaned;

-- 18. Customer Distribution by Country
SELECT
    c.Country,
    COUNT(DISTINCT c.CustomerKey) AS Total_Customers
FROM Sales_Cleaned s
JOIN Customer_Cleaned c
    ON s.CustomerKey = c.CustomerKey
GROUP BY c.Country
ORDER BY Total_Customers DESC;

-- 19. Revenue by Product
SELECT
    p.[Product Name],
    SUM(s.Quantity * p.UnitPriceUSD) AS Total_Revenue
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey
GROUP BY p.[Product Name]
ORDER BY Total_Revenue DESC;

-- 20. Profit by Brand
SELECT
    p.Brand,
    SUM(s.Quantity * (p.UnitPriceUSD - p.UnitCostUSD)) AS Total_Profit
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey
GROUP BY p.Brand
ORDER BY Total_Profit DESC;

-- 21. Monthly Revenue Trend
SELECT
    YEAR(s.[Order Date]) AS Order_Year,
    MONTH(s.[Order Date]) AS Order_Month,
    SUM(s.Quantity * p.UnitPriceUSD) AS Total_Revenue
FROM Sales_Cleaned s
JOIN Products_Cleaned p
    ON s.ProductKey = p.ProductKey
GROUP BY
    YEAR(s.[Order Date]),
    MONTH(s.[Order Date])
ORDER BY
    Order_Year ASC,
    Order_Month ASC;





