from lib.movieratings import Ratings

data_file_url = "https://datasets.imdbws.com/title.ratings.tsv.gz"

_ratings = Ratings(data_file_url)

print("Data File Name:", _ratings.data_file_name)
print("Filter:",_ratings.data_filter)

print("Avg Votes (for filtered subset):", _ratings.avg_num_votes)
print("Ratings: Top Titles - Keys:\n", _ratings.get_top_titles_keys(topn=15))
print("Ratings: Top Titles:\n", _ratings.get_top_titles_df())