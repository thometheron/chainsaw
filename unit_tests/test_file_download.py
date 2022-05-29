from datetime import datetime
import os
from lib.moviedata import MovieData

ratings = MovieData(data_file_url="https://datasets.imdbws.com/title.ratings.tsv.gz", download_file=True, load_data=False)
print("File Name:", ratings.data_file_name)
print("File Path:", ratings.data_file_path)
print("File Size:", os.path.getsize(ratings.data_file_path)/1024/1024, "MB")
print("File Download Date:", datetime.fromtimestamp(os.path.getmtime(ratings.data_file_path)).strftime("%Y-%m-%d %H:%M:%S"))