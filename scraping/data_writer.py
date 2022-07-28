import pandas as pd
import os


class DataWriter:
    def __init__(self, path, genre):
        self._full_path = f"{path}\\{genre}.csv"
        self._genre = genre

    def write_data(self, song_list: [tuple]):
        df = pd.DataFrame(song_list, columns=['song_name', 'lyrics'])

        if os.path.exists(self._full_path):
            df.to_csv(self._full_path, mode='a', header=False, index=False)
        else:
            df.to_csv(self._full_path, mode='a', header=True, index=False)


if __name__ == '__main__':
    dw = DataWriter("D:\\IDC\\S6\\NLP\\Project\\Data", "test")
    dw.write_data([("a", "asdddads"), ("b", "adada"), ("c", "afafaf")])
