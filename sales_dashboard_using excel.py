import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("sales_data.csv")  # Replace with your file path

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Add a 'Month' column
data['Month'] = data['Date'].dt.to_period('M')

# Group data by Month and Product
monthly_sales = data.groupby(['Month', 'Product']).agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Revenue=('Revenue', 'sum')
).reset_index()

# Save processed data for Excel
monthly_sales.to_excel("monthly_sales_summary.xlsx", index=False)

# Plotting total revenue by product
pivot = monthly_sales.pivot(index='Month', columns='Product', values='Total_Revenue')
pivot.plot(kind='bar', figsize=(10, 6))
plt.title('Monthly Revenue by Product')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.legend(title='Product')
plt.tight_layout()
plt.savefig("monthly_revenue_plot.png")  # Save the plot
plt.show()
