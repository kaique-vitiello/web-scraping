# Salva tabela do HTML em CSV e importa em um DF

import pandas as pd
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.gov.br/receitafederal/pt-br/assuntos/agenda-tributaria/agenda-tributaria-2021/abril-2021/dia-05-04-2021")
#html = urlopen("https://www.gov.br/receitafederal/pt-br/assuntos/agenda-tributaria/agenda-tributaria-2021/abril-2021/dia-05-04-2021")
bs = BeautifulSoup(html.text, 'html.parser')
# The main comparison table is currently the first table on the page
table = bs.findAll('table',{'class':'listing'})[0]
rows = table.findAll('tr')

csvFile = open('agenda.csv', 'wt+')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()

df = pd.read_csv (r'/home/kvl/git/web_scraping/agenda.csv')
print (df)