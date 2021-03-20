import requests
from tkinter import *
from tkinter import ttk
import tkinter as tk


# Create the currency Convert class

class CurrencyConverter():
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


# create the UI class
class CurrencyConverterUI(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter

        # Let create the converter
        self.geometry('500x200')

        self.intro_label = Label(self, text='Welcome to Real Time Currency Convertor', fg='blue', relief=tk.RAISED,
                                 borderwidth=3)
        self.intro_label.config(font=('Courier', 15, 'bold'))
        self.date_label = Label(self,
                                text=f"1 Nigerian Naira equals = {self.currency_converter.convert('NRA', 'USD', 1)} USD \n Date : {self.currency_converter.data['date']}",
                                relief=tk.GROOVE, borderwidth=5)

        self.intro_label.place(x=10, y=5)
        self.date_label.place(x=170, y=50)

        # Entry Box
        valid = (self.register(self.restrictNumberOnly), '%d', '%p')
        # restricNumberOnly function will restrict thes user to enter invavalid number in Amount field. We will define it later in code
        self.amount_field = Entry(self, bd = 3, relief = tk.RIDGE, justify = tk.CENTER, validate = 'key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text = "", fg = 'black', bg='red', relief = tk.RIDGE, justify=tk.CENTER, width = 17, borderwidth = 3)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("NRN")



    def RealTimeCurrencyConverter(self, action, string):
        regrex = re.compile(r"[0-9]*?(\.)?[0-9,]*$")
        result = regrex.match(string)
        return (string == "" or (string.count(.) <= 1 and result is not None))


if __name__ == '__main':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
    App(converter)
    mainloop()
