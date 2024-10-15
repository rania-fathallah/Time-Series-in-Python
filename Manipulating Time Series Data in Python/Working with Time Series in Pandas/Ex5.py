'''
Shifting stock prices across time
'''

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the Google stock data from 'google.csv'
# Parse 'Date' as datetime and set it as the index
google = pd.read_csv('google.csv', parse_dates=['Date'], index_col='Date')

# Set the data frequency to business daily
# This means we will only consider business days (weekdays) in the dataset
google = google.asfreq('B')

# Create a lagged version of the 'Close' column
# This shifts the 'Close' prices up by 90 days (future prices)
google['lagged'] = google['Close'].shift(-90)

# Create a shifted version of the 'Close' column
# This shifts the 'Close' prices down by 90 days (past prices)
google['shifted'] = google['Close'].shift(90)

# Plot the Google price series along with the lagged and shifted columns
google.plot(subplots=True, legend=True)
plt.suptitle('Google Stock Prices with Lagged and Shifted Values', fontsize=16)  # Title for the entire figure
plt.xlabel('Date')  # Label for the x-axis
plt.ylabel('Price')  # Label for the y-axis
plt.show()  # Display the plots

