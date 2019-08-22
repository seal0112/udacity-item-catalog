from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CatalogItem, User

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def showCatalog():
    return "Catalog Page"


@app.route('/catalog/<category>/items')
def showCatagories(category):
    return "Catalog Page"

@app.route('/catalog/<category>/<catalogItem>')
def showCategoryItems():
    return "Category Item"

# JSON APIs to view Restaurant Information
@app.route('/catalog/categories/JSON')
def CategoriesJSON():
    categories = session.query(Category).all()
    return jsonify(category=[category.serialize for category in categories])

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
