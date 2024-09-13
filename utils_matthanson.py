''' ITERATION 1

Module: Hanson Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:

We don't write code from top to bottom; instead, we often write it from the outside in.
Here's what a first draft of my utils_case.py might look like:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
   
2. I'll declare a global variable for my byline string and just set it to some simple text.

3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.

4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it in an online interpreter to ensure this version runs correctly before continuing.

Note that much of this code was based off starter code provided by the instructor of my course, but will gradually evolve and take shape according to my own modifications as we move forward through this seven week course. 
'''

# Import statistics to use for mean, mode, median and stdev
import statistics

#####################################
# Declare a global variables, ending with a blank f-string named byline.
#####################################

# Boolean for whether company has international clients
has_international_clients: bool = True

# Integer for number of years in operation
years_operating: int = 12

# List of strings representing different services and capabilities offered by company
skills_offered: list = ['Data analytics', 'Machine learning', 'Content creation', 'Data visualizations']

# List of floats for client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 3.2, 2.8, 5.0]

# List of floats for estimated values added to clients
valueadded_scores = [4.2, 4.5, 5.0, 2.1, 2.8]

###########################################################
# Calculate statistics BEFORE declaring byline variable
###########################################################

# Calculate basic stats
min_satisfaction_score: float = min(client_satisfaction_scores)
max_satisfaction_score: float = max(client_satisfaction_scores)
mean_satisfaction_score: float = statistics.mean(client_satisfaction_scores)
stdev_satisfaction_score: float = statistics.stdev(client_satisfaction_scores)

min_value_score: float = min(valueadded_scores)
max_value_score: float = max(valueadded_scores)
mean_value_score: float = statistics.mean(valueadded_scores)
stdev_value_score: float = statistics.stdev(valueadded_scores)

byline: str = f"""
------------------------------------------------------
   Hanson Analytics: Delivering Actionable Insights
------------------------------------------------------
Has international clients: {has_international_clients}
Years in business: {years_operating}
Skills offered: {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Value Added Scores: {valueadded_scores}
Min Satisfaction Score: {min_satisfaction_score}
Max Satisfaction Score: {max_satisfaction_score}
Mean Satisfaction Score: {mean_satisfaction_score}
Satisfaction Score Standard Deviation: {stdev_satisfaction_score}
Min Value Added Score: {min_value_score}
Max Value Added Score: {max_value_score}
Mean Value Added Score: {mean_value_score}
Value Added Score Standard Deviation: {stdev_value_score}
"""

#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

#####################################
# Create a function to getbyline as a string.
#####################################

def getbyline() -> str:
   '''Return byline variable.'''
   return byline

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(getbyline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
