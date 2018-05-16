# Is there any correspondence between the critics evaluation of a movie and itsacceptance by the public?
# Find out, by plotting the net profitability of a movie against the ratings it receives on Rotten Tomatoes.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("c:\\temp\\HollywoodMovies.csv")
selected_data=dataset.loc[:,['Movie','RottenTomatoes','Profitability']]
df=pd.DataFrame(selected_data)
sorted_data=selected_data.sort_index(by=['RottenTomatoes'],ascending=False)
selected_sorted_data=sorted_data.iloc[:10]
fig1, ax1 = plt.subplots()
ax1.axis('equal')
plt.pie(selected_sorted_data['Profitability'],labels=selected_sorted_data['Movie'])
movies=list(selected_sorted_data['Movie'])
plt.legend(movies,loc=2)
plt.show()