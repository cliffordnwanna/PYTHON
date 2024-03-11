# Data Preproessing.py

#SOLUTION
#Load the dataset, display the ten first lines, store the results in a variable called 'client_0_bills'
import pandas as pd
csv_path = r"C:\Users\HP\Downloads\STEG_BILLING_HISTORY.csv"
df = pd.read_csv(csv_path)
client_0_bills = df.head(10)
client_0_bills

#What is the data type of the 'client_0_bills' variable ?
type(client_0_bills)


#Display the general information of the dataset and try to answer the following questions :
df.info()

# How many rows and columns do we have in this dataset ?
# 4476748 rows and 16 columns
# How many categorical features are present in the dataset ?
# 4
# How much memory space does the dataset consume ?
# memory usage: 546.5+ MB

#Inspect the dataset for potential missing values
columns_with_missing_values = df.columns[df.isna().any()].tolist()
columns_with_missing_values
df.isnull().sum()

# Select your strategy to handle missing values, and tell us why you had made that choice.
columns_with_missing_values = ['counter_number', 'reading_remarque']
"""To handle missing values in:
    'counter_number', replace missing values with the median: This method is useful because the column's datatype is numerical
    and has outliers.
    'reading_remarque', Replace missing values with the mean: This method is useful because the column's datatype is numerical"""

#Run a descriptive analysis on numeric features (columns)
df.describe

#Select the bills records for the client with an id ='train_Client_0', using 2 methods.
df.loc[df['client_id'] == 'train_Client_0']
df.iloc[0:33]

#Transform the 'counter_type' feature to a numeric variable using the encoder of your choice.
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder() # Initialize the LabelEncoder
# Fit the encoder on the data and transform the 'Category' column
df['counter_type'] = encoder.fit_transform(df['counter_type'])
df.head()

#Delete the 'counter_statue' feature from the Dataframe
df = df.drop('counter_statue', axis=1)
df.head()

