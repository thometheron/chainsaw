from lib.moviedata import MovieData
from lib.movieratings import Ratings

rating_data_file_url = "https://datasets.imdbws.com/title.ratings.tsv.gz"
movie_titles_file_url = "https://datasets.imdbws.com/title.basics.tsv.gz"

print("Load rating data and calculate top ranked ")
_ratings = Ratings(rating_data_file_url)

df_top_ranked_movies = _ratings.get_top_titles_df()
top_ranked_movies_keys_arr_str = _ratings.get_top_titles_keys_str()

print(top_ranked_movies_keys_arr_str)

print("Load top titles")
df_top_titles = MovieData(data_file_url=movie_titles_file_url, data_filter="tconst in "+top_ranked_movies_keys_arr_str).data_df

df_result=df_top_ranked_movies.set_index("tconst").join(df_top_titles.set_index("tconst"), how="left", on="tconst", rsuffix="_").reset_index()
print(df_result[["primaryTitle", "rank"]])