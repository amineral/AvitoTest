import requests
from cachetools import TTLCache
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

def exchange(currency, amount):
    currency = currency.upper()
    if currency in cache["values"]:
        usd = amount / cache["values"][currency]
        to_rub = usd * cache["values"]["RUB"]
        return to_rub
    return False

# minimize requests to exchange API
# with caching currency values for 3600 sec
# if KeyError exception then updating our cache

cache = TTLCache(maxsize=2, ttl=3600)
try: 
    cache["values"]
except KeyError:
    cache["values"] = get_exchange()