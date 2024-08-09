from tkinter import Tk, Button, Label
import time

def buton_tikla():
    try:
        with open("sonuc.txt", "r", encoding="utf-8") as dosya:
            x = dosya.read()
        label.config(text=x)
    except FileNotFoundError:
        label.config(text="Dosya bulunamadı.")
    except IOError:
        label.config(text="Dosya okunurken bir hata oluştu.")

root = Tk()
button = Button(root, text="Dosyayı Oku", command=buton_tikla)
button.pack()
label = Label(root, text="Burada dosya içeriği gösterilecek.")
label.pack()
root.mainloop()