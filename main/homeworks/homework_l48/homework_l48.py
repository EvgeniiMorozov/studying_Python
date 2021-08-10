"""
Написать программу с использованием библиотеки SQLAlchemy ORM, которая:

1. Создаёт на сервере базу данных для товаров в магазине;
2. Создаёт в этой базе таблицу товаров, где для каждого товара определёно:
    2.1. Название
    2.2. Местоположение (напр. Склад №1, Склад №2...)
    2.3. Количество
    2.4. Цена
    2.5. И/или любые другие игровые параметры;
3. Наполняет таблицу данными (от 10 строк);
4. Делает выборку/группировку по условию, основанному на игровых параметрах.

В личный кабинет загрузить .py файл с исходным ходом программы.
"""
from os.path import exists
from random import choice, randint

import mysql.connector
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from stuff import LOCATION
from stuff import PRODUCTS


Base = declarative_base()


def create_database():
    db_conn = mysql.connector.connect(host="localhost", user="root", password="")
    db_cursor = db_conn.cursor()
    db_cursor.execute("CREATE DATABASE product")
    db_cursor.close()
    db_conn.close


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    title = Column(String(45), nullable=False, unique=True)
    location = Column(String(45), nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


def fill_data(session: sessionmaker, table: Product):
    for product in PRODUCTS:
        session.add(table(title=product, location=choice(LOCATION), amount=randint(3, 10), price=randint(30, 90)))


def main():
    # create_database()

    if not exists("app.sqlite"):
        print("Создайте файл: app.sqlite")

    # engine = create_engine("mysql+mysqlconnector://root:@localhost/product")
    engine = create_engine("sqlite:///app.sqlite")
    Base.metadata.create_all(engine)
    with sessionmaker(engine).begin() as session:
        fill_data(session, Product)


if __name__ == "__main__":
    main()
