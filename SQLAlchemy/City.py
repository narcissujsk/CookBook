from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy import ForeignKey
import json
from sqlalchemy.orm import relationship, backref
Base = declarative_base()
import unittest





class City(Base):
    def __init__( self ):
        print("City")

    __tablename__= 'city'
    ID= Column(Integer, primary_key=True)
    Name = Column(String)
    CountryCode = Column(String,ForeignKey('country.Code'))
    District = Column(String)
    Population= Column(Integer)
    country=relationship('Country')

    def __repr__(self):
        return "{ID:'%s',Name:'%s',country:%s}" % (self.ID,self.Name,self.country.Name)


class Country(Base):
    __tablename__= 'country'
    Code = Column(Integer, primary_key=True)
    Name = Column(String)
    #一对多
    citys = relationship('City')

    def __repr__( self ):
        return "{Code:'%s',Name:'%s',citys:%s}" % (self.Code, self.Name, self.citys)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/world?charset=utf8', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    print()
    print()

    for instance in session.query(City).order_by(City.ID).limit(1):
        print(instance)
    print('Completed')
    print()

    for instance in session.query(City).order_by(City.ID).limit(1):
        print(instance)
    print('Completed')
    print()


    for id, name in session.query(City.ID, City.Name).limit(1):
        print(name, id)
    print()


    for instance in session.query(Country).limit(10):
        print("*********************")
        print(instance)
        print("*********************")

    for row in session.query(City.Name.label('name_label')).limit(1):
        print(row.name_label)
    print()

    for instance in session.query(City).from_statement(text("SELECT* FROM city where CountryCode=:CountryCode Limit 1")).params(CountryCode='CHN'):
        print(instance.ID, instance.Name)
    print()

