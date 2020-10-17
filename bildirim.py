import time
from tkinter import *

saat = int(input("Saat : "))
dakika = int(input("Dakika : "))
yazı = input("Yazıyı giriniz. : ")

while True :
    bildirim = time.localtime(time.time())

    if saat == bildirim.tm_hour and dakika == bildirim.tm_min :
        pencere = Tk()
        pencere.title("Bildirim Sistemi")
        pencere.geometry("250x125+1000+500")
        etiket = Label(text = yazı , font= "Verdana 16")
        etiket.pack()
        pencere.resizable(0,0)
        pencere.mainloop()
        break
    else : 
        pass
