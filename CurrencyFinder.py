import requests
from tkinter import *

def printme():
    value = code.get("1.0", "end-1c")  # Get the country code when the button is clicked
    url = f"https://restcountries.com/v3.1/alpha/{value}"
    name = call_api(url)  # Call the API with the URL
    outputCurrency.config(text=name)  # Update the label with the retrieved currency name

def call_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        data = response.json()  # Parse the response as JSON

        currencies = data[0]['currencies']
        currency_names = []
        for currency_name in currencies:
            name = data[0]['currencies'][currency_name].get("name")
            currency_names.append(name)
        
        return ', '.join(currency_names) if currency_names else "Currency not found"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

window = Tk()
window.title("Currency Converter")
window.geometry('700x300')
window.tk.call('tk', 'scaling', 3.0)

lbl = Label(window, text="Enter the two digit country code:")
lbl.grid(column=0, row=0)

code = Text(window, height=1, width=2)
code.grid(column=1, row=0)

search = Button(window, text="Search", command=printme)  # Removed parentheses
search.grid(column=0, row=3)
cancel = Button(window, text="Cancel", command=window.destroy)
cancel.grid(column=1, row=3)

outputName = Label(window, text="Currency Name")
outputName.grid(column=0, row=2)
outputCurrency = Label(window, text="--")
outputCurrency.grid(column=1, row=2)

window.mainloop()
