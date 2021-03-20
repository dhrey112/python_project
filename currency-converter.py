import requests
from tkinter import *
from tkinter import ttk
import tkinter as tk


# Create the currency Convert class

class currency_converter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rate']


def convert(self, from_currency, to_currency, amount):
    initial_amount = amount
    # first convert it into USD if it is not in USD.
    # because our base currency is USD
    if from_currency != 'USD':
        amount = amount / self.currencies[to_currency]

    # limiting the precision to 4 decimal places
    amount = round(amount * self.currencies[to_currency], 4)
    return amount

