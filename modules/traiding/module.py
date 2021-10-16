import requests
from bs4 import BeautifulSoup
from modules.base_module import BaseModule
from binance import Client



class Trading_info(BaseModule):
    def run(self, update, context):
        # client = Client()
        resp = requests.get(url='https://ria.ru/location_rossiyskaya-federatsiya/', headers=[])
        advice = (BeautifulSoup(resp.text).
                    find('a', {'class': 'list-item__title color-font-hover-only'}).
                    text)
        url = (BeautifulSoup(resp.text).
                    find('a', {'class': 'list-item__title color-font-hover-only'}).
                    attrs["href"])

        self.send(update, context, "📰 "+ advice + ' ' + url)


# traiding_info_module = Trading_info()