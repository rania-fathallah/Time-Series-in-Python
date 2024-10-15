'''
Set and change time series frequency
'''

# Inspect the structure and data types of the DataFrame 'co'
print(co.info())

# Set the frequency of the DataFrame to daily (calendar daily)
co = co.asfreq('D')

# Plot the data with separate subplots for each column
co.plot(subplots=True, legend=True)
plt.title('Daily Data Plot')
plt.xlabel('Date')
plt.ylabel('Values')
plt.show()

# Set the frequency of the DataFrame to monthly
co = co.asfreq('M')

# Plot the data again with the new monthly frequency
co.plot(subplots=True, legend=True)
plt.title('Monthly Data Plot')
plt.xlabel('Date')
plt.ylabel('Values')
plt.show()

