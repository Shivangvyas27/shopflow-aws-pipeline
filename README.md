# ShopFlow — AWS E-Commerce Data Pipeline

A production-style, end-to-end data engineering project built on AWS, simulating an Amazon-scale e-commerce data pipeline.

## Architecture
Raw Data → S3 Data Lake → Kinesis Streams → Firehose → S3

↓

Glue ETL Job

↓

Processed S3 Data

↓

Athena SQL Queries

↓

QuickSight Dashboard
## Tech Stack

| Layer | Service |
|-------|---------|
| Data Generation | Python, Faker |
| Data Lake | AWS S3 |
| Streaming | Amazon Kinesis Data Streams |
| Delivery | Amazon Kinesis Firehose |
| ETL | AWS Glue Visual ETL |
| Querying | Amazon Athena |
| Warehouse | Amazon Redshift Serverless |
| Visualization | Amazon QuickSight |
| Language | Python, SQL |

## What This Project Does

- Generates 10,000+ realistic e-commerce orders using Python and Faker
- Streams live order events every second via Kinesis Data Streams
- Automatically lands streaming data in S3 via Kinesis Firehose
- Cleans and transforms raw data using AWS Glue ETL job (removes nulls, filters bad data)
- Queries cleaned data using SQL in Amazon Athena (no database server needed)
- Loads data into Redshift Serverless data warehouse using COPY command
- Visualizes business insights in Amazon QuickSight dashboard

## Dashboard Insights

- Revenue by product category (bar chart)
- Top 10 best selling products (bar chart)
- Daily order quantity trend (line chart)
- Average rating by category (bar chart)
- Revenue share by category (pie chart)

## Project Structure
shopflow-aws-pipeline/

├── generate_data.py       # Generates 10,000 fake orders as CSV

├── producer.py            # Streams live orders to Kinesis every second

├── athena_queries.sql     # SQL queries for data analysis on S3

├── screenshots/           # AWS console screenshots

└── README.md

## How To Run

### Prerequisites
```bash
pip install faker pandas boto3
aws configure  # Set up AWS credentials
```

### 1. Generate data
```bash
python generate_data.py
# Creates shopflow_orders.csv with 10,000 rows
```

### 2. Upload to S3
```bash
aws s3 cp shopflow_orders.csv s3://your-bucket-name/
```

### 3. Stream live orders
```bash
python producer.py
# Sends one order per second to Kinesis
# Press Ctrl+C to stop
```

### 4. Query with Athena
Run queries from `athena_queries.sql` in AWS Athena console.

## AWS Services Used
S3          → Data lake storage (raw, processed, streaming folders)

Kinesis     → Real-time event streaming (1 order/second)

Firehose    → Auto-delivery from Kinesis to S3

Glue        → Visual ETL pipeline (filter nulls, clean data)

Athena      → SQL queries directly on S3 files

Redshift    → Serverless data warehouse (COPY from S3)

QuickSight  → Business intelligence dashboard

IAM         → Roles and permissions for each service

CloudShell  → Browser-based terminal for running scripts
## Key Learnings

- Designed S3 data lake folder structure (raw/ processed/ streaming/)
- Built real-time streaming pipeline with Kinesis Data Streams + Firehose
- Created ETL jobs using AWS Glue Visual Editor (no code needed)
- Wrote SQL analytics queries on S3 data using Athena
- Loaded data into Redshift Serverless using COPY command
- Built interactive dashboard in Amazon QuickSight
- Managed IAM roles and permissions across multiple AWS services
- Monitored costs and deleted resources to avoid unnecessary charges

## Results
Total orders processed:     10,000

Top category by revenue:    Home & Kitchen ($393,551)

Top product by revenue:     Air Fryer

Pipeline latency:           ~60 seconds (Firehose batch)

Data quality improvement:   Nulls removed via Glue ETL

## Author

**Shivang Vyas**  
Data Analyst & Aspiring Data Engineer  
3+ years at Amazon — Performance Analytics & Reporting  

[LinkedIn](https://linkedin.com/in/shivangvyas) | [GitHub](https://github.com/Shivangvyas27)
