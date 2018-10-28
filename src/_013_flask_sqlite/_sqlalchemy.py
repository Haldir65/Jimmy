# 导入:
from sqlalchemy import Column, String,Integer, create_engine,ForeignKey,MetaData,Table
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
import config

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'registereduser'

    # 表的结构:
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(20))
    fullname = Column(String)
    password = Column(String)

    # 一对多:
    books = relationship('Book')
    
    def __repr__(self):
         return "<User(name='%s', fullname='%s', password='%s')>" % ( self.name, self.fullname, self.password)


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(Integer, ForeignKey('registereduser.id'))    

def creat_table(engine):
    # Create a metadata instance
    metadata = MetaData(engine)
    # Declare a table
    table_user = Table('registereduser',metadata,
                Column('id',Integer, primary_key=True,autoincrement=True),
                Column('name',String(20)),
                Column('fullname',String),
                Column('password',String))

    table_books = Table('book',metadata,
                Column('id',Integer, primary_key=True,autoincrement=True),
                Column('name',String(20)),
                Column('user_id',Integer,ForeignKey('registereduser.id')))
    metadata.create_all()       


def main():
        # 初始化数据库连接:
        ## http://docs.sqlalchemy.org/en/latest/core/engines.html
    engine = create_engine('sqlite:///foo.db')
    metadata = MetaData(engine)
    # engine = create_engine('mysql+mysqlconnector://%s:%s@localhost:3306/%s?charset=utf8' % (config.DB_USER_NAME,config.DB_PASS_WORD,config.DB_NAME))
    # 创建DBSession类型:
    creat_table(engine)
    DBSession = sessionmaker(bind=engine)



    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    book1 = Book(id=1,name='therapy one')
    new_user = User(id=5, name='Bob',fullname='Bob fullname',password='bobpassword',books=[book1])
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

if __name__ == '__main__':
    main()