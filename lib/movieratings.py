from lib.moviedata import MovieData
import pandas as pd


class Ratings(MovieData):

    def __init__(self, data_file_url, local_file_location="./data/", download_file=False, load_data=True,
                 data_file_compression="gzip", data_file_separator="\t",
                 data_filter="numVotes > 100", votes_column="numVotes"):
        super().__init__(data_file_url=data_file_url, local_file_location=local_file_location,
                         download_file=download_file, load_data=load_data,
                         data_file_compression=data_file_compression, data_file_separator=data_file_separator,
                         data_filter=data_filter)

        if load_data:
            self.rank_data(votes_column=votes_column)

    @property
    def avg_num_votes(self):
        return self.__avg_num_votes

    @classmethod
    def calculate_rank(cls, avg_votes, row):
        return row["numVotes"] / avg_votes * row["averageRating"]

    def rank_data(self, votes_column="numVotes"):
        self.__avg_num_votes = self.data_df[votes_column].mean()
        self.data_df["rank"] = self.data_df.apply(lambda row: self.calculate_rank(self.avg_num_votes, row),
                                                  axis=1)
    def get_top_titles_df(self, topn=15, rated_column="rank"):
        return self.data_df.nlargest(topn, rated_column)


    def get_top_titles_keys(self, topn=15, rated_column="rank", title_key="tconst"):
        return self.data_df.nlargest(topn, rated_column)[title_key].to_numpy()

    def get_top_titles_keys_str(self, topn=15, rated_column="rank", title_key="tconst"):
        top_titles = self.data_df.nlargest(topn, rated_column)[title_key].to_numpy()
        top_titles_str = "[";
        for title in top_titles:
            top_titles_str = top_titles_str + "'" + title + "',"

        return top_titles_str + "0]"