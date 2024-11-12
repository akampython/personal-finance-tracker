import pandas as pd

def filter_data(df, start_date, end_date):
    # Ensure the 'Date' column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Ensure start_date and end_date are datetime objects
    start_date = pd.to_datetime(start_date, errors='coerce')
    end_date = pd.to_datetime(end_date, errors='coerce')
    
    # Filter data based on the date range
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    return df.loc[mask]

# Example main function
def main():
    # Sample data
    data = {'Date': ['2024-11-10', '2024-11-12', '2024-11-15'],
            'Value': [10, 20, 30]}
    df = pd.DataFrame(data)
    
    # Example input
    start_date = '2024/11/12'
    end_date = '2024/11/12'
    
    # Filter data
    filtered_df = filter_data(df, start_date, end_date)
    print(filtered_df)

if __name__ == "__main__":
    main()
