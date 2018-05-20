# 2.Which Job Title in Year 2014 has highest mean salary?
import pandas as pd
df=pd.read_csv(r'c:\\temp\\Salaries.csv')
print df.groupby('Year').mean()
print df.groupby('JobTitle').max()