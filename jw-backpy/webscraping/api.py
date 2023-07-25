from flask import Blueprint, jsonify, request
from webscraping.web_scraping import get_reunioes

# Criar uma instância de Blueprint
api_app = Blueprint('api', __name__)

@api_app.route('/reunioes', methods=['GET'])
def reunioes():
    # Obtendo os parâmetros da query string na URL
    urlEnv = request.args.get('urlEnv')
    NomeEV = request.args.get('NomeEnV')
    mesEnv = request.args.get('mesEnV')

    if not urlEnv or not NomeEV or not mesEnv:
        return jsonify({'message': 'Parâmetros urlEnv, NomeEnV e mesEnv são obrigatórios'}), 400

    # Chamar a função get_reunioes() com os parâmetros recebidos
    reunioes_list = get_reunioes(urlEnv, NomeEV, mesEnv)
    
    # Serializar a lista de objetos Reuniao em formato JSON
    reunioes_json = [reuniao.__dict__ for reuniao in reunioes_list]

    if reunioes_list:
        return jsonify(reunioes_json)
    else:
        return jsonify({'message': 'Falha ao obter reuniões'}), 500
