# Ans 6
import pandas as pd
import numpy as np
# 6.1: From the raw data below create a Pandas Series
data='Amit', 'Bob', 'Kate', 'A', 'b', 'np.nan', 'Car', 'dog', 'cat'
s=pd.Series(data)
print 'Series elements in lower case',s.str.lower() #a) Print all elements in lower case
print 'Series elements in UPPER case',s.str.upper() #b) Print all the elements in upper case
for i in range(len(s)):                             #c) Print the length of all the elements
    print 'Length of',s[i],'=',len(s[i])

# 6.2: From the raw data below create a Pandas Series
data=' Atul', 'John ', ' jack ', 'Sam'
s=pd.Series(data)
# a) Print all elements after stripping spaces from the left and right
for i in range(len(s)):
    print s[i].strip()

# b) Print all the elements after removing spaces from the left only
for i in range(len(s)):
    print s[i].lstrip()

# c) Print all the elements after removing spaces from the right only
for i in range(len(s)):
    print s[i].rstrip()

# 6.3: Create a series from the raw data below
# a)split the individual strings wherever _comes and create a list out of it
data=['India_is_big', 'Population_is_huge', 'Has_diverse_culture']
output_data=[]
for i in range(len(data)):
    output_data.append(data[i].split('_'))

# b)Access the individual element of a list
# c)Expand the elements so that all individual elements get splitted by _ and insted of list returns individual elements
for i in range(len(output_data)):
    print output_data[i]

# 6.4: Create a series and replace either X or dog with XX-XX
data='A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'
s=pd.Series(data)
print s.str.replace('^.a|dog', 'XX-XX ', case=False)

# 6.5: Create a series and remove dollar from the numeric values
dollar='12', '-$10', '$10,000'
s_dollar=pd.Series(dollar)
print s_dollar.str.replace(r'$', '')

# Create a series and reverse all lower case words
pat=r'[a-z]+'
repl=lambda m: m.group(0)[::-1]
s=pd.Series(['india 1998', 'big country', np.nan]).str.replace(pat,repl)
print s

# 6.7: Create pandas series and print true if value is alphanumeric in series or false if value is not alphanumeric in series.
s=pd.Series([1, 2, '1a', '2b', '2003c'])
print s.str.isalnum()

# 6.8: Create pandas series and print true if value is containing A
s=pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])
print s.str.contains('A')

# 6.9: Create pandas series and print in three columns value 0 or 1 is a or b or c exists in values
s=pd.Series(['a', 'a|b', np.nan, 'a|c'])
print s.str.get_dummies(sep='|')

# 6.10: Create pandas dataframe having keys and ltable and rtable
ltable={'key': ['One', 'Two'], 'ltable': [1, 2]}
rtable={'key': ['One', 'Two'], 'rtable': [4, 5]}
df1=pd.DataFrame(data=ltable)
df2=pd.DataFrame(data=rtable)
df1.add(df2,fill_value=0)
print df1