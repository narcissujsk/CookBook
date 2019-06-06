from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__= 'users'
    id= Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test?charset=utf8', echo=True)
    Session = sessionmaker(bind=engine)
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session = Session()
    session.add(ed_user)
    session.commit()
    print('Completed')