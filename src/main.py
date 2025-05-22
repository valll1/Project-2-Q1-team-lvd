# Imports the neccesary libraries for the code to function
#import libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv


# Imports specific functions from other Python files into main.py.
from api_implement import movie_info
from database_creation import combine_dataframe, create_table
from webscraped_table import web_scrape

# Url variable that holds the Wiki website
url = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_films'

#Calls the web_scrape function and returns the dataframe containing the top 50 highest grossing films
results_df = web_scrape(url)

# Runs each movie title through the movie_info function
movie_api_data = [movie_info(title) for title in results_df['movie_titles']] #Iterates through the 'movie_titles' column from the dataframe, and running the titles through the movie_info function

#Takes the results from the movie_api_data variable and creates a dataframe
api_df = pd.DataFrame(movie_api_data)

# Combines the two previous Data Frame using the combine_dataframe function
highest_grossing_films_df = combine_dataframe(results_df, api_df)
# Prints combined Data Frame
print(highest_grossing_films_df)

create_table()
