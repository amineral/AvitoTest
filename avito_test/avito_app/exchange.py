import requests
from .config import EXCHANGE_API_KEY, API_HTTP

# TODO: add TTL Cache to values to minimize exchange API requests

def get_exchange():
    params = {
        "app_id" : EXCHANGE_API_KEY,
    }
    response = requests.get(API_HTTP, params=params)
    exchange = response.json()
    values = exchange["rates"]
    return values

values = get_exchange()

def exchange(currency, amount):
    currency = currency.upper()
    if currency in values:
        usd = amount / values[currency]
        to_rub = usd * values["RUB"]
        return to_rub
    return False
