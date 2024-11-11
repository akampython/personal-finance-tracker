import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load data
def load_data(file_path='data/Finance.xlsx', sheet_name='Sheet1'):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    print("Columns in Excel file:", df.columns)  # Print column names for debugging
    return df[['Date', 'Category', 'Income', 'Cost']]  # Updated column name

# Filter data by date range
def filter_data(df, start_date, end_date):
    df['Date'] = pd.to_datetime(df['Date'])
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    return df.loc[mask]

# Generate pie chart for income vs cost
def plot_income_cost_pie(df, output_path='artifacts/income_cost_piechart.png'):
    income = df['Income'].sum()
    cost = df['Cost'].sum()
    labels = ['Income', 'Cost']
    sizes = [income, cost]
    
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#76c7c0', '#ff6f61'])
    plt.title("Income vs Cost")
    plt.savefig(output_path)
    plt.close()

# Generate bar chart for cost by category
def plot_cost_by_category(df, output_path='artifacts/cost_category_barchart.png'):
    category_cost = df.groupby('Category')['Cost'].sum()
    category_cost = category_cost.sort_values()
    
    plt.figure(figsize=(10, 6))
    category_cost.plot(kind='barh', color='#ff6f61')
    plt.xlabel("Cost")
    plt.ylabel("Category")
    plt.title("Cost by Category")
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
    plot_income_cost_pie(filtered_df)
    plot_cost_by_category(filtered_df)

    print("Charts generated and saved in the 'artifacts' folder.")

if __name__ == "__main__":
    main()
