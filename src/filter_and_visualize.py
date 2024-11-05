import pandas as pd
import matplotlib.pyplot as plt
import sys

# Load data from Excel
def load_data(file_path='data/input.xlsx'):
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    df.columns = df.columns.str.strip()  # Remove any leading/trailing whitespace
    print("Column names:", df.columns)  # Print the column names for debugging
    return df

# Filter data by month
def filter_by_month(df, month):
    df['date'] = pd.to_datetime(df['date'])
    return df[df['date'].dt.month == month]

# Generate and save a report as an image
def generate_monthly_report(df, month, output_path='output/monthly_report.png'):
    plt.figure(figsize=(10, 6))

    # Grouping by category to summarize income and expenses
    category_summary = df.groupby('category')['amount'].sum()

    # Assuming categories contain 'Income' and 'Expense'
    total_income = category_summary.get('Income', 0)
    total_expense = category_summary.get('Expense', 0)
    balance = total_income - total_expense

    # Display summary
    plt.subplot(2, 1, 1)
    plt.bar(['Income', 'Expenses', 'Balance'], [total_income, total_expense, balance], color=['green', 'red', 'blue'])
    plt.title(f"Financial Summary for Month {month}")
    plt.ylabel("Amount")

    # Display detailed transactions by category
    plt.subplot(2, 1, 2)
    category_summary.plot(kind='bar', color='orange')
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
