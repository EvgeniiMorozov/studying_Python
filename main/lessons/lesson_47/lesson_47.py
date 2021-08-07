import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.elements import or_
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.orm import sessionmaker, Session


Base = declarative_base()


def create_database():
    db_connection = mysql.connector.connect(host="localhost", user="root", password="")
    db_cursor = db_connection.cursor()
    db_cursor.execute("CREATE DATABASE shop123")
    db_cursor.execute("SHOW DATABASES")

    for row in db_cursor:
        print(row)

    db_cursor.close()
    db_connection.close()


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False, unique=True)
    email = Column(String(45), nullable=False, unique=True)



def main():
    # create_database()

    engine = create_engine("mysql+mysqlconnector://root:@localhost/shop123", echo=False)
    connection = engine.connect()
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    cust = Customer(name="Sergei", phone="56456546456", email="2347867845@fgdfg.ru")

    # session.add(cust)
    # session.commit()

    # with session as s:
    #     s.add(cust)
    #     s.commit()

    ses = sessionmaker(engine)

    with ses.begin() as s:
        #     for row in s.query(Customer).all():
        #         print(row.name)

        # print(s.query(Customer).count())

        # print(s.query(Customer).get(4).name)

        # print(s.query(Customer).filter(
        #     Customer.id == 4
        # ).all())

        # print(s.query(Customer).filter(or_(Customer.name == "Ilya", Customer.name == "Sergei")).all())
        
        print(s.query(Customer).filter(
            Customer.name != None,
        ).all())


if __name__ == "__main__":
    main()
