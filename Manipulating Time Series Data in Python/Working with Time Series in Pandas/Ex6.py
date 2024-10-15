'''
Calculating stock price changes
'''

# Create 'shifted_30' column by shifting the 'price' column down by 30 days
yahoo['shifted_30'] = yahoo['price'].shift(30)

# Calculate 'change_30' as the difference between the current 'price' and 'shifted_30'
yahoo['change_30'] = yahoo['price'].sub(yahoo['shifted_30'])

# Calculate 'diff_30' as the 30-day difference of 'price'
yahoo['diff_30'] = yahoo['price'].diff(periods=30)

# Inspect the last five rows of 'price' to see recent values
print(yahoo['price'].tail(5))

# Compute the difference between 'change_30' and 'diff_30'
# Then use 'value_counts()' to see the frequency of each difference
difference_counts = yahoo['change_30'].sub(yahoo['diff_30']).value_counts()
print(difference_counts)
