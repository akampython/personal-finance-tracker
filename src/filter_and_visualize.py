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

# Generate and save a report as images
def generate_reports(df, month):
    # Grouping by category to summarize income and expenses
    category_summary = df.groupby('category')['amount'].sum()

    # Assuming categories contain 'Income' and 'Expense'
    total_income = category_summary.get('Income', 0)
    total_expense = category_summary.get('Expense', 0)

    # Create a bar chart for income and expenses
    plt.figure(figsize=(10, 6))
    plt.bar(['Income', 'Expenses'], [total_income, total_expense], color=['green', 'red'])
    plt.title(f"Income and Expenses Summary for Month {month}")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig('output/income_expenses_summary.png')  # Save the bar chart
    plt.close()

    # Create a pie chart for expenses by category
    plt.figure(figsize=(8, 8))
    expense_categories = category_summary[category_summary < 0]  # Only expenses (if negative)
    expense_categories.plot.pie(autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
    plt.title("Expenses by Category")
    plt.ylabel("")  # Remove y-label for aesthetics
    plt.tight_layout()
    plt.savefig('output/expenses_by_category.png')  # Save the pie chart
    plt.close()

# Main function to load data, filter, and generate reports
def main(month):
    df = load_data()
    month = int(month)  # Ensure month is an integer
    monthly_data = filter_by_month(df, month)
    generate_reports(monthly_data, month)

if __name__ == "__main__":
    # Accept month as a command-line argument
    if len(sys.argv) > 1:
        month = sys.argv[1]
        main(month)
    else:
        print("Please provide the month as an argument, e.g., 'python filter_and_visualize.py 10'")
