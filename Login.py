import requests as r
from bs4 import BeautifulSoup
import pandas as pd



resposta = r.get('https://books.toscrape.com/catalogue/page-1.html')
resposta.encoding = 'utf-8'

soup = BeautifulSoup(resposta.text,'html.parser')



livros = []



for item in soup.select('.product_pod'):
    titulo = item.h3.a['title']
    preco_texto = item.select_one('.price_color').text.strip()
    preco = float(preco_texto.replace('£', '').strip())




    livros.append({'titulo':titulo,'preco':preco})



df = pd.DataFrame(livros)


df_filtrando = df[df['preco']<30]


df_filtrando.to_csv('livros_baratos.csv',index = False)



print("Salvo com sucesso")
print(df_filtrando.head())












