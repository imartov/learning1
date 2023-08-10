import sqlalchemy as db


# двигатель БД, отправная точка sql-приложения
engine = db.create_engine('sqlite:///products-sqlalchemy.db')

# устанавливаем соединение с БД
connection = engine.connect()

# создаем объект для хранения таблиц в БД
metadata = db.MetaData()

# создание таблицы
products = db.Table('products', metadata, 
                    db.Column('product_id', db.Integer, primary_key=True),
                    db.Column('product_name', db.Text),
                    db.Column('suplier_name', db.Text),
                    db.Column('price_per_tonne', db.Integer))

metadata.create_all(engine)

# создаем объект данных
insertion_query = products.insert().values([
    {"product_name": "Banana", "suplier_name": "United Bananas", "price_per_tonne": 7000},
    {"product_name": "Avocado", "suplier_name": "United Avocados", "price_per_tonne": 12000},
    {"product_name": "Tomatoes", "suplier_name": "United Tomatoes", "price_per_tonne": 3100}
])

# выполняем вставку созданного объекта данных
connection.execute(insertion_query)

# создаем объект выборки
select_all_query = db.select([products]) # заключаем имя таблицы в спсиок, так как ожидаем множественное знаение

# выполняем операцию с помощью connection
select_all_result = connection.execute(select_all_query)

# вывод в консоль
print(select_all_result.fetchall())