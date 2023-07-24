# main.py

from webscraping.api import app as api_app
from flask import Flask

app = Flask(__name__)

# Outras rotas e configurações do seu aplicativo React podem ser adicionadas aqui

if __name__ == '__main__':
    app.run()
