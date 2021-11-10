from flask import Flask, request
from bs4 import BeautifulSoup
import lxml

class art:
    def scrapInformation(slef, nameOfcurrency):
        URL = 'https://coinmarketcap.com/alexandria/article/i-lost-everything-how-squid-game-token-collapsed'/nameOfcurrency/'news'
        r = request.get(URL, 'html.parcel').text
        soup = BeautifulSoup(r, 'lxml') 
        header = soup.h2.text

        print(header, '\n')

        article = soup.text.strip()

        print()
        print('-------------------------------------')
        print('\n\n\n')