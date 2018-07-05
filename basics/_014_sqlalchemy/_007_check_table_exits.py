from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base

Modal = declarative_base()
class Example(Modal):
   __tablename__ = "ex_t"
   id = Column(Integer, primary_key=True)
   name = Column(String(20))

db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)
Modal.metadata.create_all(engine)

# check register table exist to Modal
for _t in Modal.metadata.tables:
    print(_t)

# check all table in database
meta = MetaData(engine, reflect=True)
for _t in meta.tables:
    print(_t)

# check table names exists via inspect
ins = inspect(engine)
for _t in ins.get_table_names():
    print(_t)