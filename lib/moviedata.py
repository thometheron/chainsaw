from clint.textui import progress
import requests
import pandas as pd


class MovieData:
    __all = {}

    def __init__(self, data_file_url, local_file_location="./data/", download_file=False, load_data=True,
                 data_file_compression="gzip", data_file_separator="\t",
                 data_filter="1 == 1"):
        self.__data_file_url = data_file_url
        self.__local_file_location = local_file_location
        self.__data_file_name = self.get_name_from_path(data_file_url)
        self.__data_file_path = local_file_location + self.data_file_name
        self.__data_df = None
        self.__data_filter = data_filter

        if download_file:
            self.download_data(self.data_file_url, self.data_file_path)

        if load_data:
            self.load_data(data_file_path=self.data_file_path,
                           data_file_compression=data_file_compression,
                           data_file_separator=data_file_separator,
                           data_filter=data_filter)

        MovieData.__all[self.data_file_name] = self

    @property
    def data_filter(self):
        return self.__data_filter

    @property
    def local_file_location(self):
        return self.__local_file_location

    @property
    def data_file_url(self):
        return self.__data_file_url

    @property
    def data_file_name(self):
        return self.__data_file_name

    @property
    def data_file_path(self):
        return self.__data_file_path

    @property
    def data_df(self):
        return self.__data_df

    @classmethod
    def get_name_from_path(cls, data_file_path):
        file_nme_parts = data_file_path.split("/")
        return file_nme_parts[-1]

    @classmethod
    def download_data(cls, file_url, local_file_path):
        r = requests.get(file_url, stream=True)
        with open(local_file_path, 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
                if chunk:
                    f.write(chunk)
                    f.flush()

    def load_data(self, data_file_path, data_file_compression="gzip", data_file_separator="\t",
                  data_filter=""):
        assert data_file_compression in ('Union[Literal["infer", "gzip", "bz2", "zip", "xz", "zstd"], dict[str, Any], '
                                         'None]')
        self.__data_df = pd.read_csv(data_file_path, compression=data_file_compression,
                                     sep=data_file_separator).query(data_filter)
