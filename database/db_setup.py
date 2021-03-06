
# import dependencies
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


# instantiate sqlalchemy base object
Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'

    # map to table columns
    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    # relate Items of this Category via ForeignKey
    items = relationship("Item")

    @property
    def serialize(self):
        """returns object data in easily serializable format"""
        return {
            'category_id': self.id,
            'category_name': self.name }


class Item(Base):
    __tablename__ = 'items'

    # map to table columns
    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    description = Column(String(1000))
    category_id = Column(Integer, ForeignKey('categories.id'))
    # relate Category of this Item via ForeignKey
    category = relationship("Category")

    @property
    def serialize(self):
        """returns object data in easily serializable format"""
        return {
            'item_id': self.id,
            'item_name': self.name,
            'item_description': self.description,
            'category_id': self.category_id,
            'category_name': self.category.name }


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    email = Column(String(80), nullable = False)
    picture = Column(String(250))



def main():
    # [create and] bind db to SQLAlchemy engine
    engine = create_engine('sqlite:///item_catalog.db')
    # create db tables (Base sub-classes)
    Base.metadata.create_all(engine)

    print("\nDatabase has been setup\n")


if __name__ == '__main__':
    main()