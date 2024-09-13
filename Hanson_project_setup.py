'''This module provides functions for creating a series of project folders and files for a new analytics project.'''

# Import necessary libraries
# TODO: Import additional modules as needed. 
import pathlib
import time

# Import local modules
# TODO: Import your module here.
import utils_matthanson as uh

########################################################################################
# Declare global variables
########################################################################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

########################################################################################
# Define function 1: create_folders_for_range
# Parameters: start_year, end_year
# Returns: None
########################################################################################

def create_folders_for_range(start_year, end_year):
    '''Create folders for a range of years.'''
    for year in range(start_year, end_year + 1):
        year_path = data_path.joinpath(str(year))
        year_path.mkdir(exist_ok=True)
    # Log the function call and its arguments
        print(f'FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}')

#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list):
    '''Create folders from a list of names.'''
    for folder in folder_list:
        folder_path = data_path.joinpath(str(folder))
        folder_path.mkdir(exist_ok=True)

    # Log the function call and its arguments
        print(f"FUNCTION CALLED: create_folders_from_list with '{folder_list}'")

#####################################
# Define Function 3: create_prefixed_folders
# Pass in a list of folder names and a prefix, add prefix to each folder name
#####################################

folder_id = ['csv', 'excel', 'json']
prefix = 'format-'
def create_prefixed_folders(folder_list: list, prefix: str):
    
    '''Create folders with a prefix using a list of names.'''
    for folder in folder_list:
        folder_path = data_path.joinpath(str(prefix + folder))
        folder_path.mkdir(exist_ok=True)

    # Log the function call and its arguments
        print(f"FUNCTION CALLED: create_prefixed_folders with '{folder_list}' and prefix '{prefix}'")

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
   folder_count = 0
   num_folders = 5
   
   while folder_count < num_folders:
       
       # Define the folder path
       folder_path = project_path.joinpath(f"folder_{folder_count}")
       
       # Create the folder if it doesn't exist
       folder_path.mkdir(exist_ok=True)
       
       # Print a message indicating folder was created
       print(f"FUNCTION CALLED: create_folders_periodically - duration_seconds={duration_seconds}")

       # Wait for the specified duration
       time.sleep(duration_seconds)

       # Increment the folder count
       folder_count += 1

       if folder_count == num_folders:
           break


       
    
#####################################
# Define a main function for this module.
#####################################

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {uh.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_list= ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_list)

    # Call function 3 to create folders using comprehension
    folder_list = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_list, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    num_folders = 5  # number of folders to create
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions)

if __name__ == '__main__':
    main()