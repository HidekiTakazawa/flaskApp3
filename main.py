# coding: UTF-8
from flask import Flask, render_template, request, url_for, redirect
from google.appengine.ext import db
from google.appengine.ext.db import Key
app = Flask(__name__)

class BooksData(db.Model):
    bookname = db.StringProperty()
    author = db.StringProperty()
    publisher = db.StringProperty()
    purchasedate = db.StringProperty()
    price = db.StringProperty()
    memo = db.StringProperty()
@app.route('/')
def toppage():
    
    return render_template('toppage.html')
    
@app.route('/database_new', methods=['get', 'post'])
def database_new():
    
    bookname = request.form['bookname']
    author = request.form['author']
    publisher = request.form['publisher']
    purchasedate = request.form['purchasedate']
    price = request.form['price']
    memo = request.form['memo']
    bookdata = BooksData(bookname=bookname, author=author, publisher=publisher, purchasedate=purchasedate, price=price, memo=memo)
    bookdata.put()
    return render_template('databaseAdd.html', bookname=bookname, author=author, publisher=publisher, purchasedate=purchasedate, price=price,memo=memo)
@app.route('/database_all', methods=['get', 'post'])
def database_all():
    #booksData = BooksData.query().fetch()
    booksData = db.GqlQuery("Select * from BooksData")
    return render_template('databaseAll.html', booksData=booksData)
@app.route('/<int:id>/database_delete', methods=( 'post',))
def database_delete(id):
    db.delete(id)
    return redirect(url_for('main.database_all'))
    