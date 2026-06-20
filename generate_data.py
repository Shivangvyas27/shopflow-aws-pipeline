import pandas as pd
from faker import Faker
import random

fake = Faker()

categories = ["Electronics", "Books", "Clothing", "Home & Kitchen", 
              "Sports", "Beauty", "Toys", "Automotive"]

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

rows = []
for _ in range(10000):
    product = random.choice(products)
    quantity = random.randint(1, 5)
    rows.append({
        "order_id":       fake.uuid4(),
        "customer_id":    fake.uuid4(),
        "product_name":   product[0],
        "category":       product[1],
        "price":          product[2],
        "quantity":       quantity,
        "revenue":        round(product[2] * quantity, 2),
        "rating":         round(random.uniform(1, 5), 1),
        "order_date":     fake.date_between(start_date="-1y", end_date="today"),
        "customer_city":  fake.city(),
        "customer_state": fake.state(),
    })

df = pd.DataFrame(rows)
df.to_csv("shopflow_orders.csv", index=False)
print(f"Done! {len(df)} rows saved to shopflow_orders.csv")
print(df.head())
