import csv
import os
import sys
from pathlib import Path


# Function to extract the columns we want from the downloaded csv file
def extract_columns(columns):
    download_dir = Path(sys.argv[1])  # Use the download directory passed as an argument
    # Get the latest downloaded file
    files = os.listdir(download_dir) # Get all the files in the downloads folder
    files.sort(key=lambda x: os.path.getmtime(os.path.join(download_dir, x))) # Sort the files by date
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
