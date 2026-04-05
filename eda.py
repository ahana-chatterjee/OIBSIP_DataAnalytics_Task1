import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("retail_sales_dataset.csv")

# Display basic info
print(df.head())
print(df.info())
print(df.describe())

# Data Cleaning
# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Remove duplicates
df = df.drop_duplicates()

# Check missing values
print(df.isnull().sum())

# -----------------------------
# Time Series Analysis
# -----------------------------
sales_trend = df.groupby('Date')['Total Amount'].sum()

plt.figure(figsize=(10,5))
sales_trend.plot()
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()

# -----------------------------
# Gender Analysis
# -----------------------------
sns.barplot(x='Gender', y='Total Amount', data=df)
plt.title("Sales by Gender")
plt.show()

# -----------------------------
# Age Distribution
# -----------------------------
sns.histplot(df['Age'], bins=10)
plt.title("Age Distribution")
plt.show()

# -----------------------------
# Product Category Analysis
# -----------------------------
category_sales = df.groupby('Product Category')['Total Amount'].sum()

category_sales.plot(kind='bar')
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

# -----------------------------
# Quantity vs Total Amount
# -----------------------------
sns.scatterplot(x='Quantity', y='Total Amount', data=df)
plt.title("Quantity vs Total Amount")
plt.show()

# -----------------------------
# Heatmap
# -----------------------------
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()