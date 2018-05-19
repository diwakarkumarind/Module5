# Ans 5
import numpy as np
import pandas as pd

file_path='c:\\temp\\example.csv'

# 5.1: From the raw data below create a data frame
dataset={'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
'age': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, ".", "."],
'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df=pd.DataFrame(dataset)

# 5.2: Save the dataframe into a csv file as example.csv
df.to_csv(file_path,sep=',')

# 5.3: Read the example.csv and print the data frame
dataset2=pd.read_csv(file_path)
df2=pd.DataFrame(dataset2)
# print df2

# 5.4: Read the example.csv without column heading
dataset3=pd.read_csv(file_path, header=None)
df3=pd.DataFrame(dataset3)
# print df3

# 5.5 Read the example.csv and make the index columns as First Name and Last Name
dataset4=pd.read_csv(file_path,usecols=[2,3])
df4=pd.DataFrame(dataset4)
# print df4

# 5.6:  Print  the  data  frame  in  a  Boolean  form  as  True  or  False.  True  for  Null/  NaN values and false for non-null values
dataset5=pd.read_csv(file_path)
df5=pd.DataFrame(dataset5)
# print df5.isnull()

# 5.7: Read the dataframe by skipping first 3 rows and print the data frame
dataset6=pd.read_csv(file_path, skiprows=3)
df6=pd.DataFrame(dataset6)
# print df6

# 5.8: Load a csv file while interpreting , in strings around numbers as thousands seperators.
# Check the raw data postTestScore column has, as thousands separator.
data=pd.read_csv(file_path, index_col=4).filter(regex='\d{4}')


