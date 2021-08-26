#instancia da aplicação

from flask import Flask
from flask_restplus import Api  

class Server(): #criacao classe Server
    def __init__(self, ): 
        self.app = Flask(__name__) #app Flask
        self.api = Api(self.app,    #objeto Api onde terá os controllers
            version='1.0',
            title='Sample Book API',
            description='A simple book API',
            doc='/docs' #url documentação
        )

def run(self, ):   #metodo para startar o server
    self.app.run(
        debug=True
    )

server = Server()