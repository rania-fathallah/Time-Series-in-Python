'''
Your first time series
'''

# Import necessary libraries
import pandas as pd

# Create a range of dates for the first week of 2017
seven_days = pd.date_range(start='2017-1-1', periods=7)

# Iterate over the dates in the range and print the number and name of the weekday
for day in seven_days:
    # day.dayofweek returns the day of the week as an integer (Monday=0, Sunday=6)
    # day.day_name() returns the name of the day as a string
    print(day.dayofweek, day.day_name())
