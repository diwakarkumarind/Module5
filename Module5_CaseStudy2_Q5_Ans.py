#5.Who was the top earning employee across all the years?
import pandas as pd
df=pd.read_csv(r'c:\\temp\\Salaries.csv')
selected_data=df.loc[:,['EmployeeName','Year','TotalPayBenefits']]
print selected_data.nlargest(5,'TotalPayBenefits')