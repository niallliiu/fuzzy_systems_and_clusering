import os
import csv

def count_unique_days_in_folder(folder_path):
    unique_days = set()  # Use a set to store unique dates
    file_count = 0
    total_rows_processed = 0

    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):  # Only process CSV files
            file_path = os.path.join(folder_path, file_name)
            print(f"Processing file: {file_name}")

            try:
                with open(file_path, 'r', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile, delimiter=';')

                    # Skip the header row
                    header = next(reader)
                    
                    for row in reader:
                        total_rows_processed += 1
                        # Extract the "Dato" column (6th column, index 5)
                        date = row[5]
                        unique_days.add(date)  # Add date to the global set

                    file_count += 1

            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

    # Print summary
    print(f"\nProcessed {file_count} CSV file(s)")
    print(f"Total rows processed: {total_rows_processed}")
    print(f"Total unique days across all files: {len(unique_days)}")
    print("Unique days:", sorted(unique_days))

# Replace with the path to your folder containing CSV files
folder_path = "downloads"
count_unique_days_in_folder(folder_path)
