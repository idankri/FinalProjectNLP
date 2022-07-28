from bs4 import BeautifulSoup
import requests

from custom_exceptions import SongNotFoundError

LYRICS_FREAK_URL = "https://www.lyricsfreak.com"
SONG_PRIMARY_CLASS = "lf-link lf-link--primary"
LYRICS_PRIMARY_CLASS = "lyrictxt js-lyrics js-share-text-content"


class SongScraper:
    @staticmethod
    def get_all_songs(band_name: str):
        song_url_dict = SongScraper.fetch_song_url_dict(band_name)
        return SongScraper.song_url_dict_to_song_list(song_url_dict)

    @staticmethod
    def band_name_to_url(band_name: str):
        return f"{LYRICS_FREAK_URL}/{band_name[0]}/{band_name}"

    @staticmethod
    def parsed_html_song_to_url(parsed_html_song):
        uri = parsed_html_song.get('href')
        return f"{LYRICS_FREAK_URL}{uri}"

    @staticmethod
    def parsed_html_song_to_song_name(parsed_html_song):
        return parsed_html_song.text.strip()[:-7]

    @staticmethod
    def fetch_song_url_dict(band_name: str):
        url = SongScraper.band_name_to_url(band_name)
        html_text = requests.get(url)
        parsed_html = BeautifulSoup(html_text.text, "html.parser")
        all_songs = parsed_html.find_all("a", {"class": SONG_PRIMARY_CLASS})
        return {SongScraper.parsed_html_song_to_song_name(song): SongScraper.parsed_html_song_to_url(song) for song in all_songs}

    @staticmethod
    def song_url_dict_to_song_list(song_url_dict: dict):
        res = list()
        for song_name, song_url in song_url_dict.items():
            try:
                lyrics = SongScraper.fetch_song_lyrics(song_url)
                res.append((song_name, lyrics))
            except SongNotFoundError:
                continue

        return res

    @staticmethod
    def fetch_song_lyrics(song_url: str):
        html_text = requests.get(song_url)
        parsed_html = BeautifulSoup(html_text.text, "html.parser")
        try:
            unparsed_lyrics = parsed_html.find_all("div", {"class": LYRICS_PRIMARY_CLASS})[0]
        except IndexError:
            raise SongNotFoundError
        return SongScraper.clean_html_marks(unparsed_lyrics.text)

    @staticmethod
    def clean_html_marks(song: str):
        return song.strip().replace("<br />", "\n").replace("</div>", "'").replace("&#039;", "'")


if __name__ == '__main__':
    print(SongScraper.get_all_songs('metallica'))