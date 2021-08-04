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

import mysql.connector
from random import choice, randint
from sqlalchemy.engine import create_engine
from sqlalchemy.sql.schema import Column, MetaData, Table
from sqlalchemy.sql.sqltypes import Integer, String


def create_database():
    db_connection = mysql.connector.connect(host="localhost", user="root", password="12345")
    db_cursor = db_connection.cursor()
    db_cursor.execute("CREATE DATABASE players")
    db_cursor.close()
    db_connection.close()


def create_table(metadata, engine):
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


def create_player() -> tuple:
    nicknames = [
        "David",
        "Robert",
        "Mario",
        "Lawrence",
        "Anita",
        "Carlson",
        "Cedric",
        "Ortega",
        "Elliot",
        "Robles",
        "Emilio",
        "May",
        "Elisabeth",
        "Riley",
        "Robyn",
        "Contreras",
        "Sean",
        "Robbin",
        "Ashlee",
        "Kelly",
    ]
    roles = ["wizard", "warrior", "priest", "dark knight", "archer"]
    level = randint(1, 30)
    strenght = randint(5, 15)
    dexterity = randint(5, 15)
    mind = randint(5, 15)
    for name in nicknames:
        yield (name, choice(roles), level, strenght, dexterity, mind)


def main():
    create_database()

    engine = create_engine("mysql+mysqlconnector://root:12345@localhost/players", echo=True)
    metadata = MetaData()

    conn = engine.connect()

    players = create_table(metadata, engine)

    for _ in range(20):
        player_data = players.insert().values(*create_player)
        conn.execute(player_data)
        print(player_data.nickname)


if __name__ == "__main__":
    main()
