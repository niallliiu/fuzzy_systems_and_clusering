import pandas as pd

# Load the CSV file
csv_file = 'Helsfyr_filtered.csv'
data = pd.read_csv(csv_file)

# Parse the 'Dato' column to datetime
data['Dato'] = pd.to_datetime(data['Dato'])

# Function to filter data by date and hour without calculating totals
def extract_hourly_vehicle_lengths(date, hour):
    """
    Extract data for a specific date and hour range (1-24) with vehicle lengths.
    :param date: Date to filter (YYYY-MM-DD format).
    :param hour: Hour to filter (1-24).
    :return: Filtered data with vehicle lengths for the specified time range.
    """
    # Adjust hour to fit the 'Time Range' format
    start_hour = f"{hour - 1:02d}:00"
    end_hour = f"{hour:02d}:00"

    # Filter the data for the given date and hour range
    filtered_data = data[
        (data['Dato'] == date) &
        (data['Fra tidspunkt'] == start_hour) &
        (data['Til tidspunkt'] == end_hour) &
        (data['Felt'].str.contains('retning|Totalt'))
    ]

    # Select relevant columns including vehicle lengths
    vehicle_length_columns = ['< 5,6m', '>= 5,6m', '5,6m - 7,6m', '7,6m - 12,5m', '12,5m - 16,0m', '>= 16,0m', '16,0m - 24,0m', '>= 24,0m']
    result = filtered_data[['Felt', 'Dato', 'Fra tidspunkt', 'Til tidspunkt'] + vehicle_length_columns]

    if result.empty:
        print(f"No data found for {date} during hour {hour}.")
    else:
        print(f"Data for {date} during hour {hour}:")
        #print(result)

    return result

# Example usage
selected_date = '2023-10-31'  # Input your desired date here
selected_hour = 1  # Input the hour you want to filter (1-24)

# Call the function
filtered_data = extract_hourly_vehicle_lengths(selected_date, selected_hour)


