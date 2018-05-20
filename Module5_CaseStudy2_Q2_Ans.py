# 2.Which Job Title in Year 2014 has highest mean salary?
import pandas as pd
df=pd.read_csv(r'c:\\temp\\Salaries.csv')
selected_data=df.loc[:,['JobTitle','Year','TotalPay']]
print selected_data.max()