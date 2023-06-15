import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='b', label='Original Data')

    # Create first line of best fit
    slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    plt.plot(data['Year'], intercept_all + slope_all * data['Year'], 'r', label='Line of Best Fit (All Data)')

    # Create second line of best fit
    data_since_2000 = data[data['Year'] >= 2000]
    slope_since_2000, intercept_since_2000, r_value_since_2000, p_value_since_2000, std_err_since_2000 = linregress(data_since_2000['Year'], data_since_2000['CSIRO Adjusted Sea Level'])
    plt.plot(data_since_2000['Year'], intercept_since_2000 + slope_since_2000 * data_since_2000['Year'], 'g', label='Line of Best Fit (Since 2000)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
