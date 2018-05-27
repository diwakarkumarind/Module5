# Print the names of the top five movies with the costliest budgets
import pandas as pd
import numpy as np
dataset=pd.read_csv('c:\\temp\\HollywoodMovies.csv')
selected_data=dataset.loc[:,['Movie','Budget']]
df_raw=pd.DataFrame(selected_data)
df=df_raw[df_raw.Budget.notnull()]
df2=df.sort_values(by='Budget', ascending=False).head(5)
print df2
