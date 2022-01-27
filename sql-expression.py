from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

db = create_engine("postgresql+psycopg2://gitpod@127.0.0.1/chinook")

meta = MetaData(db)

artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key =True),
    Column("Name", String)
)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key =True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key =True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.ArtistId")),
    Column("MediaTypeId", Integer, primary_key =False),
    Column("GenreId", Integer, primary_key =False),
    Column("Composer", String),
    Column("Milliseconds", String),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


with db.connect() as connection:
    #select_query = artist_table.select().with_only_columns(artist_table.c.Name)
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)