import json
import requests
from config import *


class ExchangeException(Exception):
    pass


class Exchange:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ExchangeException(f'Нельзя конвертировать одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ExchangeException(f'Ошибка ввода: Валюты {quote} не существует, посмотреть список доступных для конвертации валют /values')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ExchangeException(f'Ошибка ввода: Валюты {base} не существует, посмотреть список доступных для конвертации валют /values')

        try:
            amount = int(amount)
        except ValueError:
            raise ExchangeException(f'Не могу обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base = total_base * amount
        return total_base
