from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server

app = server.app, server.api

books_db = [
    {'id': 0, 'title': 'The Boat'}
    {'id': 1, 'title': 'Clean Code'}
]


@api.route('/books') #decorator
class BookList(Resource):
    def get(self, ):
        return books_db