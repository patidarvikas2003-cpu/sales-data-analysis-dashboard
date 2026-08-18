import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../data/sales_data.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Basic information
print("Shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

# KPIs
total_sales = df["Net_Sales"].sum()
total_orders = df["Order_ID"].nunique()
total_quantity = df["Quantity"].sum()
avg_order_value = total_sales / total_orders

print(f"\nTotal Net Sales: {total_sales:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Quantity: {total_quantity}")
print(f"Average Order Value: {avg_order_value:,.2f}")

# Category analysis
category_sales = (
    df.groupby("Category")["Net_Sales"]
      .sum()
      .sort_values(ascending=False)
)
print("\nCategory-wise Sales:")
print(category_sales)

# City analysis
city_sales = (
    df.groupby("City")["Net_Sales"]
      .sum()
      .sort_values(ascending=False)
)
print("\nCity-wise Sales:")
print(city_sales)

# Monthly trend
monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Net_Sales"]
      .sum()
)
print("\nMonthly Sales:")
print(monthly_sales)

# Top 10 products
top_products = (
    df.groupby("Product")["Net_Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)
print("\nTop 10 Products:")
print(top_products)

# Charts
category_sales.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Net Sales")
plt.tight_layout()
plt.savefig("../charts/category_sales.png")
plt.close()

monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Net Sales")
plt.tight_layout()
plt.savefig("../charts/monthly_sales.png")
plt.close()
