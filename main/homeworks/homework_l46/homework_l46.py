"""
Написать программу с использованием библиотеки SQLAlchemy, которая:

1. Создаёт на сервере базу данных для какой-нибудь игры;
2. Создаёт в этой базе таблицу игроков, где для каждого игрока определён:
    2.1. Ник
    2.2. Уровень
    2.3. Сила
    2.4. Ловкость
    2.5. Интеллект
    2.6. И/или любые другие игровые параметры;
3. Наполняет таблицу данными (от 10 строк);
4. Делает выборку/группировку по условию, основанному на игровых параметрах.

В личный кабинет загрузить .py файл с исходным ходом программы.
"""


from os.path import exists
from random import choice
from random import randint

import mysql.connector
from sqlalchemy.engine import create_engine
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.schema import MetaData
from sqlalchemy.sql.schema import Table
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql.sqltypes import String

NICKNAMES = [
    "David", "Robert", "Mario", "Lawrence", "Anita", "Carlson", "Cedric", "Ortega", "Sean", "Robbin",
    "Elliot", "Robles", "Emilio", "May", "Elisabeth", "Riley", "Robyn", "Contreras", "Ashlee", "Kelly"
]
ROLES = ["wizard", "warrior", "priest", "dark knight", "archer", "cleric"]


def create_database():
    """
    Создание базы данных на сервере MySQL
    """
    db_connection = mysql.connector.connect(host="localhost", user="root", password="")
    db_cursor = db_connection.cursor()
    db_cursor.execute("CREATE DATABASE players")
    db_cursor.close()
    db_connection.close()


def create_sqlite_database():
    pass


def create_table(metadata, engine):
    """
    Создание таблицы player
        nickname - имя игрока
        role - тип персонажа
        level - уровень персонажа
        strenght, dexterity, mind - сила, ловкость и интеллект персонажа
    """
    player = Table(
        "player",
        metadata,
        Column("id", Integer(), primary_key=True),
        Column("nickname", String(45), nullable=False, unique=True),
        Column("role", String(45), nullable=False),
        Column("level", Integer(), nullable=False),
        Column("strenght", Integer(), nullable=False),
        Column("dexterity", Integer(), nullable=False),
        Column("mind", Integer(), nullable=False),
    )

    metadata.create_all(engine)

    return player


def main():
    # create_database()

    if not exists("app.sqlite"):
        print("Создайте файл: app.sqlite")

    # Драйвер для подключения к БД MySQL
    # engine = create_engine("mysql+mysqlconnector://root:@localhost/players", echo=True)
    # conn = engine.connect()

    # Драйвер для подключения к БД SQLITE3
    sqlite_engine = create_engine("sqlite:///app.sqlite")
    sqlite_conn = sqlite_engine.connect()

    metadata = MetaData()

    # player = create_table(metadata, engine)

    player = create_table(metadata, sqlite_engine)

    #  "Заливаем" данные в нашу БД
    # for i in range(len(NICKNAMES)):
    #     insert_query = player.insert().values(
    #         nickname=f"{NICKNAMES[i]}",
    #         role=f"{choice(ROLES)}",
    #         level=randint(1, 30),
    #         strenght = randint(5, 15),
    #         dexterity = randint(5, 15),
    #         mind = randint(5, 15)
    #     )
    #     print(insert_query)
    #     result = sqlite_conn.execute(insert_query)

    # Выполнение подзапросов к БД

    # Отобразить "всю" таблицу
    select_all = player.select()
    result = sqlite_conn.execute(select_all)

    # print(result.fetchmany(5))
    # print(result.fetchmany(3))

    for row in result:
        print(row)

    # Запросы с условием
    where_query = select([player]).where(player.columns.role != "dark knight")
    result_where = sqlite_conn.execute(where_query)
    print(result_where.fetchall())

    where_query_1 = select([player]).where((player.columns.role != "dark knight") and (player.columns.level >= 15))
    result_where_1 = sqlite_conn.execute(where_query_1)
    print(result_where_1.fetchall())


if __name__ == "__main__":
    main()
