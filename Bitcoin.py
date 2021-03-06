import requests
import tkinter as tk
from datetime import datetime

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,GBP"
    response = requests.get(url).json()
    price = response["GBP"]
    price2 = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice2.config(text = "£" + str(price)  )
    labelPrice.config(text = str(price2) + " $")
    labelTime.config(text = "Updated at: " + time)

    canvas.after(1000, trackBitcoin)

canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Bitcoin Tracker")

f1 = ("poppns", 24, "bold")
f2 = ("poppns", 22, "bold")
f3 = ("poppns", 18, "normal")

label = tk.Label(canvas, text = "Bitcoin Price", font = f1)
label.pack(pady = 20)

labelPrice = tk.Label(canvas, font = f2)
labelPrice.pack(pady = 20)

labelPrice2 = tk.Label(canvas, font = f2)
labelPrice2.pack(pady = 20)

labelTime = tk.Label(canvas, font = f3)
labelTime.pack(pady = 20)

trackBitcoin()

canvas.mainloop()
