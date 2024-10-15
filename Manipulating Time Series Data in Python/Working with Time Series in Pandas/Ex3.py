'''
Compare annual stock price trends
'''

# Create an empty DataFrame called prices
prices = pd.DataFrame()

# Select data for each year and concatenate it with the prices DataFrame
for year in ['2013', '2014', '2015']:
    # Select the price data for the current year
    # Using .loc to filter by year and selecting the 'price' column
    price_per_year = yahoo.loc[year, ['price']].reset_index(drop=True)
    
    # Rename the 'price' column to the current year for clarity
    price_per_year.rename(columns={'price': year}, inplace=True)
    
    # Concatenate the current year's data with the existing prices DataFrame along axis=1 (columns)
    prices = pd.concat([prices, price_per_year], axis=1)

# Plot the prices DataFrame
prices.plot(subplots=True, legend=True)
plt.title('Yearly Prices from 2013 to 2015')
plt.xlabel('Index')
plt.ylabel('Price')
plt.show()

