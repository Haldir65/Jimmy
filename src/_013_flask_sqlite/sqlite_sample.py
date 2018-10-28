# coding: utf-8

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base		

import uuid, random

Base = declarative_base()

class ApplyCode(Base):
	__tablename__ = 'applycode'
	id     = Column('id', Integer, primary_key=True)
	code   = Column('code', String)
	status = Column('status', Integer, default=1)
	uid    = Column('uid', String)

engine = create_engine('sqlite:///data.db', echo=True)
Database= sessionmaker(bind=engine)

if __name__ == '__main__':
	db = Database()
	# try:
	# 	for x in range(17):
	# 		code = ''
	# 		for i in xrange(3): code += random.choice('abcdefghijklmnopqrstuvwxyz'.upper())
	# 		for i in xrange(3): code += random.choice('0123456789')
	# 		app = ApplyCode(code=code, uid=str(uuid.uuid4()))
	# 		db.add(app)
	# 	db.commit()
	# except Exception, e:
	# 	print e
	# 	db.rollback()

	idlist = [144,143,142,141,140]
	query = db.query(ApplyCode)
	query = query.filter(ApplyCode.id.in_(idlist))
	query = query.order_by(-ApplyCode.id)
	data  = query.all()
	# print data.id
	# print data.code
	# print data.uid

	for x in data:
		print(x.id)
