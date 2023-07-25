# pacote1/web_scraping.py

import requests
from bs4 import BeautifulSoup
import calendar
import datetime


class Reuniao:
    def __init__(self, semana, livro, canticoInicial, tesouro, perguntaJoias, leituraSemana, canticoMeio, nvcP1, nvcP2, estudo, canticoFinal):
        self.semana = semana
        self.livro = livro
        self.canticoInicial = canticoInicial
        self.tesouro = tesouro
        self.perguntaJoias = perguntaJoias
        self.leituraSemana = leituraSemana
        self.canticoMeio = canticoMeio
        self.nvcP1 = nvcP1
        self.nvcp2 = nvcP2
        self.estudo = estudo
        self.canticoFinal = canticoFinal


def obter_qtd_segundas_feiras(ano, mes):
    _, dias_no_mes = calendar.monthrange(ano, mes)
    qtd_segundas_feiras = 0

    for dia in range(1, dias_no_mes + 1):
        # weekday() retorna o dia da semana, sendo 0 para segunda-feira e 6 para domingo
        if calendar.weekday(ano, mes, dia) == 0:  # 0 representa segunda-feira
            qtd_segundas_feiras += 1

    return qtd_segundas_feiras


def get_reunioes(urlEnv, nomeEnv, mesEnv):

    filename = nomeEnv
    urlEnviada = urlEnv
    reunioes_list = []

    # Pega a Semana que está na URL
    urlSplit = urlEnviada.split("/")
    semanas = urlSplit[len(urlSplit) - 1]

    # Variaveis utilizadas para os For e montar a Url novamente
    tamanhoURL = len(urlSplit)
    x = int(semanas)
    ## y = obter_qtd_segundas_feiras(datetime.datetime.now().year, mesEnv) + x
    y = x +5 
    base_url = ''
    

    for v in range(0, tamanhoURL-1):
        if v == 0:
            base_url = base_url + urlSplit[v]
        else:
            base_url = base_url + "/" + urlSplit[v]

    while x < y:

        url = base_url + "/" + str(x)
        print("Criando semana: " + str(x))

        x = x + 1
        # Fazendo a solicitação HTTP
        response = requests.get(url)

        # Verificando se a solicitação foi bem-sucedida
        if response.status_code == 200:

            # Analisando o HTML com BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Procurando a div com a classe "todayitem"
            pag = soup.find("div", class_="todayItem")

            # Extraindo o texto da div
            text = pag.get_text()

            verificaSemana = soup.find(id="p1")
            if verificaSemana != None:
                semana = soup.find(id="p1").get_text() 
                livro = soup.find(id="p2").get_text()
                canticoInicial = soup.find(id="p3").get_text()
                tesouro = soup.find(id="p6").get_text().split('(')
                perguntaJoias = soup.find(id="p8").get_text()
                leituraSemana = soup.find(id="p12").get_text().split(')')
                canticoMeio = soup.find(id="p18").get_text()
                nvcP1temp = soup.find(id="p19").get_text().split('(')
                
                
                p20_element = soup.find(id="p20")
                if p20_element and "<div class=\"gen-field\" id=\"p20\" data-pid=\"20\">" in str(p20_element):
                    nvcP2temp = "null"
                else:
                    nvcP2temp = soup.find(id="p20").get_text().split('(')
                
                
                # Buscar o último texto que contém "Cântico" na página
                for tag in soup.find_all(text=lambda text: "Cântico" in text):
                    canticoFinal = tag

                # Buscar o último texto que contém "Estudo bíblico de congregação" na página
                for tag in soup.find_all(text=lambda text: "Estudo bíblico de congregação" in text):
                    estudo = tag
                
                
                ## estudo = soup.find(id="p21").get_text()
                ## canticoFinal = soup.find(id="p23")
                nvcP1 = nvcP1temp[0]
                nvcP2 = nvcP2temp[0]
            
            reuniao = Reuniao(semana, livro, canticoInicial, tesouro, perguntaJoias, leituraSemana, canticoMeio, nvcP1, nvcP2, estudo, canticoFinal)
            reunioes_list.append(reuniao)

    return reunioes_list
