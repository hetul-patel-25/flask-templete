import os
from flask_sqlalchemy import SQLAlchemy
from app import app
from dotenv import load_dotenv

load_dotenv()

user=os.getenv('sql_user')
password=os.getenv('sql_password')
host=os.getenv('sql_host')
database=os.getenv('sql_database')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']="7894556123"

sql_db = SQLAlchemy(app)