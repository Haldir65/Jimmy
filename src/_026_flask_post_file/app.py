from flask import Flask,render_template,request,send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,MetaData,Table,Column
import os,logging
from io import BytesIO
from extensions import save_file_to_disk

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "filestorage.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class FileContents(db.Model):
    __tablename__ = "fileStorages"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)



def create_table_if_non_exists(engine=db.engine):
    if not engine.dialect.has_table(engine, 'fileStorages'):  # If table don't exist, Create.
        metadata = MetaData(engine)
        # Create a table with the appropriate Columns
        ##主键，auto_increment是这么设置的
        Table('fileStorages', metadata,
            Column('id', db.Integer, primary_key=True, nullable=False,autoincrement = True),
            Column('name', db.String(300)),
            Column('data', db.LargeBinary))
        # Implement the creation
        metadata.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    create_table_if_non_exists()
    file = request.files['inputFile']
    print(file)
    newFile = FileContents(name=file.filename,data=file.read())
    save_file_to_disk(file.read(),file.filename)
    db.session.add(newFile)
    db.session.commit()
    logging.error('saving file with file name %s ' % (file.filename,))
    return 'saved '+ file.filename + " to file database"

@app.route('/download',methods=['GET'])
def download():
    file_data = FileContents.query.filter_by(id=2).first()
    return send_file(BytesIO(file_data.data),attachment_filename='lovely.png',as_attachment=True)





def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()