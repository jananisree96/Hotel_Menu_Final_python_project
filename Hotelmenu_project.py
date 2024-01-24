#Hotel Menu:

import time
import datetime
from PIL import Image

class Menu:
    def __init__(self):
        print("                    *                    ")
        print("                   * *                   ")
        print("                  * * *                  ")
        print("    WELCOME TO AROMA PURE VEG RESTAURANT ")
        print("                  * * *                  ")
        print("                   * *                   ")
        print("                    *                    ")
        print("Please be aware that once an order has been placed, it cannot be canceled or replaced.")
        print()
        x = datetime.datetime.now()
        print("Today Date and time:", x)
        x1 = Image.open("D:/Hotelmenu_finalpro/logo1.png")
        size = (1080, 720)
        edit = x1.resize(size)
        edit.show()

    def place_order(self):
        print("What do you want to place order? Breakfast or Dinner?")
        meal = input("If you want Breakfast type 'M', if you want Dinner type 'N': ").upper()

        if (meal == 'M'):
            self.morning()
        elif (meal == 'N'):
            self.night()
        else:
            print("Invalid choice. Please enter 'M' for Breakfast or 'N' for Dinner.")
    def morning(self):
        print("Today Breakfast Menu::\n 1--Idli \n 2--Dosa \n 3--Venpongal \n 4--Poori\n")
        time.sleep(1)
        ch = int(input("What do u want? Select no--(1 to 4) and place your order"))
        if (ch == 1):
            print("You are selected Idli")
            from PIL import Image
            x2=Image.open("D:/Hotelmenu_finalpro/idly.png")
            x2.show()
            qty = int(input("How many plates do you want? Each plate-50--"))
            rate = 50
            tot = rate * qty
            print("Total:", tot)
            print("<<Your order has been placed. Thank you, Happy Eating!>>")
        elif (ch == 2):
            print("You are selected Dosa")
            from PIL import Image
            x2=Image.open("D:/Hotelmenu_finalpro/dosa.png")
            x2.show()
            qty = int(input("How many Dosas do you want? Dosa rate-60--"))
            rate = 60
            tot = rate * qty
            print("Total:", tot)
            print("<<Your order has been placed. Thank you, Happy Eating!>>")
        elif (ch == 3):
            print("You are selected Venpongal")
            from PIL import Image
            x2=Image.open("D:/Hotelmenu_finalpro/pongal.png")
            x2.show()
            qty = int(input("How many plates do you want? Each plate-60--"))
            rate = 60
            tot = rate * qty
            print("Total:", tot)
            print("<<Your order has been placed. Thank you, Happy Eating!>>")
        elif (ch == 4):
            print("You are selected Poori")
            from PIL import Image
            x2=Image.open("D:/Hotelmenu_finalpro/poori.png")
            x2.show()
            qty = int(input("How many plates do you want? Each plate-50--"))
            rate = 50
            tot = rate * qty
            print("Total:", tot)
            print("<<Your order has been placed. Thank you, Happy Eating!>>")

    def night(self):
        print("Today Dinner Menu::\n 5--Mushroom Friedrice \n 6--Panner Friedrice \n 7--ButterNaan \n 8--Peaspulao\n")
        time.sleep(1)
        ch = int(input("What do u want? Select no--(5 to 8) and place your order"))
        if (ch == 5):
            print("You are selected mushroom Fried rice")
            from PIL import Image
            x2=Image.open("D:/Hotelmenu_finalpro/mushfry.png")
            x2.show()
            qty = int(input("How many plates do you want? Each plate-160--"))
            rate = 160
            tot = rate * qty
            print("Total:", tot)
            print("<<Your order has been placed. Thank you, Happy Eating!>>")
        elif (ch == 6):
            print("You are selected panner Fried rice")
            from PIL import Image
            x2=Image.open("D:/Hotelmenu_finalpro/pannerfry.png")
            x2.show()
            qty = int(input("How many Panner plates do you want? Each plate-160--"))
            rate = 160
            tot = rate * qty
            print("Total:", tot)
            print("<<Your order has been placed. Thank you, Happy Eating!>>")
        elif (ch == 7):
            print("You are selected butternaan")
            from PIL import Image
            x2=Image.open("D:/Hotelmenu_finalpro/butternaan.png")
            x2.show()
            qty = int(input("How many plates do you want? Each plate-65--"))
            rate = 65
            tot = rate * qty
            print("Total:", tot)
            print("<<Your order has been placed. Thank you, Happy Eating!>>")
        elif (ch == 8):
            print("You are selected peaspulao")
            from PIL import Image
            x2=Image.open("D:/Hotelmenu_finalpro/peaspulao.png")
            x2.show()
            qty = int(input("How many plates do you want? Each plate--50"))
            rate = 50
            tot = rate * qty
            print("Total:", tot)
            print("<<Your order has been placed. Thank you, Happy Eating!>>")

ob = Menu()
n1=int(input("How many orders you want to place?"))
for i in range(n1):
    ob.place_order()
