# 1.Compute how much total salary cost has increased from year 2011 to 2014
import pandas as pd
df=pd.read_csv(r'c:\\temp\\Salaries.csv')
selected_data=df.loc[:,['Year','TotalPay']]
print selected_data.groupby('Year').mean()
