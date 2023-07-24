# pacote1/web_scraping.py

import requests
from bs4 import BeautifulSoup

def get_news():
    url = 'https://example.com/news'  # Substitua pela URL do site de notícias que você deseja raspar
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_list = []

        # Aqui você pode utilizar o BeautifulSoup para extrair informações específicas do site, como títulos, links, etc.
        # Exemplo:
        for news_item in soup.find_all('div', class_='news-item'):
            title = news_item.find('h2').text
            link = news_item.find('a')['href']
            news_list.append({'title': title, 'link': link})

        return news_list

    return None
