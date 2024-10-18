import pandas as pd
import numpy as np

df = pd.read_csv('imdb_top_1000.csv')
#print(df)
# data = df.to_numpy()
# print('Data Shape: ', data.shape)
# print('First 5 rows: ', data[:5])

my_set = {
    'Cars': ['Honda', 'Maruti', 'Hyundai', 'Toyota'],
    'ratings': [7,8,6,9]
}
'''
my_df = pd.DataFrame(my_set)
print(my_df)

data = pd.Series([10, 12, 14, 16, 15])
print(data)
'''
###Extracting Columns
imdb_ratings = df['IMDB_Rating'].to_numpy()
votes = df['No_of_Votes'].to_numpy()
print(imdb_ratings[:10], votes[:10])

min_rating = np.min(imdb_ratings)
max_rating = np.max(imdb_ratings)

print(f'Rating is between {min_rating} and {max_rating}')

#Display top-rated movies
top_ratings = imdb_ratings > 8
top_movies = df['Series_Title'][top_ratings]
print(top_movies[:5])

#Find top 10 Movies with max no votes:
top_ten = np.argsort(votes)[-10:]
top_5_movies = df.iloc[top_ten]
print('Top 10:\n', top_5_movies[['Series_Title', 'Director', 'No_of_Votes']])

print(df.info())

#Find the max no of movies released based on year
movies_per_year = df.groupby('Released_Year').size()
max_year = movies_per_year.idxmax()
max_count = movies_per_year.max()
print(f'In the year of {max_year}, {max_count} no of movies were released')

#Get the top 5 directors with max no fo movies
movies_per_director = df.groupby('Director').size()
#max_year = movies_per_year.idxmax()
#max_count = movies_per_year.max()
top_5_directors = movies_per_director.sort_values(ascending=False).head()
print(top_5_directors)

year = df['Released_Year'].unique()
print(year)

#Display Actors of Top rated movies that has rating more than 8.
high_rated = df[df['IMDB_Rating'] > 8.5][['Star1', 'Star2']]
print(high_rated)

#Find the highest Gross Movie:
gross = df['Gross'].to_numpy().max(

)
highest_gross_idx = np.argmax(gross)
highest_grossed_movie = df.iloc[highest_gross_idx]
print('Movie: ', highest_grossed_movie[['Series_Title', 'Gross']])
