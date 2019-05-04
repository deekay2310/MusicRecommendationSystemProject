import pandas as pd
from sklearn.model_selection import train_test_split



#This step might take time to download data from external sources
song_df = pd.read_csv("song_df.csv")
#print(song_df.head(16))


song_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
grouped_sum = song_grouped['listen_count'].sum()
song_grouped['percentage']  = song_grouped['listen_count'].div(grouped_sum)*100
song_grouped.sort_values(['listen_count', 'song'], ascending = [0,1])

#training data model
train_data, test_data = train_test_split(song_df, test_size = 0.3, random_state=0)
# print(train_data.head(5))


users = song_df['user_id'].unique()
#print(len(users))


songs = song_df['song_id'].unique()