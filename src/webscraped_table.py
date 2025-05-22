''' This function takes a url as a parameter and scrapes through its desired table,
    retrieving and storing all 50 movie titles into a single data frame.'''
#import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

def web_scrape(url):
  page = requests.get(url) # Makes requests to the url

  titles = [] # List to store our movie titles

  if page.status_code == 200: # Only runs if the status code is valid

    soup = BeautifulSoup(page.content, 'html.parser') # To parse through HTML code
    table_tags = soup.find('table') # Looks for the first table tag –– the table we are concered about
    body_tag = table_tags.find('tbody') # Go to the first tbody tag
    movie_titles = body_tag.find_all('tr') # All tr tags, which hold the movie titles

    for x in movie_titles: #loops through the movie_titles tags
      title_name  = x.find('th').get_text().strip() #uses the get_text and strip methods to extract the movie titles
      if title_name == 'Rank': # Makes sure that only movie titles are appended to the titles list
        continue
      else:
        titles.append(title_name.strip()) # Appends if its a valid movie title

  data= {'movie_titles':titles}  # Prepares data for data frame creation

  # Creates and stores data in movie_df dataframe
  movie_df = pd.DataFrame(data)
  return movie_df # Returns dataframe

