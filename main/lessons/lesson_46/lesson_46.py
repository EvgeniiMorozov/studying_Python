from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
import mysql.connector


def create_database():
    db_connection = mysql.connector.connect(host="localhost", user="root", password="")
    db_cursor = db_connection.cursor()
    db_cursor.execute("CREATE DATABASE shop123")
    db_cursor.execute("SHOW DATABASES")

    for row in db_cursor:
        print(row)

    db_cursor.close()
    db_connection.close()


def create_tables(metadata, engine):
    customer = Table(
        "customer",
        metadata,
        Column("id", Integer(), primary_key=True),
        Column("name", String(45), nullable=False),
        Column("phone", String(45), nullable=False, unique=True),
        Column("email", String(45), nullable=False, unique=True),
    )

    customer_cart = Table(
        "cart",
        metadata,
        Column("id", Integer(), primary_key=True),
        Column("customer_id", ForeignKey("customer.id")),
        Column("product", String(45)),
    )

    metadata.create_all(engine)

    return customer, customer_cart


def main():
    # создаём DB shop123
    # create_database()

    engine = create_engine("mysql+mysqlconnector://root:@localhost/shop123", echo=True)
    connection = engine.connect()

    metadata = MetaData()
    customer, cart = create_tables(metadata, engine)

    insert_query = customer.insert().values(name="Vasya", phone="123456789", email="qwer@asd.ru")
    print(insert_query)

    result = connection.execute(insert_query)
    print(result.inserted_primary_key)


if __name__ == "__main__":
    main()
