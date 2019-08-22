from flask import Flask
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CatalogItem, User

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

@app.route('/')
def showCatalog():
    return 'haha'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
