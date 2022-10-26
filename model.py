from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=40), unique=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    id_published = Column(Integer, ForeignKey('publisher.id'), nullable=False)
    title = Column(String(length=40), unique=True)

    publish = relationship(Publisher, backref='boo')


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=40), unique=True)


class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    id_book = Column(Integer, ForeignKey('book.id'), nullable=False)
    id_shop = Column(Integer, ForeignKey('shop.id'), nullable=False)
    count = Column(Integer)

    boo = relationship(Book, backref='stoc')
    sho = relationship(Shop, backref='stoc')


class Sale(Base):
    __tablename__ = 'sale'

    id = Column(Integer, primary_key=True)
    id_stock = Column(Integer, ForeignKey('stock.id'), nullable=False)
    price = Column(Float, nullable=False)
    date_sale = Column(Date, nullable=False)
    count = Column(Integer)

    stoc = relationship(Stock, backref='sal')


def tables_create(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
