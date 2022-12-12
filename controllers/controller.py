from flask import render_template, request, redirect
from app import app
from models.books import books, add_new_book, remove_book_at_index
from models.book import *

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books', methods=['POST'])
def add_book():
  title = request.form['title']
  author = request.form['author']
  genre = request.form['genre']
  new_book = Book(title=title, author=author, genre=genre)
  add_new_book(new_book)
  return redirect('/books')

@app.route('/books/remove/<index>', methods=['POST'])
def remove(index):
  remove_book_at_index(int(index))
  return redirect('/books')

@app.route('/books/<index>')
def show(index):
    return render_template('book.html', title='Home', book= books[int(index)])


