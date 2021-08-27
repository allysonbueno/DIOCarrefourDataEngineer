# tecnica para coletar dados da web, minteração atraves de extração de dados de sites
from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/278/maringa-pr').content
# content para pegar o conteudo e retornar com o get
# objeto site recebendo o conteudo da req http do site

soup = BeautifulSoup(site,'html.parser')
# objeto soup baixando do site o html

# print(soup.prettify())
# pretify transforma o html em string e o print vai exibir o html

trecho = '-gray-light'
temperatura = soup.find('span', class_ = trecho)
print(temperatura)