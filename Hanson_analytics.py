
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

# Define function to write data to an excel file

########################################################################################
# JSON #
########################################################################################

# Define function to write data to a JSON file


# Process and analyze data