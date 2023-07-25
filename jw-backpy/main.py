from flask import Flask
from webscraping.api import api_app

app = Flask(__name__)

# Registrar o blueprint do arquivo api.py na instância do Flask criada em main.py
app.register_blueprint(api_app, url_prefix='/api')

# Outras rotas e configurações do seu aplicativo React podem ser adicionadas aqui

if __name__ == '__main__':
    app.run()
