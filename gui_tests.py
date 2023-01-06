import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.scrolledtext as st
from tkinter import *

# Set window
root = tk.Tk()
root.title('Sklep')
# root.resizable(width=False, height=False)  # rozmiar okna jest stały

window_height = 500
window_width = 1200
root.geometry("{}x{}".format(window_width, window_height))


def center_screen():
    """ gets the coordinates of the center of the screen """
    global screen_height, screen_width, x_cordinate, y_cordinate

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


center_screen()

# Icon
root.iconbitmap('diagram_v2_29.ico')

# Set Azure style
style = ttk.Style(root)
root.tk.call('source', 'azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground='white')

# Variables
global params
global hurtownie
global cars
global products
global distances
hurtownie = 0
cars = 0
products = 0
distances = 0
m1P = tk.IntVar()
m2P = tk.IntVar()
m3P = tk.IntVar()
kP = tk.IntVar()
popSize = tk.IntVar()
iterations = tk.IntVar()
wData = tk.IntVar()
cData = tk.IntVar()
pData = tk.IntVar()


def get_params() -> None:
    # Będzie można to pominąć i mieć cały czas dostęp do tych paramterów pod postacią x.get()
    # Ale chyba lepiej zostać przy zmiennych globalnych
    global params

    m1 = inM1.get()
    m2 = inM2.get()
    m3 = inM3.get()
    k = inK.get()
    pop = inPop.get()
    it = inIt.get()
    params = [m1, m2, m3, k, pop, it]


# Frames
paramsFrame = ttk.LabelFrame(root, text='Parametry', width=250, height=360)
paramsFrame.place(x=400, y=12)
propFrame = ttk.LabelFrame(paramsFrame, text='Prawdopodobieństwo', width=200, height=215)
propFrame.place(x=20, y=15)
dataFrame = ttk.LabelFrame(root, text='Dane', width=355, height=480)
dataFrame.place(x=20, y=12)
algoFrame = ttk.LabelFrame(root, text='Algorytm', width=250, height=100)
algoFrame.place(x=400, y=390)

# Labels
ttk.Label(propFrame, text="Mutacji 1").place(x=20, y=15)
ttk.Label(propFrame, text="Mutacji 2").place(x=20, y=62)
ttk.Label(propFrame, text="Mutacji 3").place(x=20, y=109)
ttk.Label(propFrame, text="Krzyżowania").place(x=20, y=156)
ttk.Label(paramsFrame, text="Liczebność\npopulacji").place(x=40, y=245)
ttk.Label(paramsFrame, text="Liczba iteracji").place(x=40, y=303)
pathW = tk.Label(dataFrame, text="Filepath:")
pathW.place(x=160, y=20)
pathC = tk.Label(dataFrame, text="Filepath:")
pathC.place(x=160, y=65)
pathP = tk.Label(dataFrame, text="Filepath:")
pathP.place(x=160, y=110)
pathD = tk.Label(dataFrame, text="Filepath:")
pathD.place(x=160, y=155)

# Inputs
inM1 = ttk.Entry(propFrame, width=8)
inM1.place(x=110, y=8)
inM2 = ttk.Entry(propFrame, width=8)
inM2.place(x=110, y=55)
inM3 = ttk.Entry(propFrame, width=8)
inM3.place(x=110, y=102)
inK = ttk.Entry(propFrame, width=8)
inK.place(x=110, y=149)
inPop = ttk.Entry(paramsFrame, width=8)
inPop.place(x=130, y=245)
inIt = ttk.Entry(paramsFrame, width=8)
inIt.place(x=130, y=295)

# Notebook
notebook = ttk.Notebook(dataFrame)
notebook.place(x=20, y=250)

# karty w notatniku
tabW = ttk.Frame(notebook, width=150, height=150)
notebook.add(tabW, text='Hurtownie')
tabC = ttk.Frame(notebook, width=150, height=150)
notebook.add(tabC, text='Samochody')
tabP = ttk.Frame(notebook, width=150, height=150)
notebook.add(tabP, text='Produkty')
tabD = ttk.Frame(notebook, width=150, height=150)
notebook.add(tabD, text='Dystanse')

# scrolled texts
scrtextW = st.ScrolledText(tabW, width=45, height=10, state='disabled')
scrtextW.pack()
scrtextC = st.ScrolledText(tabC, width=45, height=10, state='disabled')
scrtextC.pack()
scrtextP = st.ScrolledText(tabP, width=45, height=10, state='disabled')
scrtextP.pack()
scrtextD = st.ScrolledText(tabD, width=45, height=10, state='disabled')
scrtextD.pack()


# Reading .txt files
def browser_wholsel():
    global hurtownie
    hurtownie = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                           filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    if hurtownie:
        with open(hurtownie, mode="r", encoding="utf-8") as input_file:
            scrtextW.configure(state='normal')
            scrtextW.delete(1.0, END)
            for line in input_file.readlines():
                scrtextW.insert(tk.INSERT, line)
            scrtextW.configure(state='disabled')
    pathW.configure(text='Filepath:' + hurtownie)


def browser_cars():
    global cars
    cars = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                      filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    if cars:
        with open(cars, mode="r", encoding="utf-8") as input_file:
            scrtextC.configure(state='normal')
            for line in input_file.readlines():
                scrtextC.insert(tk.INSERT, line)
            scrtextC.configure(state='disabled')
    pathC.configure(text='Filepath:' + cars)


def browser_products():
    global products
    products = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    if products:
        with open(products, mode="r", encoding="utf-8") as input_file:
            scrtextP.configure(state='normal')
            for line in input_file.readlines():
                scrtextP.insert(tk.INSERT, line)
            scrtextP.configure(state='disabled')
    pathP.configure(text='Filepath:' + products)


def browser_distances():
    global distances
    distances = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                           filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    if distances:
        with open(distances, mode="r", encoding="utf-8") as input_file:
            scrtextD.configure(state='normal')
            for line in input_file.readlines():
                scrtextD.insert(tk.INSERT, line)
            scrtextD.configure(state='disabled')
    pathD.configure(text='Filepath:' + distances)


def browser_all():
    global hurtownie, cars, products, distances
    if not hurtownie:
        with open('Data/Hurtownie.txt', mode="r", encoding="utf-8") as input_file:
            scrtextW.configure(state='normal')
            for line in input_file.readlines():
                scrtextW.insert(tk.INSERT, line)
            scrtextW.configure(state='disabled')
    pathW.configure(text='Filepath: ' + 'Data/hurtownie.txt')

    if not cars:
        with open('Data/cars.txt', mode="r", encoding="utf-8") as input_file:
            scrtextC.configure(state='normal')
            for line in input_file.readlines():
                scrtextC.insert(tk.INSERT, line)
            scrtextC.configure(state='disabled')
    pathC.configure(text='Filepath: ' + 'Data/cars.txt')

    if not products:
        with open('Data/Produkty.txt', mode="r", encoding="utf-8") as input_file:
            scrtextP.configure(state='normal')
            for line in input_file.readlines():
                scrtextP.insert(tk.INSERT, line)
            scrtextP.configure(state='disabled')
    pathP.configure(text='Filepath: ' + 'Data/produkty.txt')

    if not distances:
        with open('Data/distances.txt', mode="r", encoding="utf-8") as input_file:
            scrtextD.configure(state='normal')
            for line in input_file.readlines():
                scrtextD.insert(tk.INSERT, line)
            scrtextD.configure(state='disabled')
    pathD.configure(text='Filepath: ' + 'Data/distances.txt')


# Buttons
get_wholB = ttk.Button(dataFrame, text='Wgraj hurtownie', style='Accentbutton', command=browser_wholsel, width=16)
get_wholB.place(x=20, y=15)
get_carsB = ttk.Button(dataFrame, text='Wgraj samochody', style='Accentbutton', command=browser_cars, width=16)
get_carsB.place(x=20, y=60)
get_prodB = ttk.Button(dataFrame, text='Wgraj produkty', style='Accentbutton', command=browser_products, width=16)
get_prodB.place(x=20, y=105)
get_distB = ttk.Button(dataFrame, text='Wgraj dystanse', style='Accentbutton', command=browser_distances, width=16)
get_distB.place(x=20, y=150)
get_all = ttk.Button(dataFrame, text='Wgraj automatycznie', style='Accentbutton', command=browser_all)
get_all.place(x=20, y=195)
startAlgoB = ttk.Button(algoFrame, text='Uruchom algorytm', style='Accentbutton', command=get_params)
startAlgoB.place(x=60, y=45)


# Radiobuttons
radio1 = ttk.Radiobutton(algoFrame, text='Algorytm 1',  value=1)
radio1.place(x=10, y=5)
radio2 = ttk.Radiobutton(algoFrame, text='Algorytm 2',  value=2)
radio2.place(x=130, y=5)

root.mainloop()
