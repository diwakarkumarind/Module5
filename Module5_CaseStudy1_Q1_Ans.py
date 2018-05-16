# Find the highest rated movie in the Quest story type.

import numpy as np
import pandas as pd

dataset=pd.read_csv('c:\\temp\\HollywoodMovies.csv')
selected_data=dataset.loc[:,['Movie','Story','RottenTomatoes']]
df=pd.DataFrame(selected_data)
df_movie_filter = df[(df.Story == 'Quest') & (df.Story.notnull())]
output = df_movie_filter[df_movie_filter.RottenTomatoes == max(df_movie_filter.RottenTomatoes)]
print output
