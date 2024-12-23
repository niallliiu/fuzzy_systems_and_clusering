import pandas as pd

def process_traffic_data(file_path, start_date, end_date):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Ensure the "Dato" column is a datetime format for filtering
    df['Dato'] = pd.to_datetime(df['Dato'], format='%Y-%m-%d')

    # Filter the rows based on the date range
    df = df[(df['Dato'] >= pd.to_datetime(start_date)) & (df['Dato'] <= pd.to_datetime(end_date))]

    # Filter rows to keep only "Totalt i retning Alnabru" and "Totalt i retning Sentrum"
    directions = ["Totalt i retning Alnabru", "Totalt i retning Sentrum"]
    df = df[df["Felt"].isin(directions)]

    # Loop through each unique hour and print the results
    grouped = df.groupby(["Dato", "Time Range"])
    for (date, time_range), group in grouped:
        print(f"Date: {date.strftime('%Y-%m-%d')}, Time Range: {time_range}")
        for direction in directions:
            direction_data = group[group["Felt"] == direction]
            if not direction_data.empty:
                total_cars = direction_data["Trafikkmengde"].values[0]
                car_sizes = {
                    "< 5,6m": direction_data["< 5,6m"].values[0],
                    ">= 5,6m": direction_data[">= 5,6m"].values[0],
                    "5,6m - 7,6m": direction_data["5,6m - 7,6m"].values[0],
                    "7,6m - 12,5m": direction_data["7,6m - 12,5m"].values[0],
                    "12,5m - 16,0m": direction_data["12,5m - 16,0m"].values[0],
                    ">= 16,0m": direction_data[">= 16,0m"].values[0],
                    "16,0m - 24,0m": direction_data["16,0m - 24,0m"].values[0],
                    ">= 24,0m": direction_data[">= 24,0m"].values[0],
                }
                print(f"  Direction: {direction}")
                print(f"    Total Cars: {total_cars}")
                print(f"    Car Sizes: {car_sizes}")

    # Print the number of lanes for reference
    lanes_each_direction = 2  # Assuming 2 lanes each direction
    print(f"\nNumber of lanes in each direction: {lanes_each_direction}")


# Example usage
file_path = "Helsfyr_cleaned.csv"  # Replace with your actual file path
start_date = "2023-10-31"  # Replace with your desired start date
end_date = "2023-10-31"    # Replace with your desired end date

process_traffic_data(file_path, start_date, end_date)
