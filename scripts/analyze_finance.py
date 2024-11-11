import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load data
def load_data(file_path='data/Finance.xlsx', sheet_name='Sheet1'):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df[['Date', 'Category', 'Income', 'Expenses']]

# Filter data by date range
def filter_data(df, start_date, end_date):
    df['Date'] = pd.to_datetime(df['Date'])
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    return df.loc[mask]

# Generate pie chart for income vs expenses
def plot_income_expenses_pie(df, output_path='artifacts/income_expenses_piechart.png'):
    income = df['Income'].sum()
    expenses = df['Expenses'].sum()
    labels = ['Income', 'Expenses']
    sizes = [income, expenses]
    
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#76c7c0', '#ff6f61'])
    plt.title("Income vs Expenses")
    plt.savefig(output_path)
    plt.close()

# Generate bar chart for expenses by category
def plot_expenses_by_category(df, output_path='artifacts/expenses_category_barchart.png'):
    category_expenses = df.groupby('Category')['Expenses'].sum()
    category_expenses = category_expenses.sort_values()
    
    plt.figure(figsize=(10, 6))
    category_expenses.plot(kind='barh', color='#ff6f61')
    plt.xlabel("Expenses")
    plt.ylabel("Category")
    plt.title("Expenses by Category")
    plt.savefig(output_path)
    plt.close()

# Main function
def main():
    # Load and display data
    df = load_data()

    # Get date range from user
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Filter data by date range
    filtered_df = filter_data(df, start_date, end_date)

    # Generate and save charts
    plot_income_expenses_pie(filtered_df)
    plot_expenses_by_category(filtered_df)

    print("Charts generated and saved in the 'artifacts' folder.")

if __name__ == "__main__":
    main()
