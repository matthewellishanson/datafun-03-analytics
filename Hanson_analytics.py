
# Standard library imports
import pathlib 
import logging

# External library imports (requires virtual environment)
import requests
import pandas as pd
from nba_api.stats.endpoints import playercareerstats
import numpy as np
import json
import csv

# Local module imports
import utils_matthanson as utils
import Hanson_project_setup as HanPS


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

########################################################################################
# Define functions for fetching and writing data from online sources to text files, csv files, excel files and JSON files.
########################################################################################


########################################################################################
# TXT #
########################################################################################

# Define function to write data to a text file

def write_txt_data(folder_name, filename, data):
    '''Write data to a text file.'''
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        # Try opening the file and writing the data
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
        logging.info(f'Data written to {file_path}') # Log the success
    except IOError as e:
        # Log the error
        logging.error(f'Error writing data to {file_path}: {e}')

# Define function for fetching data from specified APIs or online data sources, including JSON, CSV, and plain text data.
# After fetching, write or save the data to a text file.

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        write_txt_data(folder_name, filename, response.text)
        return response.text
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Process text data: count words and unique words and save to file.

def process_txt_data(folder_name, input_filename, output_filename):
    '''Process text data.'''
    # Read the data from the input file
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    
    try:
        # Try opening the file and reading the data
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except IOError as e:
        # Log the error
        logging.error(f'Error reading data from {file_path}: {e}')
        return
    
    try:
        # Try processing the data
        # For example, count the number of words and unique words
        words = text.split()
        num_words = len(words)
        unique_words = set(words)
        logging.info(f'Number of words: {num_words}')
        logging.info(f'Number of unique words: {len(unique_words)}')

        # Write the processed data to the output file
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(f'Number of words: {num_words}\n')
            output_file.write(f'Number of unique words: {len(unique_words)}\n')
        logging.info(f'Processed data written to {output_path}')

    except IOError as e:
        # Log the error
        logging.error(f'Error processing data: {e}')
        return

########################################################################################
# CSV #
########################################################################################

# Define function to write data to a csv file

def write_csv_data(folder_name, filename, data):
    '''Write data to a csv file.'''
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        # Try opening the file and writing the data
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        logging.info(f'Data written to {file_path}') # Log the success
    except IOError as e:
        # Log the error
        logging.error(f'Error writing data to {file_path}: {e}')

# Define function for fetching data from specified APIs or online data sources, including JSON, CSV, and plain text data.
# After fetching, write or save the data to a text file.

def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        write_csv_data(folder_name, filename, response.text)
        return response.text
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Process csv data: count rows and columns and save to file.

def process_csv_data(folder_name, input_filename, output_filename):
    '''Process csv data.'''
    # Read the data from the input file
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    
    try:
        # Try opening the file and reading the data
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
    except IOError as e:
        # Log the error
        logging.error(f'Error reading data from {file_path}: {e}')
        return
    
    try:
        # Try processing the data
        num_rows = len(data)
        num_columns = len(data[0])
        logging.info(f'Number of rows: {num_rows}')
        logging.info(f'Number of columns: {num_columns}')

        # Write the processed data to the output file
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(f'Number of rows: {num_rows}\n')
            output_file.write(f'Number of columns: {num_columns}\n')
        logging.info(f'Processed data written to {output_path}')

    except IOError as e:
        # Log the error
        logging.error(f'Error processing data: {e}')
        return


########################################################################################
# EXCEL #
########################################################################################

# Write data to an excel file

def write_excel_data(folder_name, filename, data):
    '''Write data to an excel file.'''
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        # Try opening the file and writing the data
        data.to_excel(file_path)
        logging.info(f'Data written to {file_path}') # Log the success
    except IOError as e:
        # Log the error
        logging.error(f'Error writing data to {file_path}: {e}')

# Fetch data from url and write to an excel file

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        write_excel_data(folder_name, filename, response.text)
        return response.text
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None
    
# Process excel data: count rows and columns and save to file. 

def process_excel_data(folder_name, input_filename, output_filename):
    '''Process excel data.'''
    # Read the data from the input file
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    
    try:
        # Try opening the file and reading the data
        df = pd.read_excel(file_path)
        # Try processing the data with basic analysis
        num_rows = len(df)
        num_columns = len(df.columns)
        logging.info(f'Number of rows: {num_rows}')
        logging.info(f'Number of columns: {num_columns}')

        # Write the processed data to the output file
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(f'Number of rows: {num_rows}\n')
            output_file.write(f'Number of columns: {num_columns}\n')
        logging.info(f'Processed data written to {output_path}')

    except IOError as e:
        # Log the error
        logging.error(f'Error processing data: {e}')
        return

########################################################################################
# JSON #
########################################################################################

# Define function to write data to a JSON file
def write_json_data(folder_name, filename, data):
    '''Write data to a JSON file.'''
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        # Try opening the file and writing the data
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        logging.info(f'Data written to {file_path}') # Log the success
    
    except IOError as e:
        # Log the error
        logging.error(f'Error writing data to {file_path}: {e}')

# Fetch data from url and write to a JSON file
def fetch_and_write_json_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for errors
        if response.headers['Content-Type'] == 'application/json':
            json_data = response.json()
            write_json_data(folder_name, filename, data)
            return json_data
        else:
            logging.error(f'Error: Content type is not JSON')
            return None
    
    except requests.RequestException as e:
        logging.error(f'Error fetching JSON data from {url}: {e}')


# Process JSON data: extract and analyze data and save to file.
def process_json_data(folder_name, input_filename, output_filename):
    '''Process JSON data.'''
    # Read the data from the input file
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    
    try:
        # Try opening the file and reading the data
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
    except IOError as e:
        # Log the error
        logging.error(f'Error reading data from {file_path}: {e}')
        return
    
    try:
        # Try processing the data
        # For example, extract and analyze data
        # Here, we extract and analyze the data from a JSON file
        # and save the results to an output file
        # Extract data from JSON
        data = json_data['data']
        values = [item['value'] for item in data]
        # Analyze data
        mean_value = np.mean(values)
        max_value = np.max(values)
        min_value = np.min(values)
        # Save the results to the output file
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(f'Mean value: {mean_value}\n')
            output_file.write(f'Max value: {max_value}\n')
            output_file.write(f'Min value: {min_value}\n')
        logging.info(f'Processed data written to {output_path}')

    except IOError as e:
        # Log the error
        logging.error(f'Error processing data: {e}')
        return

########################################################################################
# Main function #
########################################################################################

def main():
    
    # print byline from imported module
    print(utils.byline)

    # URLs to fetch datasets from, and nba_api to fetch JSON data
    datasets = {
        'kanye_lyrics_txt': ('txt', 'https://www.kaggle.com/datasets/paultimothymooney/poetry?select=Kanye_West.txt'),
        'climate_change_csv': ('csv', 'https://www.kaggle.com/datasets/waqi786/climate-change-impact-on-agriculture/data'),
        'world_cup_excel': ('excel', 'https://www.kaggle.com/datasets/rhugvedbhojane/fifa-world-cup-2022-players-statistics?select=FIFA+WC+2022+Players+Stats+.xlsx'),
        'nba_json': ('json', playercareerstats.PlayerCareerStats(player_id=203999).get_json())
    }

    # Folder names for storing data
    folder_names = {
        'txt': 'txt_data',
        'csv': 'csv_data',
        'excel': 'excel_data',
        'json': 'json_data'
    }

    # File names for data
    filenames = {
        'kanye_lyrics_txt': 'kanye_lyrics.txt',
        'climate_change_csv': 'climate_change.csv',
        'world_cup_excel': 'world_cup.xlsx',
        'nba_json': 'nba.json'
    }

    # Processed datasets based on type
    for dataset, (data_type, url) in datasets.items():
        folder_name = folder_names[data_type]
        filename = filenames[dataset]
        if data_type == 'txt':
            fetch_and_write_txt_data(folder_name, filename, url)
            process_txt_data(folder_name, filename, f'processed_{filename}')
        elif data_type == 'csv':
            fetch_and_write_csv_data(folder_name, filename, url)
            process_csv_data(folder_name, filename, f'processed_{filename}')
        elif data_type == 'excel':
            fetch_and_write_excel_data(folder_name, filename, url)
            process_excel_data(folder_name, filename, f'processed_{filename}')
        elif data_type == 'json':
            fetch_and_write_json_data(folder_name, filename, url)
            process_json_data(folder_name, filename, f'processed_{filename}')

if __name__ == '__main__':
    main()