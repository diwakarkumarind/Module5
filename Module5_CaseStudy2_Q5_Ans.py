# 5.Who was the top earning employee across all the years?
import pandas as pd
df=pd.read_csv(r'c:\\temp\\Salaries.csv')
temp_df=df.loc[:,['Year','JobTitle','TotalPayBenefits']]
selected_data=temp_df[temp_df['Year']==2014]
print selected_data.groupby('JobTitle')['TotalPayBenefits'].nlargest(5)