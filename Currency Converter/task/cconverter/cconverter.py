import json
import requests


class ConicoinConverter:
    def __init__(self):
        self.currency = None
        self.exchange_rates = None
        self.cache = {}
        self.get_currency()
        self.get_exchange_rate()
        self.save_rate(code="usd")
        self.save_rate(code="eur")
        self.convert()

    def get_currency(self):
        self.currency = input().lower()

    def get_exchange_rate(self):
        self.exchange_rates = json.loads(requests.get(url=f"http://www.floatrates.com/daily/{self.currency}.json").text)

    def save_rate(self, code):
        if code == self.currency:
            return
        self.cache.update({code: self.exchange_rates[code]["rate"]})

    def convert(self):
        while True:
            code = input().lower()
            if code == "":
                return
            amount = float(input())
            print("Checking the cache...")
            if code in self.cache:
                print("Oh! It is in the cache!")
                print(f"You received {round(self.cache[code] * amount, ndigits=2)} {code.upper()}.")
            else:
                self.save_rate(code=code)
                print("Sorry, but it is not in the cache!")
                print(f"You received {round(self.cache[code] * amount, ndigits=2)} {code.upper()}.")


calculator = ConicoinConverter()
