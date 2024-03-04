#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import math
import clipboard
from time import sleep

def genandcopy():
    res = ''.join(format(ord(i), '08b') for i in entry1.get())
    clipboard.copy(res)
    label5.configure(
        background = "#ffffff",
        foreground = "#000000"
    )

class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        toplevel2 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel2.configure(background="#828282", height=400, width=400)
        toplevel2.resizable(False, False)
        toplevel2.title("Generator Binarny")
        label2 = ttk.Label(toplevel2)
        label2.configure(
            anchor="center",
            background="#ffffff",
            font="{Yu Gothic UI Semilight} 16 {bold}",
            foreground="#000000",
            text='WYGENERUJ SOBIE KOD BINARNY\n')
        label2.place(
            anchor="center",
            relheight=0.08,
            relwidth=1.0,
            relx=0.5,
            rely=0.04,
            x=0,
            y=0)
        global entry1
        entry1 = ttk.Entry(toplevel2)
        entry1.place(
            anchor="center",
            relwidth=0.95,
            relx=0.5,
            rely=0.24,
            x=0,
            y=0)
        label4 = ttk.Label(toplevel2)
        label4.configure(
            anchor="center",
            background="#ffffff",
            font="{Yu Gothic UI Semilight} 10 {bold}",
            foreground="#000000",
            text='Wpisz tekst który chcesz wygenerować w kodzie binarnym')
        label4.place(
            anchor="center",
            relwidth=1.0,
            relx=0.5,
            rely=0.15,
            x=0,
            y=0)
        button1 = ttk.Button(toplevel2)
        button1.configure(text='GENERUJ I KOPIUJ DO SCHOWKA', command = genandcopy)
        button1.place(
            anchor="center",
            relheight=0.25,
            relwidth=0.58,
            relx=0.5,
            rely=0.47,
            x=0,
            y=0)
        global label5
        label5 = ttk.Label(toplevel2)
        label5.configure(
            anchor="center",
            background="#828282",
            font="{Yu Gothic UI Semilight} 12 {bold}",
            foreground="#828282",
            text='Twój kod binarny został skopiowany do schowka')
        label5.place(
            anchor="center",
            relheight=0.16,
            relwidth=1.0,
            relx=0.5,
            rely=0.75,
            x=0,
            y=0)
        toplevel2.pack_propagate(0)

        # Main widget
        self.mainwindow = toplevel2

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = NewprojectApp()
    app.run()
