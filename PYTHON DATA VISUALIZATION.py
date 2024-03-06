
#IMPORT LIBRARIES
#SOLUTION
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# MOUNT DRIVE
from google.colab import drive
drive.mount('/content/drive')

# LOAD THE DATASET
df = pd.read_csv('/content/drive/MyDrive/Untitled folder/Africa_climate_change.csv')

# DATA EXPLORATION
df.head() # to display the first five rows of the dataset
#df.tail() # to display the last five rows of the dataset
#df.describe() # to display a statistical summary of the numeric columns
#df.info() # this function displays the totals rows and columns and from here i can identify the missing rows
#df.columns[df.isna().any()].tolist() # this will display a list of columns with missing values
#df.isna().sum() # this will display the sum of the missing rows for each columns

# DATA CLEANING
"""Replacing missing values with the mean: Mean is the average value of a column. This method is useful when
the data is normally distributed or nearly normally distributed and there are no extreme outliers in the data
that could heavily skew the mean."""

df['PRCP'].fillna(df['PRCP'].mean(), inplace=True)# Replace missing values with mean
df['TAVG'].fillna(df['TAVG'].mean(), inplace=True)# Replace missing values with mean
df['TMAX'].fillna(df['TMAX'].mean(), inplace=True)# Replace missing values with mean
df['TMIN'].fillna(df['TMIN'].mean(), inplace=True)# Replace missing values with mean
df.isnull().sum() # this will display the sum of the missing rows for each columns

# DATA WRANGLING
"""I observed that the 'DATE' column contains not only the date in 'YYYYMMDD' format but also time information
('HH:MM:SS'). To remove the time information and keep only the date part, you can use the .str accessor in
combination with string slicing."""
# Remove the time information and keep only the date part
#df['DATE'] = df['DATE'].str[:8]

# Convert the 'DATE' column to a numerical data type (integer)
#df['DATE'] = df['DATE'].astype(int)


# Convert the date column to a proper date format
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y%m%d')

# (2)Plot a line chart to show the average temperature fluctuations in Tunisia and Cameroon. Interpret the results

# Filter the "COUNTRY" column in the dataset and slice out rows where "COUNTRY"= Tunisia and Cameroon.
Tunisia_Cameroon_DF = df[(df['COUNTRY'].isin(['Tunisia', 'Cameroon']))]
# Create a line chart
fig = px.line(Tunisia_Cameroon_DF, x='TAVG', y='COUNTRY', color='COUNTRY', title='Average Temperature Fluctuations in Tunisia and Cameroon (1980-2023)')
# Show the chart
fig.show()

"""Result interpretation for the Average Temperature Fluctuations in Tunisia and Cameroon (1980-2023)
average temperature = [(maximum temperature + minimum temperature) / 2]degrees

average temperature [Tunisia] = [(-49 + 105) /2 ] = 28 degrees

average temperature [Cameroon] = [(50 + 108) /2 ] = 79 degrees

"""

#(3) Zoom in to only include data between 1980 and 2005, try to customize the axes labels.

# Filter the data for Tunisia and Cameroon based on a datetime range
Tunisia_Cameroon_DF_1980_2005 = Tunisia_Cameroon_DF[(Tunisia_Cameroon_DF['DATE'] >= '1980-01-01') & (Tunisia_Cameroon_DF['DATE'] <= '2005-12-31')]
## Create a line chart
fig = px.line(Tunisia_Cameroon_DF_1980_2005, x='DATE', y='TAVG', color='COUNTRY', title='Average Temperature Fluctuations in Tunisia and Cameroon (1980-2005)')
# Customize the axes labels
fig.update_xaxes(title_text='Year [1980 - 2005]')
fig.update_yaxes(title_text='Average Temperature (°C)')

# Show the chart
fig.show()

#Create Histograms to show temperature distribution in Senegal between [1980,2000] and [2000,2023] (in the same figure).
#Describe the obtained results.
# Filter the data for Senegal and the specified years
senegal_1980_2000 = df[(df['COUNTRY'] == 'Senegal') & (df['DATE'] >= '1980-01-01') & (df['DATE'] <= '2000-12-31')]
senegal_2000_2023 = df[(df['COUNTRY'] == 'Senegal') & (df['DATE'] >= '2000-01-01') & (df['DATE'] <= '2023-12-31')]

# Create histograms
plt.figure(figsize=(10, 5)) #This line creates a new Matplotlib figure with a specified figure size of 10 units in width and 5 units in height. The figure function initializes a new plotting area.

plt.subplot(1, 2, 1) #This line creates the first subplot within the figure. The parameters (1, 2, 1) indicate that the figure is divided into one row and two columns of subplots, and this subplot is the first one.
plt.hist(senegal_1980_2000['TAVG'], bins=20, color='blue') #This line creates a histogram for the 'Average_Temperature' data in the senegal_1980_2000 DataFrame. It specifies the number of bins as 20, which controls
                                                          #how the data is divided into intervals. The 'color' parameter is set to 'blue' to color the bars in the histogram in blue.
plt.title('Temperature Distribution in Senegal (1980-2000)') #This line sets the title for the first subplot.
plt.xlabel('Average Temperature (°C)')#This line labels the x-axis of the first subplot.
plt.ylabel('Frequency') #This line labels the y-axis of the first subplot.

plt.subplot(1, 2, 2) # This line creates the second subplot within the same figure. The parameters (1, 2, 2) indicate that this subplot is the second one in the one row and two columns layout.
plt.hist(senegal_2000_2023['TAVG'], bins=20, color='green') #This line creates a histogram for the 'Average_Temperature' data in the senegal_1980_2000 DataFrame. It specifies the number of bins as 20, which controls
                                                          #how the data is divided into intervals. The 'color' parameter is set to 'blue' to color the bars in the histogram in blue.
plt.title('Temperature Distribution in Senegal (2000-2023)') #This line sets the title for the second subplot.
plt.xlabel('Average Temperature (°C)') #This line labels the x-axis of the second subplot.
plt.ylabel('Frequency') #This line labels the y-axis of the second subplot.

plt.tight_layout() # This line ensures that the subplots are properly spaced and do not overlap within the figure.
plt.show() #This line displays the entire figure, including both subplots. The resulting figure will have two side-by-side histograms,
            #each representing the temperature distribution in Senegal for a specific time period.

#(4) Select the best chart to show the Average temperature per country.
##The choice of the best chart depends on the specific goals and preferences,but a bar chart can be a good option to compare average temperatures across countries.


# Calculate the average temperature per country
avg_temp_per_country = df.groupby('COUNTRY')['TAVG'].mean().reset_index()

# Create a bar chart
fig = px.bar(avg_temp_per_country, x='COUNTRY', y='TAVG', title='Average Temperature per Country')

# Customize the axes labels
fig.update_xaxes(title_text='Country')
fig.update_yaxes(title_text='Average Temperature (°C)')

# Show the chart
fig.show()

