import json

import requests


response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
data = response.json()


rate = float(data[0]["Rate"])
rate2=float(data[1]["Rate"])

date = data[0]["Date"]
date2 = data[1]["Date"]

while True:
    print("""
    ---Menyu---
    1.So'm->Dollar
    2.Dollar->So'm
    3.So'm->EURO
    4.EURO->So'm
    5.Exit
    """
    )

    choice = input("Tanlov: ")


    if choice == "1":
        amount = float(input("So‘m miqdorini kiriting: "))
        usd = amount / rate
        print(f"{amount:,.2f} so‘m = {usd:.2f} USD ({date})")
    elif choice == "2":
        amount = float(input("Dollar miqdorini kiriting: "))
        som = amount * rate
        print(f"{amount:.2f} USD = {som:,.2f} so‘m ({date})")
    elif choice == "3":
        amount = float(input("So‘m miqdorini kiriting: "))
        euro = amount / rate2
        print(f"{amount:,.2f} so‘m = {euro:.2f} EURO ({date2})")
    elif choice == "4":
        amount = float(input("EURO miqdorini kiriting: "))
        som = amount * rate2
        print(f"{amount:.2f} EURO = {som:,.2f} so‘m ({date2})")
    elif choice == "5":
        break
    else:
        print("Noto‘g‘ri tanlov!")