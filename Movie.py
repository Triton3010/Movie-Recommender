
# coding: utf-8

# In[1]:




# In[15]:

import pandas as pd
col1 = ['movie_id','title']
col2 = ['user_id','movie_id','rating'] 
movies = pd.read_csv('movies.csv'  , usecols=range(2))
ratings = pd.read_csv('ratings.csv' , usecols=range(3))
rate = pd.merge(movies,ratings)
rate.head()


# In[17]:

movie_rate = rate.pivot_table(index=['userId'], columns='title' , values='rating')
movie_rate.head()


# In[51]:

ins =  movie_rate['Saving Private Ryan (1998)']
ins.head(50)


# In[52]:

similar = movie_rate.corrwith(ins)
similar = similar.dropna()
df = pd.DataFrame(similar)
df.head(50)


# In[53]:

similar.sort_values(ascending=False)


# In[54]:

import numpy as np
movie_stats = rate.groupby('title').agg({'rating': [np.size, np.mean]})
movie_stats.head(50)


# In[56]:

popular = movie_stats['rating']['size'] >= 100
movie_stats[popular].sort_values([('rating','mean')], ascending=False)[:15]


# In[59]:

de = movie_stats[popular].join(df)
de.head()


# In[50]:

df.sort_values(['similar'], ascending=False)


# In[ ]:



