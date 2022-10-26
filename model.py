from sqlalchemy import Column, Integer, String, ForeignKey
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
