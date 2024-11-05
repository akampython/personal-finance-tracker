import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Load the data
file_path = 'data/input.xlsx'
sheet_name = 'Sheet1'
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Ask user for the month to filter
month_input = input("Enter the month to filter (e.g., '2023-03' for March 2023): ")
month_filter = datetime.strptime(month_input, "%Y-%m")

# Filter data for the specified month
data['date'] = pd.to_datetime(data['date'], errors='coerce')
filtered_data = data[data['date'].dt.to_period('M') == month_filter.to_period('M')]

# Separate income and expenses for the pie chart
income = filtered_data[filtered_data['amount'] > 0]['amount'].sum()
expenses = -filtered_data[filtered_data['amount'] < 0]['amount'].sum()

# Create directory for artifacts
os.makedirs('artifacts', exist_ok=True)

# Generate the pie chart for income and expenses
plt.figure(figsize=(6, 6))
plt.pie([income, expenses], labels=['Income', 'Expenses'], autopct='%1.1f%%', colors=['#4CAF50', '#F44336'])
plt.title('Income vs Expenses')
plt.savefig('artifacts/piechart.png')
plt.close()

# Generate the bar chart for expenses by category
expenses_by_category = filtered_data[filtered_data['amount'] < 0].groupby('category')['amount'].sum().abs()
plt.figure(figsize=(10, 6))
expenses_by_category.plot(kind='bar', color=['#FFB6C1', '#FFC0CB', '#FF69B4', '#FF1493'])
plt.xlabel('Category')
plt.ylabel('Amount')
plt.title('Expenses by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('artifacts/barchart.png')
plt.close()

print("Artifacts generated and saved in the 'artifacts' folder.")
