from lib.albums import Album

class AlbumsRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM albums')
        albums = []
        for i in rows:
            item = Album(i['id'], i['title'], i['release_year'], i['artist_id'],)
            albums.append(item)
        return albums
    
    def find(self, album_id):
        rows = self.connection.execute('SELECT * FROM albums WHERE id =%s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row['artist_id'])
