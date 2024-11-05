import pandas as pd
import matplotlib.pyplot as plt
import sys
from datetime import datetime

# Load data from Excel
def load_data(file_path='data/input.xlsx'):
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    return df

# Filter data by month
def filter_by_month(df, month):
    df['Date'] = pd.to_datetime(df['Date'])
    return df[df['Date'].dt.month == month]

# Generate and save a report as an image
def generate_monthly_report(df, month, output_path='output/monthly_report.png'):
    plt.figure(figsize=(10, 6))

    # Total income and expenses for the month
    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
    balance = total_income - total_expense

    # Display summary
    plt.subplot(2, 1, 1)
    plt.bar(['Income', 'Expenses', 'Balance'], [total_income, total_expense, balance], color=['green', 'red', 'blue'])
    plt.title(f"Financial Summary for Month {month}")
    plt.ylabel("Amount")

    # Display detailed transactions
    plt.subplot(2, 1, 2)
    df.groupby('Category')['Amount'].sum().plot(kind='bar', color='orange')
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    # Save the dashboard as an image
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# Main function to load data, filter, and generate report
def main(month):
    df = load_data()
    month = int(month)  # Ensure month is an integer
    monthly_data = filter_by_month(df, month)
    generate_monthly_report(monthly_data, month)

if __name__ == "__main__":
    # Accept month as a command-line argument
    if len(sys.argv) > 1:
        month = sys.argv[1]
        main(month)
    else:
        print("Please provide the month as an argument, e.g., 'python filter_and_visualize.py 10'")
