from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import select
from sqlalchemy import or_


def clean_up_table(engine):
      db_uri = 'sqlite:///db.sqlite'
      engine = create_engine(db_uri,echo=True)  
      meta = MetaData(engine,reflect=True) 
      conn = engine.connect()
      table = meta.tables['user']
      del_st = table.delete().where(table.c.id > 100)
      print('-------deleting stuff--------')
      res = conn.execute(del_st)
      sel_st = table.select()
      res = conn.execute(sel_st)
      print('-----------heads up!!-----------')
      for _row in res:
            print(_row)

def select_stuff_from_table(engine):
      db_uri = 'sqlite:///db.sqlite'
      engine = create_engine(db_uri)
      conn = engine.connect()

      meta = MetaData(engine,reflect=True)
      table = meta.tables['user']

      # select * from 'user'
      select_st = select([table]).where(
      table.c.l_name == 'Hello')
      res = conn.execute(select_st)
      for _row in res:
            print(_row)

      # or equal to
      select_st = table.select().where(
      table.c.l_name == 'Hello')
      res = conn.execute(select_st)
      for _row in res:
            print(_row)

      # combine with "OR"
      select_st = select([
      table.c.l_name,
      table.c.f_name]).where(or_(
            table.c.l_name == 'Hello',
            table.c.l_name == 'Hi'))
      res = conn.execute(select_st)
      for _row in res:
            print(_row)

      # combine with "ORDER_BY"
      select_st = select([table]).where(or_(
            table.c.l_name == 'Hello',
            table.c.l_name == 'Hi')).order_by(table.c.f_name)
      res = conn.execute(select_st)
      for _row in res:
            print(_row)


def insert_data_into_table(engine):
      meta = MetaData(engine)
      table = Table('user', meta,
                  Column('id', Integer, primary_key=True),
                  Column('l_name', String),
                  Column('f_name', String))
      # insert data via insert() construct
      ins = table.insert().values(
            l_name='Hello',
            f_name='World')
      conn = engine.connect()
      conn.execute(ins)

      # insert multiple data
      conn.execute(table.insert(),[
      {'l_name':'Hi','f_name':'bob'},
      {'l_name':'yo','f_name':'alice'}])

def creta_table_if_non_exists(engine,table_name):
      # create table
      if not engine.dialect.has_table(engine,table_name=table_name):
            meta = MetaData(engine)
            table = Table(table_name, meta,
                        Column('id', Integer, primary_key=True),
                        Column('l_name', String),
                        Column('f_name', String))
            meta.create_all()
      else:
            print('table %s already exists' % (table_name))
def main():
      db_uri = 'sqlite:///db.sqlite'
      engine = create_engine(db_uri,echo=True)
      # creta_table_if_non_exists(engine,'user')
      # insert_data_into_table(engine)
      # select_stuff_from_table(engine)
      clean_up_table(None)


if __name__ == '__main__':
      main()   