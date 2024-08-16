# -*- coding: utf-8 -*-
"""GOMYCODE CHECKPOINT 17 [ydata-profiling].ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oqmCZRCg-bdj-0lByrFuIpmGlqJvX-dA

Checkpoint Objective:
In this checkpoint, we are going to work on
'Education Attainment And Enrolment Around The World' dataset, provided by the World bank group.

Dataset description : The dataset was derived from the original copy, which was published on the
world bank website. The primary purpose of this database is to document and analyse patterns of
educational attainment rates in different country around the world.

➡️ Dataset link :https://drive.google.com/file/d/1v4qPmCg2AGHgUmpc-n4J5e2M8zur7t5N/view

Columns description :
Age[15-49]All_gradeX : Percentage of the entire population ages 15 to 49 that has completed grade X
Age[15-49]Male_gradeX : Percentage of the male population ages 15 to 49 that has completed grade X
Age[15-49]Female_gradeX : Percentage of the female population ages 15 to 49 that has completed grade X
X = [1...3]
Instructions
Step 1: Data exploration with Pandas
Download the provided dataset
Use pandas to read the file into a pandas Dataframe.
Display general information about the dataset.
Run descriptive analysis on the dataset using the 'describe' function.

Step 2: Data exploration with ydata-profiling
Use ydata-profiling to generate a report of the provided dataset.
Look for missing values in the dataset. You can use the report generated by ydata to identify missing values.
Examine the correlations between different columns in the dataset. You can use the report generated by ydata
to identify correlations.
Identify any other interesting patterns or insights in the dataset that you can discover through the ydata-profiling
report.
Step 3: Summary
Write a summary of your findings based on the ydata-profiling report. Be sure to include any interesting patterns or
insights
you discovered in the dataset.
"""

!pip install ydata_profiling

!pip uninstall tensorflow

# Installation and importation of libraries
import pandas as pd
from ydata_profiling import ProfileReport

# MOUNT DRIVE
from google.colab import drive
drive.mount('/content/drive')

# Read in the data
csv_filepath = "/content/drive/MyDrive/Colab Notebooks/DATASETS/EDUCATION_ATTAINMENT.csv"
df = pd.read_csv(csv_filepath)  # Use pandas to read the file into a pandas DataFrame

"""DATA EXPLORATION WITH PANDAS

SOLUTION:

I installed and imported the neccessary libraries

I loaded the provided dataset into a pandas dataframe

I used pandas to explore the dataset.

I looked for missing values in the dataset.

I used pandas to calculate some summary statistics for the dataset.

"""

# DATA EXPLORATION
#df.head() # to display the first five rows of the dataset
#df.tail() # to display the last five rows of the dataset
#df.describe() # to display a statistical summary of the numeric columns
#df.info() # this function displays the totals rows and columns and from here i can identify the missing rows
df.columns[df.isna().any()].tolist() # this will display a list of columns with missing values
#df.isna().sum() # this will display the sum of the missing rows for each columns

# Pick the first five columns of the dataset
Five_columns = df[['Ages[15-49]_All_grade1', 'Ages[15-49]_All_grade2', 'Ages[15-49]_All_grade3', 'Ages[20-29]_All_grade1', 'Ages[20-29]_All_grade2']]# Pick 20 random columns using the sample method in pandas

# Pick 20 random columns using the sample method in pandas
sample_20 = Five_columns.sample(20)

# Use the ProfileReport method of ydata_profile to profile your data
profile = ProfileReport(sample_20, title = "Random Twenty data points") # Generate the profile report for the sliced data

# View your profile and submit your checkpoint
profile

"""SUMMARY
1. From the profile report generated using the sample, there are no missing values in the dataset
2. There is a strong correlation between the five sliced columns
3. All colomns contain unique values
4. The dataset took a very long time to import, so i used a sample of 5 columns and 20 rows'''
"""

