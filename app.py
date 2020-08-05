from flask import Flask, Blueprint, render_template, redirect, request
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

from models.book import Book
from models.author import Author


app = Flask(__name__)

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template('books/index.html', books=books)


@books_blueprint.route("/books/<id>/delete", methods = ['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")

@books_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", authors=authors)

@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    author_id =request.form['author_id']
    author = author_repository.select(author_id)
    new_book = Book(title, author, genre)
    book_repository.save(new_book)
    return redirect("/books")

app.register_blueprint(books_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)