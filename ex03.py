import pandas as pd

"""
GENERAL INSTRUCTIONS:

Complete the implementations of the functions so that the functions 
work as described. Do not change the names (of the functions or this
file) or the parameterization in any way. Submit the completed ex03.py
to the respective assignment submission area in Moodle. 

Clean up any unnecessary code from the version to be submitted.
You can use helper functions, but remove the calls to the functions
requested to be implemented. Also make sure that any data not 
specifically requested to be printed by the instructions is not 
printed on the console. (Do not worry, the functions will be 
called during the evaluation. However, if there are extra prints 
or calls with some other than the actual test data, that makes 
the test process unnecessarily confusing.)

You can assume that the pandas library is available. 
(Install that for yourself, possibly in a virtual 
environment (pip install pandas).) No other assumptions should be 
made about the availability of external libraries not included in 
the standard Python distribution.
"""


"""
Function merge_stuff (max 1 XP)
-------------------------------

The function

¤ reads the data from the files data1.csv and data2.csv*,
located in the directory where the code file is located 
and from which the code is run, into pandas data frames 
(one DataFrame for each file),

¤ creates a new data frame that combines data from the original
data frames based on the values in the time and location columns,
so that rows with matching values in these columns are considered
to correspond to each other for the other columns as well**,

¤ sorts the data so that the primary sorting criterion is the 
value of the temperature_C column and the secondary criterion 
is the value of the air_pressure_hPa column (in ascending order),
and the order of the columns from left to right is time, location,
CO2_ppm, temperature_C, air_pressure_hPa, humidity_rel_perc,

¤ removes all the data rows missing a value for humidity_rel_perc,

¤ writes the resulting data to a CSV file named output.csv, 
including the column header row, in the same directory, and

¤ returns the arithmetic mean of the CO2_ppm values for the
result data.

The file output.csv should not contain any columns other than 
those listed. (For example, there should not be a row index 
column created by pandas.)

*) When coding, you can use the files data1.csv and data2.csv 
found on Moodle. These files illustrate the structure of the 
files to be used for testing.

**) In the new data frame, the number of data rows does not 
increase, but it will have more columns than either of the 
original data frames. There should, however, be only one time 
column and one location column in the combined structure;
duplicate columns are not allowed.
"""

def merge_stuff() -> float:
    # read csvs
    df1 = pd.read_csv('./data1.csv')
    df2 = pd.read_csv('./data2.csv')

    # new dataframe
    df = pd.merge(df1, df2, on=['time', 'location'])
    df = df[['time', 'location','CO2_ppm', 'temperature_C', 'air_pressure_hPa', 'humidity_rel_perc']]

    # drop row for NAN
    df = df.dropna(subset=['humidity_rel_perc'])

    # sort
    df = df.sort_values(by=['temperature_C', 'air_pressure_hPa'], ascending=[True, True])

    # humidity_rel_perc convert
    df['humidity_rel_perc'] = df['humidity_rel_perc'].astype(int)

    # generate output.csv
    df.to_csv('output.csv', index=False)

    # arithmetic mean
    return df['CO2_ppm'].mean()