-- Create database
CREATE DATABASE IF NOT EXISTS shopflow_db;

-- Create table on S3
CREATE EXTERNAL TABLE shopflow_db.orders (
  order_id        string,
  customer_id     string,
  product_name    string,
  category        string,
  price           double,
  quantity        int,
  revenue         double,
  rating          double,
  order_date      string,
  customer_city   string,
  customer_state  string
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://your-bucket-name/'
TBLPROPERTIES ('skip.header.line.count'='1');

-- Revenue by category
SELECT category, 
       COUNT(*) as total_orders,
       SUM(revenue) as total_revenue
FROM shopflow_db.orders
GROUP BY category
ORDER BY total_revenue DESC;

-- Top 5 products
SELECT product_name,
       COUNT(*) as times_ordered,
       SUM(revenue) as total_revenue
FROM shopflow_db.orders
GROUP BY product_name
ORDER BY total_revenue DESC
LIMIT 5;

-- Average order value by state
SELECT customer_state,
       COUNT(*) as total_orders,
       ROUND(AVG(revenue), 2) as avg_order_value
FROM shopflow_db.orders
GROUP BY customer_state
ORDER BY avg_order_value DESC
LIMIT 10;

-- Monthly revenue trend
SELECT order_date,
       COUNT(*) as orders,
       SUM(revenue) as daily_revenue
FROM shopflow_db.orders
GROUP BY order_date
ORDER BY order_date ASC;

-- Data quality check
SELECT 
  COUNT(*) as total_rows,
  COUNT(CASE WHEN product_name IS NULL 
             OR product_name = '' THEN 1 END) as blank_products,
  COUNT(CASE WHEN category IS NULL 
             OR category = '' THEN 1 END) as blank_categories,
  COUNT(CASE WHEN revenue IS NULL THEN 1 END) as null_revenue
FROM shopflow_db.orders;
