'''
Plotting multi-period returns
'''

# Create 'daily_return' as the daily percentage change in 'Close', expressed as a percentage
google['daily_return'] = google['Close'].pct_change(1).mul(100)

# Create 'monthly_return' as the percentage change over a 30-day period in 'Close', expressed as a percentage
google['monthly_return'] = google['Close'].pct_change(30).mul(100)

# Create 'annual_return' as the percentage change over a 360-day period in 'Close', expressed as a percentage
google['annual_return'] = google['Close'].pct_change(360).mul(100)

# Plot the result with each time series as a subplot and legends enabled
google.plot(subplots=True, legend=True)
plt.show()
