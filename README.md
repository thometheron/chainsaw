# Project Chainsaw - Top Movies
## Overview
### Why the chainsaw? 
This project_name was suggested by gitlab.  
This (chainsaw) operator was going to have some fun with a chainsaw and some rogue trees next to the fence today.
The fun with the chainsaw is still in play - but alas, there is a python in the grass that demands his attention.

### Data Insights:
A. Fetch top 15 movies with a minimum of 100 votes. Please note that ranking is calculated by formula: (numVotes /
averageNumberOfVotes) * averageRating
B. List of the title of these top 15 movies

### Dataset:
Required data to be downloaded to the ./data folder.  **This will be catered for in code**

**Data Set [Documentation](https://www.imdb.com/interfaces/)**

[**dataset**:https://datasets.imdbws.com/](https://datasets.imdbws.com/)
* [name.basics](https://datasets.imdbws.com/name.basics.tsv.gz)
* [title.akas](https://datasets.imdbws.com/title.akas.tsv.gz)
* [title.basics](https://datasets.imdbws.com/title.basics.tsv.gz)
* [title.crew](https://datasets.imdbws.com/title.crew.tsv.gz)
* [title.episode](https://datasets.imdbws.com/title.episode.tsv.gz)
* [title.principals](https://datasets.imdbws.com/title.principals.tsv.gz)
* [title.ratings](https://datasets.imdbws.com/title.ratings.tsv.gz)

<hr>
##  Data Exploration
### Jupyter
Notebook ./notebooks/explorer.ipynb
The notebook opens all (pre-downloaded) files from the ./data folder, loads to a pandas dataframe and preview
> Only the below data-sets will be required for this project:
> title.rating + title.basics

<hr>
## Classes
The below classes are provided:
### MovieData
Base Class for all Movie Data.  This class will also be used for the "rated" titles

#### Constructor

#### Methods

### Ratings
This class extends MovieData.  Functionality is added to rank the movies based on the provided formula
> (numVotes / averageNumberOfVotes) * averageRating

#### Constructor

#### Methods

<hr>
## Unit Tests
1. test_file_download.py:  Files are opened from local disc - the option is provided to download the latest version of the file. This test case will test the file download
3. test_load_data.py:  Test loading data from disc an display
4. test_ratings.py: Test ratings class: Load data, compute average, rank data, return top n records
5. test_top_titles.py: Load top n titles and display

<hr>
## Execution

<hr>
## Execution: Jupyter

