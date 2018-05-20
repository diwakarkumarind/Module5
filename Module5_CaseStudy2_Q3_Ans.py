# 3.How much money could have been saved in Year 2014 by stopping OverTimePay?
import pandas as pd
df=pd.read_csv(r'c:\\temp\\Salaries.csv')
selected_data=df.loc[:,['Year','OvertimePay']]
print selected_data.groupby('Year').sum()