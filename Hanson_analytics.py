
# Standard library imports
import pathlib 
import logging

# External library imports (requires virtual environment)
import requests
import pandas as pd
import matplotlib.pyplot as plt
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
    except Exception as e:
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

# Process text data

def process_txt_data(folder_name, input_filename, output_filename):
    '''Process text data.'''
    # Read the data from the input file
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    
    try:
        # Try opening the file and reading the data
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except Exception as e:
        # Log the error
        logging.error(f'Error reading data from {file_path}: {e}')
        return
    
    try:
        # Try processing the data
        # For example, count the number of words
        words = text.split()
        num_words = len(words)
        unique_words = set(words)
        logging.info(f'Number of words: {num_words}')
        logging.info(f'Number of unique words: {len(unique_words)}')
    except Exception as e:
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
    except Exception as e:
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
    except Exception as e:
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

########################################################################################
# JSON #
########################################################################################

# Define function to write data to a JSON file


# Process and analyze data