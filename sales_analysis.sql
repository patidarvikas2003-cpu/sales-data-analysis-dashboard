-- Sales Data Analysis SQL Queries

-- 1. Total net sales
SELECT ROUND(SUM(net_sales), 2) AS total_net_sales
FROM sales_data;

-- 2. Total orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM sales_data;

-- 3. Total quantity sold
SELECT SUM(quantity) AS total_quantity
FROM sales_data;

-- 4. Average order value
SELECT ROUND(SUM(net_sales) / COUNT(DISTINCT order_id), 2) AS average_order_value
FROM sales_data;

-- 5. Category-wise sales
SELECT category,
       ROUND(SUM(net_sales), 2) AS total_sales
FROM sales_data
GROUP BY category
ORDER BY total_sales DESC;

-- 6. City-wise sales
SELECT city,
       ROUND(SUM(net_sales), 2) AS total_sales
FROM sales_data
GROUP BY city
ORDER BY total_sales DESC;

-- 7. Top 10 products
SELECT product,
       ROUND(SUM(net_sales), 2) AS total_sales
FROM sales_data
GROUP BY product
ORDER BY total_sales DESC
LIMIT 10;

-- 8. Monthly sales
SELECT DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
       ROUND(SUM(net_sales), 2) AS total_sales
FROM sales_data
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY sales_month;

-- 9. Category and city performance
SELECT city, category,
       ROUND(SUM(net_sales), 2) AS total_sales
FROM sales_data
GROUP BY city, category
ORDER BY total_sales DESC;

-- 10. Highest-value order
SELECT order_id, city, category, product,
       quantity, net_sales
FROM sales_data
ORDER BY net_sales DESC
LIMIT 1;
