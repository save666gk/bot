import json
from config import keys
import requests


class ConvertionExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert( quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionExeption(' Конвертирование  одинаковых валют ')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f' Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f' Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f' Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base