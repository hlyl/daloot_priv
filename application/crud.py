from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'some_table'
    id = Column(Integer, primary_key=True)
    firstname =  Column(String(50))
    lastname =  Column(String(50))

def pprint(obj):
    print([u.__dict__ for u in obj])

engine = create_engine('sqlite:///pythonsqlite.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# create a Session
session = Session()

# Create
hlyl = User(firstname="Henrik", lastname="Lunge")
session.add(hlyl)
session.commit()

# Read
pprint(session.query(User).filter(User.firstname=="Henrik").all())

# Update
user=session.query(User).filter(User.firstname=="Henrik").first()
user.lastname = "Lynge"
session.commit()
pprint(session.query(User).filter(User.firstname=="Henrik").all())

# Delete
session.query(User).filter(User.firstname=="Henrik").delete()
session.commit()

pprint(session.query(User).all())
