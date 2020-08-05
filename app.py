from flask import Flask, Blueprint, render_template, redirect, request
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

from models.book import Book
from models.author import Author


app = Flask(__name__)









@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)