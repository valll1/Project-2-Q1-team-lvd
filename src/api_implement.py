
'''
This function returns the basic movie information (Title, Release Date, Overview, Language, Average Rating) from the TMDb API for the list of highest-grossing films.
'''

def movie_info(title):

  # Dictionary for the TMDb API key for authentication and the movie title that is being searched
  query_params = {
      'api_key': TMDB_API_KEY,
      'query': title
  }

  # Makes an API request to TMDb search
  query_response = requests.get(api_url, params = query_params)

  # Loop for if the request is successful
  if query_response.status_code == 200:
    data = query_response.json()
    results = data.get('results')

    # Loop for if the result exists
    if len(results) > 0:

      # Returns the first result
      movie = results[0]

      # Returns the basic movie information
      return {
          'Title': movie.get('title'),
          'Release Date': movie.get('release_date'),
          'Overview': movie.get('overview'),
          'Language': movie.get('original_language'),
          'Average Rating': movie.get('vote_average')
      }

    # If no results are found for the movie, an error message is presented
    else:
      return {
          'Title': title, 'Error': 'No results found'
      }

  # If the request to the TMDb is unsuccessful, an error message is presented
  else:
    return {
        'Title': title, 'Error': f'Error: {query_response.status_code}: {query_response.text}'
    }

# Movie data is collected through list comprehension
movie_api_data = [movie_info(title) for title in titles]

api_df = pd.DataFrame(movie_api_data)