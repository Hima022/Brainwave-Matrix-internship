import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Dataset
file_path = r"C:\Users\user\Downloads\real_time_sales_data.csv"  # Replace with your file path if needed
sales_data = pd.read_csv(file_path, parse_dates=['Timestamp'])

# Step 2: Data Overview
print("Dataset Overview:")
print(sales_data.head())

# Step 3: Compute Key Metrics
# Add a total sales column
sales_data['Total Sales'] = sales_data['Price'] * sales_data['Quantity']

# Compute total revenue
total_revenue = sales_data['Total Sales'].sum()

# Top-selling items
top_items = sales_data.groupby('Item Name')['Total Sales'].sum().sort_values(ascending=False)

# Sales by category
sales_by_category = sales_data.groupby('Category')['Total Sales'].sum()

# Step 4: Print Key Metrics
print(f"\nTotal Revenue: ${total_revenue:,.2f}")
print("\nTop-Selling Items:")
print(top_items.head(5))
print("\nSales by Category:")
print(sales_by_category)

# Step 5: Visualize Metrics
# Bar chart for top items
plt.figure(figsize=(10, 5))
top_items.head(5).plot(kind='bar', color='skyblue')
plt.title('Top 5 Best-Selling Items')
plt.xlabel('Item Name')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie chart for sales by category
plt.figure(figsize=(8, 8))
sales_by_category.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Sales by Category')
plt.ylabel("")  # Remove y-axis label
plt.tight_layout()
plt.show()
