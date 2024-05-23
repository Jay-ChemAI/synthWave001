import csv
import os
import sys
from pathlib import Path

# Function to extract the columns we want from the downloaded csv file
def extract_columns(columns):
    download_dir = Path(os.getcwd()).joinpath('bots').joinpath('CMS_Provider_data').joinpath('dataset')  # Use the current directory plus '/dataset' as the download directory
    print(f"Download directory: {download_dir}")  # Print the download directory

    # Get the latest downloaded file
    files = [f for f in os.listdir(download_dir) if f.startswith('HH_')] # Get all the files in the downloads folder that start with 'HH_'
    files.sort(key=lambda x: os.path.getmtime(os.path.join(download_dir, x))) # Sort the files by date

    # Check if files list is not empty
    if not files:
        print("No files found that start with 'HH_' in the directory.")
        return

    input_file = os.path.join(download_dir, files[-1]) # Get the latest file

    # Create a new csv file with the columns we want
    output_base_name = 'cms_data.csv'
    output_file = os.path.join(download_dir, output_base_name)
    count = 1

    # Check if the file already exists
    while os.path.exists(output_file):
        count += 1
        output_file = os.path.join(download_dir, f'cms_data_{count}.csv')

    # Open the input and output files
    with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out: # Open the input and output files
        reader = csv.DictReader(csv_in) # Read the input file
        writer = csv.DictWriter(csv_out, fieldnames=columns) # Write the output file with the columns we want
        writer.writeheader()   # Write the header of the output file
        for row in reader: # Read a row from the input file
            writer.writerow({column: row.get(column, '') for column in columns}) # Write the row to the output file

    # Remove the input file
    os.remove(input_file)

# Use the function
extract_columns(['CMS Certification Number (CCN)', 'Provider Name', 'ZIP Code', 'Quality of patient care star rating']) # Extract the columns we want
