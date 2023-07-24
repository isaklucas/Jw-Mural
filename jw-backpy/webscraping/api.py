# jw-backpy/webscraping/api.py

from webscraping.web_scraping import get_news
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/news')
def news():
    news_list = get_news()
    if news_list:
        return jsonify(news_list)
    else:
        return jsonify({'message': 'Falha ao obter notícias'}), 500
