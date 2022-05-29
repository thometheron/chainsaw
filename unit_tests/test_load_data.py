from datetime import datetime
import os
from lib.moviedata import MovieData

top_title_keys = ['tt0111161', 'tt0468569', 'tt1375666', 'tt0944947', 'tt0137523', 'tt0110912',
                 'tt0109830', 'tt0903747', 'tt0068646', 'tt0133093', 'tt0167260', 'tt0120737',
                 'tt0816692', 'tt0167261', 'tt1345836']


print(str(top_title_keys))
titles = MovieData(data_file_url="https://datasets.imdbws.com/title.basics.tsv.gz",
                    data_filter="tconst in " + str(top_title_keys), download_file=False, load_data=True)

print(titles.data_df)
