from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from datetime import datetime

db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri,echo=True)

Base = declarative_base()

class TestTable(Base):
    __tablename__ = 'Test Table'
    id   = Column(Integer, primary_key=True)
    key  = Column(String, nullable=False)
    val  = Column(String)
    date = Column(DateTime, default=datetime.utcnow)

# create tables
# Base.metadata.create_all(bind=engine)

# create session
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# data = {'a': 5566, 'b': 9527, 'c': 183}
# try:
#     for _key, _val in data.items():
#         row = TestTable(key=_key, val=_val)
#         session.add(row)
#     session.commit()
# except SQLAlchemyError as e:
#     print(e)

try:
    row = session.query(TestTable).filter(TestTable.key=='a').first()
    print('original: %s %s ' % (row.key,row.val))
    row.key = 'aa'
    row.val = 'new value'
    session.commit()
except SQLAlchemyError as e:
    print(e)    
finally:
    session.close()