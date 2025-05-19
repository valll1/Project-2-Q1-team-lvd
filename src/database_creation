#combine the movie_df and api_df into a combined dataframe using the join method
highest_grossing_films_df = movie_df.join(api_df)
#remove duplicate movie title column using drop method
highest_grossing_films_df = highest_grossing_films_df.drop(columns=['Title'])
#print the combined dataframe
highest_grossing_films_df

#print the description statistics of the combined dataframe
print(highest_grossing_films_df.describe())

#output data as csv file
highest_grossing_films_df.to_csv('highest_grossing_films.csv', index=False)

#import libraries
import sqlite3
import pandas as pd

#create database
db_conn = sqlite3.connect('highest_grossing_films.db')
cursor = db_conn.cursor()

#create table
cursor.execute('''
    CREATE TABLE highest_grossing_films (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_title TEXT NOT NULL,
        release_date TEXT NOT NULL,
        overview TEXT NOT NULL,
        language TEXT NOT NULL,
        average_rating FLOAT NOT NULL
    )
''')
db_conn.commit()

#read csv
df = pd.read_csv('highest_grossing_films.csv')

#create a list of tuples to easily insert movie information into table
movie_info = list(zip(df['movie_titles'], df['Release Date'], df['Overview'], df['Language'], df['Average Rating']))

#insert movie_info into table
cursor.executemany("INSERT INTO highest_grossing_films (movie_title, release_date, overview, language, average_rating) VALUES (?, ?, ?, ?, ?)", movie_info)

#commit changes
db_conn.commit()

#close database
db_conn.close()
