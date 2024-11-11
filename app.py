import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load data
def load_data(file_path='data/Finance.xlsx', sheet_name='Sheet1'):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df[['Date', 'Category', 'Income', 'Cost']]  # Updated column name

# Filter data by date range
def filter_data(df, start_date, end_date):
    df['Date'] = pd.to_datetime(df['Date'])
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    return df.loc[mask]

# Generate pie chart for income vs cost
def plot_income_cost_pie(df):
    income = df['Income'].sum()
    cost = df['Cost'].sum()
    labels = ['Income', 'Cost']
    sizes = [income, cost]
    
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#76c7c0', '#ff6f61'])
    plt.title("Income vs Cost")
    st.pyplot(plt)  # Display the plot in Streamlit
    plt.close()

# Generate bar chart for cost by category
def plot_cost_by_category(df):
    category_cost = df.groupby('Category')['Cost'].sum()
    category_cost = category_cost.sort_values()
    
    plt.figure(figsize=(10, 6))
    category_cost.plot(kind='barh', color='#ff6f61')
    plt.xlabel("Cost")
    plt.ylabel("Category")
    plt.title("Cost by Category")
    st.pyplot(plt)  # Display the plot in Streamlit
    plt.close()

# Streamlit interface
def main():
    st.title("Personal Finance Tracker")
    
    # Load and display data
    df = load_data()

    # Date input from user
    start_date = st.date_input("Start Date", datetime.today())
    end_date = st.date_input("End Date", datetime.today())

    # Filter data based on user input
    filtered_df = filter_data(df, start_date, end_date)

    # Display the charts
    st.subheader("Income vs Cost")
    plot_income_cost_pie(filtered_df)
    
    st.subheader("Cost by Category")
    plot_cost_by_category(filtered_df)

if __name__ == "__main__":
    main()
