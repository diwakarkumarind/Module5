# Find the genre in which there has been the greatest number of movie releases

import pandas as pd
import numpy as np

dataset=pd.read_csv('c:\\temp\\HollywoodMovies.csv')
selected_data=dataset.loc[:,['WorldGross','Genre']]
df=pd.DataFrame(selected_data)
df_notnull_genre=df[df.Genre.notnull()]
df_notnull_worldgross=df_notnull_genre[df_notnull_genre.WorldGross.notnull()]
df_final= df_notnull_worldgross
Series_genre = df_final['WorldGross'].groupby(df_final['Genre']).sum()
df_new=pd.DataFrame(Series_genre)
genre=df_new.sort_values(by='WorldGross', ascending=False).head(10)  #finding top 10 genre movies released
print genre
