from sqlalchemy import (
    create_engine,
    inspect,
    Column,
    String,
    MetaData,
    Table,
    Integer)

from sqlalchemy.ext.declarative import declarative_base

db_url = "sqlite:///db.sqlite"
engine = create_engine(db_url,echo=True)

# Base = declarative_base()

# class TemplateTable(object):
#     id   = Column(Integer, primary_key=True)
#     name = Column(String)
#     age  = Column(Integer)

# class DowntownAPeople(TemplateTable, Base):
#     __tablename__ = "downtown_a_people"

# class DowntownBPeople(TemplateTable, Base):
#     __tablename__ = "downtown_b_people"

# Base.metadata.create_all(bind=engine)

meta = MetaData(engine)
# table = Table('Test1', meta,
#               Column('id', Integer, primary_key=True),
#               Column('key', String, nullable=True),
#               Column('val', String))

# table.create(engine)

# # check table exists
# ins = inspect(engine)
# for _t in ins.get_table_names():
#     print(_t)

# table.drop(engine)    

t = Table('ex_table', meta,
          Column('id', Integer, primary_key=True),
          Column('key', String),
          Column('val', Integer))
# Get Table Name

t.create()
print(t.name)

# Get Columns
print(t.columns.keys())

# Get Column
c = t.c.key
print(c.name)
# Or
c = t.columns.key
print(c.name)

# Get Table from Column
print(c.table)

# check table exists
ins = inspect(engine)
for _t in ins.get_table_names():
    print(_t)