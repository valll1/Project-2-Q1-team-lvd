# Project #2: Question 1
This project involves implementing a Python program that scrapes a Wikipedia table of the highest-grossing films and uses the title of the movie as parameters to make requests to the TMDb API. The API will return the movie title, the release date, an overview of the movie, the language the movie is in, and the average rating. All data will be combined into a single dataframe for analysis and storage. 

To run the program: run: python scr/main.py

## Members:
* Lydia Mei
* Valeria Ortega Preciado
* Dora Zhu

## Allocation of Tasks:

Lydia Mei - Lydia was in charge of implementing the database_creation function, which combines the two dataframes (Wikipedia dataframe and API dataframe). This database was exported as a csv file. Additionally, Lydia organized the data into a SQLite database.

Valeria Ortega Preciado - Valeria was in charge of implementing the webscraped_table function, which scrapes a Wikipedia table of the highest-grossing films. The data was put into dataframes, and the movie titles was later used as a parameter for the API scraping. This was later used for the final database. Addtionally, Valeria integrated functions into main branch. 


Dora Zhu - Dora was in charge of implementing the api_implement function, which uses movie titles in the webscraped_table as query values for the TMDb API and returns the relevant movie title, release date, overview of the movie, language the movie is in, and the average rating. The data was put into dataframes and later used for the final database. Additionally, Dora wrote the README.md file, highlighting all contributions made by each member.

