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
Base Class for all Movie Data.  It provides functionality to:
1.  Download data to local
2.  Open downloaded data an load to (instance) dataframa
3.  Data is filtered on (after) load and filtered result is retained
This class will also be used as a contained for the "top ranked" titles

#### Constructor
 * data_file_url (property): URL to download data source file 
 * local_file_location (property) ="./data/":  Location of data-file on local system.  The location is relative to the running folder of fully qualified name is not passed 
 * download_file=False: True|False: False: Local copy of data file will be used, otherwise the latest version will be downloaded 
 * load_data=True: Initialize and load data 
 * data_file_compression="gzip": Data file compression mechanism.  Supported: "infer", "gzip", "bz2", "zip", "xz", "zstd"
 * data_file_separator="\t": Data file field separator
 * data_filter (property) ="1 == 1"): Data filter - Filter will be applied after full load, and only filtered data persisted

#### Properties (Not in constructor)
 *  data_file_path: Path to data file (NOT SETABLE: derived from local_file_location and file_name)
 *  data_file_name: File name - based on URL (NOT SETABLE)
 *  data_df: Dataframe with data (Populated in constructor or load_data)

#### Methods



##### Class Methods
  * get_name_from_path: Extract data_file_name from path
     * Parameters: 
        * data_file_path: Full (Relative) data file path (file_name included).
           
  * download_data: 
     * Parameters:
        * file_url: Data file URL
        * local_file_path: Local path to save file

##### Instance Methods
 * load_data: Load data from data file and apply filter: Result stored in data-frame
     * Parameters
        * data_file_path
        * data_file_compression
        * data_file_separator
        * data_filter
 
### Ratings
This class extends MovieData.  Functionality is added to rank the movies based on the provided formula
> (numVotes / averageNumberOfVotes) * averageRating

1. Inherited functionality from base (MovieData)
2. Compute Average (mean) rating for loaded data-set
3. Rank data
4. Rreturn top-n records

#### Constructor
 * Inherited
   * data_file_url (property): URL to download data source file 
   * local_file_location (property) ="./data/":  Location of data-file on local system.  The location is relative to the running folder of fully qualified name is not passed 
   * download_file=False: True|False: False: Local copy of data file will be used, otherwise the latest version will be downloaded 
   * load_data=True: Initialize and load data 
   * data_file_compression="gzip": Data file compression mechanism.  Supported: "infer", "gzip", "bz2", "zip", "xz", "zstd"
   * data_file_separator="\t": Data file field separator
   * data_filter (property) ="1 == 1"): Data filter - Filter will be applied after full load, and only filtered data persisted
 * Additonal
 *  * **votes_column**: Column name of column that contains the number of votes

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

