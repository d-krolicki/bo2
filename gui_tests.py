# WERSJA TESTOWA - coś tam wypisuje ale nie za wiele

import tkinter as tk
from tkinter import filedialog

# Set window
window = tk.Tk()
window.geometry('600x550')

# Set labels
tk.Label(text="Parametry:", fg="black", bg="white", font=15).place(relx=0.1, rely=0.1)
tk.Label(text="Prawdopodobieństwo:", fg="black", bg="white", font=('Arial', 12)).place(relx=0.1, rely=0.2)
tk.Label(text="Mutacji 1", fg="black", bg="white").place(relx=0.1, rely=0.25)
tk.Label(text="Mutacji 2", fg="black", bg="white").place(relx=0.1, rely=0.3)
tk.Label(text="Mutacji 3", fg="black", bg="white").place(relx=0.1, rely=0.35)
tk.Label(text="Krzyżowania", fg="black", bg="white").place(relx=0.1, rely=0.4)
tk.Label(text="Liczebność populacji", fg="black", bg="white").place(relx=0.5, rely=0.2)
tk.Label(text="Liczba iteracji", fg="black", bg="white").place(relx=0.5, rely=0.28)
aa = tk.Label(text="Hurtownie")
aa.place(relx=0.4, rely=0.6)

# Inputs
wid_m1 = tk.Entry(fg="black", bg="white", width=8)
wid_m2 = tk.Entry(fg="black", bg="white", width=8)
wid_m3 = tk.Entry(fg="black", bg="white", width=8)
wid_k = tk.Entry(fg="black", bg="white", width=8)
wid_pop = tk.Entry(fg="black", bg="white", width=8)
wid_it = tk.Entry(fg="black", bg="white", width=8)
wid_m1.place(relx=0.23, rely=0.25)
wid_m2.place(relx=0.23, rely=0.3)
wid_m3.place(relx=0.23, rely=0.35)
wid_k.place(relx=0.23, rely=0.4)
wid_pop.place(relx=0.7, rely=0.2)
wid_it.place(relx=0.7, rely=0.28)

# Actions
global params
global hurtownie
global cars
global products


def get_params() -> None:
    # Będzie można to pominąć i mieć cały czas dostęp do tych paramterów pod postacią x.get()
    m1 = wid_m1.get()
    m2 = wid_m2.get()
    m3 = wid_m3.get()
    k = wid_k.get()
    pop = wid_pop.get()
    it = wid_it.get()
    params = [m1, m2, m3, k, pop, it]


# Reading .txt files
def browser_wholsel():
    hurtownie = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                           filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    # if hurtownie:
    #     with open(hurtownie, mode="r", encoding="utf-8") as input_file:
    #         for line in input_file.readlines():
    #             print(line)
    aa.configure(text='Filepath:'+hurtownie)


# Buttons
get_paramsB = tk.Button(window, text='Zapisz parametry', command=get_params)
get_paramsB.place(relx=0.5, rely=0.4)
get_whols = tk.Button(window, text='Wgraj hurtownie', command=browser_wholsel)
get_whols.place(relx=0.2, rely=0.6)
get_whols = tk.Button(window, text='Wgraj samochody', command=browser_wholsel)
get_whols.place(relx=0.2, rely=0.7)
get_whols = tk.Button(window, text='Wgraj produkty', command=browser_wholsel)
get_whols.place(relx=0.2, rely=0.8)

window.mainloop()
