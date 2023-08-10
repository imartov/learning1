import sqlalchemy as db 


metadata = db.MetaData() # информация о БД и ее объектах

authors = db.Table("authors", metadata,
    db.Column("id_author", db.Integer, primary_key=True),
    db.Column("name", db.String(250))
)

books = db.Table("books", metadata,
    db.Column("id_book", db.Integer, primary_key=True),
    db.Column("title", db.String(250), nullable=False),
    db.Column("author_id", db.Integer, db.ForeignKey("authors.id_author")),
    db.Column("genre", db.String(250)),
    db.Column("price", db.Integer)
)

engine = db.create_engine('sqlite:///books.db')
metadata.create_all(engine)

conneection = engine.connect()

insert_author_query = authors.insert().values([
    {"name": "Lutz"}
])
conneection.execute(insert_author_query)
conneection.close()

insert_books_query = books.insert().values([
    {"title": "Learn Python", "author_id": 1, "genre": "Education", "price": 1299},
    {"title": "Clear Python", "author_id": 1, "genre": "Education", "price": 956},
])
conneection.execute(insert_books_query)
conneection.close()

books_gr_1000_query = books.select().where(books.columns.price > 1000)
result = conneection.execute(books_gr_1000_query)

for row in result:
    print(row)

join_select = db.select([authors, books]).where(authors.columns.id_author == books.columns.author_id)
result_join = conneection.execute(join_select)
print(result_join)
# TODO: fix exception