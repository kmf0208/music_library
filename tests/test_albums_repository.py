from lib.albums import Album
from lib.albums_repository import AlbumsRepository

def test_get_all_albums(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumsRepository(db_connection) # Create a new ArtistRepository
    album = repository.all()
    # Assert on the results
    assert album == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
    ]


def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumsRepository(db_connection)

    artist = repository.find(3)
    assert artist == Album(3, 'Waterloo', 1974, 2)