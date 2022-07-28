from song_scraper import SongScraper
from data_writer import DataWriter

PATH = "D:\\IDC\\S6\\NLP\\Project\\Data"

all_bands_to_scrape = {
    'metal': [
        'metallica',
        'megadeth',
        'slayer',
        'kreator',
        'whitechapel',
        'slipknot',
        'meshuggah',
        'behemoth',
        'black+sabbath',
        'system+of+a+down',
        'gojira',
        'municipal+waste',
        'iron+maiden',
        'pantera'],
    'rock': [
        'led+zeppelin',
        'ac+dc',
        'david+bowie',
        'beatles',
        'pink+floyd',
        'queen',
        'red+hot+chili+peppers',
        'nirvana',
        'arctic+monkeys',
        'guns+n+roses',
        'rush',
        'rolling+stones',
        'pearl+jam',
        'jimi+hendrix',
        'frank+zappa'
    ],
    'hiphop': [
        'mac+miller',
        'kendrick+lamar',
        '2+pac',
        'nwa',
        'eminem',
        'drake',
        'jay+z',
        'asap+rocky',
        'snoop+dogg',
        'ice+cube',
        'j+cole',
        'kanye+west',
        'mf+doom',
        'anderson+paak'
    ],
    'pop': [
        'lady+gaga',
        'sia',
        'justin+bieber',
        'justin+timberlake',
        'madonna',
        'britney+spears',
        'michael+jackson',
        'Taylor+Swift',
        'Ariana+Grande',
        'Miley+Cyrus',
        'maroon+5',
        'jennifer+lopez',
        'beyonce',
        'billie+eilish'
    ],
    'reggae': [
        'bob+marley',
        'peter+tosh',
        'gregory+isaacs',
        'desmond+dekker',
        'jimmy+cliff',
        'dennis+brown',
        'burning+spear',
        'sizzla',
        'bunny+wailer',
        'marcia+griffiths',
        'ziggy+marley',
        'yellowman',
        'toots+the+maytals',
        'black+uhuru',
        'the+gladiators',
        'damian+jr+gong+marley',
        'ub40',
        'koffee',
        'buju+banton'
    ]
}


if __name__ == '__main__':
    genres_and_progress = [('reggae', 0), ('pop', 0), ('hiphop', 0)]
    for genre, progress in genres_and_progress:
        print(f"Current genre: {genre}")
        dw = DataWriter(PATH, genre)
        artists = all_bands_to_scrape[genre][progress:]

        for i, artist in enumerate(artists):
            print(f"Current artist: {artist}, {i + progress}")
            all_songs = SongScraper.get_all_songs(artist)
            dw.write_data(all_songs)
            print(f"Finished processing artist {i + progress}")

        print(f"Finished processing genre {genre}")
