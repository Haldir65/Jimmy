from sqlalchemy import create_engine

db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)

# Create connection
conn = engine.connect()
# Begin transaction
trans = conn.begin()
conn.execute('INSERT INTO "EX1" (name) '
             'VALUES ("Hello there")')
trans.commit()

result = engine.execute('SELECT * FROM '
                        '"EX1"')
for _r in result:
   print(_r)
# Close connection
conn.close()