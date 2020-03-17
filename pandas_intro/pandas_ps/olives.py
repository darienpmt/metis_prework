# q1
import pandas as pd # importe the required modules
import numpy as np

# q2
pd.options.display.max_rows = 30 # set max rows displayed to be 30
pd.options.display.max_columns = None # set no limit for max columns
pd.set_option('precision', 3) # set precision to 3

# q3
pd_version = '0.25.3' # verion of pandas and numpy
np_version = '1.18.1'

# q4
df = pd.read_csv('olive.csv') # read in the csv file and save it under the variable name 'df'

# q5
df_shape = df.shape # returns a tuple representing the number rows and then the number of columns in the df

# q6
df_first_two = df[:2] # assign variable 'df_first_two' to the first two rows of the df

# q7
df_data_types_count = len(df.dtypes.value_counts()) # assigne variable df_data_types_count to a series of the data types in each column in df
print(df_data_types_count)
# q8
df['sub_region_raw'] = df['Unnamed: 0'] # copying the 'Unnamed: 0' column (the first column in the df) and naming it 'sub_region_raw'

# q9
df.rename(columns={'Unnamed: 0': 'sub_region_desc'}, inplace=True) # renaming col 'Unnamed: 0' to 'sub_region_desc'

# q10
df.rename(columns={'area': 'sub_region'}, inplace=True) # renaming col 'area' to 'sub_region'

# q11
region_unique = df.region.unique() # assigning 'region_unique' to an array containing the unique values in the column 'region'

# q12
sub_region_unique_count = len(df.sub_region.unique())

print(df['sub_region_desc'].head())
# q13 
#df['sub_region_desc'] = df['sub_region_desc'].str.split('.').apply(lambda lst: lst[-1])
df['sub_region_desc'] = df['sub_region_desc'].replace('\d+\.','',regex=True)
srd_unique = df['sub_region_desc'].unique()

print(srd_unique)
