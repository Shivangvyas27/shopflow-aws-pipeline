import boto3
import json
import random
import time
from datetime import datetime
from faker import Faker

fake = Faker()
kinesis = boto3.client('kinesis', region_name='ap-south-1')

products = [
    ("Wireless Earbuds", "Electronics", 29.99),
    ("Python Crash Course", "Books", 19.99),
    ("Running Shoes", "Clothing", 59.99),
    ("Air Fryer", "Home & Kitchen", 89.99),
    ("Yoga Mat", "Sports", 24.99),
    ("Face Moisturizer", "Beauty", 14.99),
    ("LEGO Set", "Toys", 49.99),
    ("Car Phone Mount", "Automotive", 12.99),
    ("Bluetooth Speaker", "Electronics", 39.99),
    ("Knife Set", "Home & Kitchen", 34.99),
]

def generate_order():
    product = random.choice(products)
    quantity = random.randint(1, 5)
    return {
        "order_id":       fake.uuid4(),
        "customer_id":    fake.uuid4(),
        "product_name":   product[0],
        "category":       product[1],
        "price":          product[2],
        "quantity":       quantity,
        "revenue":        round(product[2] * quantity, 2),
        "rating":         round(random.uniform(1, 5), 1),
        "order_date":     datetime.now().strftime("%Y-%m-%d"),
        "timestamp":      datetime.now().isoformat(),
        "customer_city":  fake.city(),
        "customer_state": fake.state(),
    }

print("Starting order stream... Press Ctrl+C to stop\n")

while True:
    order = generate_order()
    kinesis.put_record(
        StreamName='shopflow-orders-stream',
        Data=json.dumps(order),
        PartitionKey=order['order_id']
    )
    print(f"✅ Sent: {order['product_name']} | "
          f"qty: {order['quantity']} | "
          f"${order['revenue']} | "
          f"{order['timestamp']}")
    time.sleep(1)
