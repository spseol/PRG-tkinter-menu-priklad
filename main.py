#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk

from datetime import datetime


zacatek = datetime.now()
print(zacatek)

globalni = 10


def abc():
    global globalni
    globalni = 20
    print(globalni)


abc()
print(globalni)

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.geometry("500x500")
        self.lbl = tk.Label(self, text="Hello World")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.btn2 = tk.Button(self, text="About", command=self.about)
        self.btn2.pack()

        self.menuHlavni = tk.Menu(self, tearoff=0)

        self.menuSoubor = tk.Menu(self.menuHlavni, tearoff=0)
        self.menuSoubor.add_command(label="Otevřít", command=self.hello)
        self.menuSoubor.add_command(label="Uložit", command=self.hello)
        self.menuSoubor.add_separator()
        self.menuSoubor.add_command(label="Pryč", command=self.quit)

        self.onoff = tk.BooleanVar()
        self.menuSoubor.add_checkbutton(
            label="On/Off", variable=self.onoff, command=self.hello
        )
        self.menuSoubor.add_separator()

        self.cisla = tk.IntVar()
        self.menuSoubor.add_radiobutton(label="jenda", value=1, variable=self.cisla)
        self.menuSoubor.add_radiobutton(label="dva", value=2, variable=self.cisla)
        self.menuSoubor.add_radiobutton(label="tri", value=3, variable=self.cisla)
        self.menuHlavni.add_cascade(label="Soubor", menu=self.menuSoubor)

        self.menuBla = tk.Menu(self.menuHlavni)
        self.menuBla.add_command(label="Beee", command=self.hello)
        self.menuBla.add_cascade(label="podmenu", menu=self.menuSoubor)
        self.menuBla.add_command(label="Buuuu", command=self.hello)
        self.menuHlavni.add_cascade(label="Bla", menu=self.menuBla)

        self.bind("<Button-3>", self.showMenu)

        # zobrazení menu
        self.config(menu=self.menuHlavni)

    def showMenu(self, event=None):
        # print(dir(event))
        print(event.x, event.y)
        print(event.x_root, event.y_root)
        self.menuHlavni.post(event.x_root, event.y_root)

    def about(self):
        pass

    def hello(self):
        print(self.onoff.get())
        print(self.cisla.get())

    def quit(self, event=None):
        super().quit()


app = Application()

app.mainloop()

konec = datetime.now()
print(konec)
print(konec - zacatek)
