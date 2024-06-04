import pandas as pd

# Tesla annual revenue data
annual_revenue_data = {
    'Year': ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009'],
    'Annual Revenue (Millions of US $)': [96773, 81462, 53823, 31536, 24578, 21461, 11759, 7000, 4046, 3198, 2013, 413, 204, 117, 112]
}

# Tesla quarterly revenue data
quarterly_revenue_data = {
    'Quarter': ['2024-03-31', '2023-12-31', '2023-09-30', '2023-06-30', '2023-03-31', '2022-12-31', '2022-09-30', '2022-06-30', '2022-03-31', '2021-12-31', '2021-09-30', '2021-06-30', '2021-03-31', '2020-12-31', '2020-09-30', '2020-06-30', '2020-03-31', '2019-12-31', '2019-09-30', '2019-06-30', '2019-03-31', '2018-12-31', '2018-09-30', '2018-06-30', '2018-03-31', '2017-12-31', '2017-09-30', '2017-06-30', '2017-03-31', '2016-12-31', '2016-09-30', '2016-06-30', '2016-03-31', '2015-12-31', '2015-09-30', '2015-06-30', '2015-03-31', '2014-12-31', '2014-09-30', '2014-06-30', '2014-03-31', '2013-12-31', '2013-09-30', '2013-06-30', '2013-03-31', '2012-12-31', '2012-09-30', '2012-06-30', '2012-03-31', '2011-12-31', '2011-09-30', '2011-06-30', '2011-03-31', '2010-12-31', '2010-09-30', '2010-06-30', '2010-03-31'],
    'Quarterly Revenue (Millions of US $)': [21301, 25167, 23350, 24927, 23329, 24318, 21454, 16934, 18756, 17719, 13757, 11958, 10389, 10744, 8771, 6036, 5985, 7384, 6303, 6350, 4541, 7226, 6824, 4002, 3409, 3288, 2985, 2790, 2696, 2285, 2298, 1270, 1147, 1214, 937, 955, 940, 957, 852, 769, 621, 615, 431, 405, 562, 306, 50, 27, 30, 39, 58, 58, 49, 36, 31, 28, 21]
}

# Create DataFrames
tesla_annual_revenue = pd.DataFrame(annual_revenue_data)
tesla_quarterly_revenue = pd.DataFrame(quarterly_revenue_data)

# Display the last five rows of the quarterly revenue DataFrame
print(tesla_quarterly_revenue.tail())

# Save a screenshot of the last five rows as an image
import matplotlib.pyplot as plt

# Create a simple plot to save as an image
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')
tbl = ax.table(cellText=tesla_quarterly_revenue.tail().values, colLabels=tesla_quarterly_revenue.columns, cellLoc='center', loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.2, 1.2)

# Save the table as an image
plt.savefig('tesla_quarterly_revenue_tail.png')
