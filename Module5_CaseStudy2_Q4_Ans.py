# 4.Which are the top 5 common job in Year 2014 and how much do they cost SFO ?
import pandas as pd
df=pd.read_csv(r'c:\\temp\\Salaries.csv')
temp_df=df.loc[:,['Year','JobTitle','TotalPayBenefits']]
selected_data=temp_df[temp_df['Year']==2014]
print selected_data.groupby('JobTitle')['TotalPayBenefits'].nlargest(5)