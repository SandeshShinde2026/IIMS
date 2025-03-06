import mysql.connector
import pandas as pd

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sandesh@5535",
    database="warehousedb"
)

cursor = db.cursor()

# Fetch sales data from orders table
query = "SELECT TransactionDate, ItemName, SUM(Amount) AS total_sold FROM ordersdb GROUP BY TransactionDate, ItemName;"
cursor.execute(query)
data = cursor.fetchall()

# Convert to Pandas DataFrame
df = pd.DataFrame(data, columns=["date", "product", "quantity"])
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce") # Convert to datetime format

# Save data to CSV for AI training
df.to_csv("sales_data.csv", index=False)

print("✅ Sales data fetched and saved as sales_data.csv")

cursor.close()
db.close()
