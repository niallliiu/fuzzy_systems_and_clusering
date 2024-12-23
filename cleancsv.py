import pandas as pd

# Define the file path
file_path = 'downloads\Helsfyr_data_2023-10-31_to_2024-11-01.csv'  # Replace with your actual file name

# Load the CSV file with the correct delimiter
data = pd.read_csv(file_path, delimiter=';')

# Inspect column names for debugging
print("Columns in the file:", data.columns.tolist())

# Drop unnecessary columns
columns_to_drop = [
    'Fra', 'Til', 'Vegreferanse', 'Dekningsgrad (%)', 
    'Antall timer total', 'Antall timer inkludert', 
    'Antall timer ugyldig', 'Ikke gyldig lengde', 
    'Lengdekvalitetsgrad (%)'
]
existing_columns_to_drop = [col for col in columns_to_drop if col in data.columns]
data = data.drop(columns=existing_columns_to_drop, axis=1)

# Filter rows to keep only 'Totalt i retning Alnabru', 'Totalt i retning Sentrum', and 'Totalt'
rows_to_keep = ['Totalt i retning Alnabru', 'Totalt i retning Sentrum', 'Totalt']
if 'Felt' in data.columns:
    data = data[data['Felt'].isin(rows_to_keep)]
else:
    print("Error: 'Felt' column not found. Ensure the CSV file has the correct format.")
    exit()

# Save the cleaned data to a new CSV file
output_file = 'Helsfyr_filtered.csv'
data.to_csv(output_file, index=False, encoding='utf-8')

print(f"Processing complete. Filtered data saved to '{output_file}'.")
