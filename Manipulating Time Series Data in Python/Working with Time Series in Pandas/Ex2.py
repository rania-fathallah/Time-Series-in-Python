'''
Create a time series of air quality data
'''

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file 'nyc.csv' into a DataFrame named 'data'
data = pd.read_csv('nyc.csv')

# Inspect the structure and data types of the DataFrame
print(data.info())

# Convert the 'date' column to datetime64 format for proper date handling
data['date'] = pd.to_datetime(data['date'])

# Set the 'date' column as the index of the DataFrame for time series analysis
data.set_index('date', inplace=True)

# Inspect the structure and data types of the DataFrame again to confirm changes
print(data.info())

# Plot the data, creating subplots for each column with legends
data.plot(subplots=True, legend=True)
plt.show()

