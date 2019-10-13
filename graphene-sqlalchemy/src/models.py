from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Table, Unicode,
                        create_engine, func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship


engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


Base = declarative_base()
Base.query = db_session.query_property()


rent_log_table = Table(
    'rent_log',
    Base.metadata,
    Column('customer_id', Integer, ForeignKey('customer.id')),
    Column('scooter_id', Integer, ForeignKey('scooter.id')),
    Column('rented_at', DateTime, default=func.now())
)


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    rental_scooters = relationship('Scooter', secondary=rent_log_table)


class Scooter(Base):
    __tablename__ = 'scooter'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    customers_who_rent = relationship('Customer', secondary=rent_log_table)
