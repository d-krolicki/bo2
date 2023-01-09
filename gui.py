import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.scrolledtext as st
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# matplotlib.use("TkAgg")

from algorithm import *


class GUI:
    def __init__(self, root):
        # =============================GENERAL SETTINGS=========================================
        self.shop = Shop()
        self.root = root
        root.title('Sklep')

        self.window_height = 550
        self.window_width = 1200
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (self.window_width / 2))
        y_cordinate = int((screen_height / 2) - (self.window_height / 2))
        self.root.geometry("{}x{}".format(self.window_width, self.window_height, x_cordinate, y_cordinate))

        # Icon
        self.root.iconbitmap('diagram_v2_29.ico')

        # Set Azure style
        style = ttk.Style(root)
        self.root.tk.call('source', 'azure/azure.tcl')
        style.theme_use('azure')
        style.configure("Accentbutton", foreground='white')

        # ===============================VARIABLES===================================
        self.paramsData = None
        self.wholsalersFilePath = None
        self.carsFilePath = None
        self.productsFilePath = None
        self.distancesFilePath = None

        self.wholsalersData = []
        self.carsData = []
        self.productsData = []
        self.distancesData = []

        self.radioButtonVar = tk.IntVar()

        self.toPlot = None

        self.solution = None

        # ===============================WINDOW======================================
        # Frames
        self.paramsFrame = ttk.LabelFrame(self.root, text='Parametry', width=250, height=410)
        self.paramsFrame.place(x=400, y=12)
        self.propFrame = ttk.LabelFrame(self.paramsFrame, text='Prawdopodobieństwo', width=200, height=265)
        self.propFrame.place(x=20, y=15)
        self.dataFrame = ttk.LabelFrame(self.root, text='Dane', width=355, height=530)
        self.dataFrame.place(x=20, y=12)
        self.algoFrame = ttk.LabelFrame(self.root, text='Algorytm', width=250, height=102)
        self.algoFrame.place(x=400, y=440)

        # Labels
        ttk.Label(self.propFrame, text="Mutacji 1").place(x=20, y=15)
        ttk.Label(self.propFrame, text="Mutacji 2").place(x=20, y=62)
        ttk.Label(self.propFrame, text="Mutacji 3").place(x=20, y=109)
        ttk.Label(self.propFrame, text="Mutacji 4").place(x=20, y=156)
        ttk.Label(self.propFrame, text="Krzyżowania").place(x=20, y=203)
        ttk.Label(self.paramsFrame, text="Liczebność\npopulacji").place(x=40, y=295)
        ttk.Label(self.paramsFrame, text="Liczba iteracji").place(x=40, y=353)

        self.pathW = tk.Label(self.dataFrame, text="Filepath:", justify=LEFT)
        self.pathW.place(x=160, y=13)
        self.pathC = tk.Label(self.dataFrame, text="Filepath:", justify=LEFT)
        self.pathC.place(x=160, y=73)
        self.pathP = tk.Label(self.dataFrame, text="Filepath:", justify=LEFT)
        self.pathP.place(x=160, y=133)
        self.pathD = tk.Label(self.dataFrame, text="Filepath:", justify=LEFT)
        self.pathD.place(x=160, y=193)

        self.errorLabel = tk.Label(root, text=' ', justify=LEFT)
        self.errorLabel.place(x=1030, y=400)

        # Inputs
        self.inM1 = ttk.Entry(self.propFrame, width=8)
        self.inM1.insert(0, '0.1')
        self.inM1.place(x=110, y=8)
        self.inM2 = ttk.Entry(self.propFrame, width=8)
        self.inM2.insert(0, '0.1')
        self.inM2.place(x=110, y=55)
        self.inM3 = ttk.Entry(self.propFrame, width=8)
        self.inM3.insert(0, '0.1')
        self.inM3.place(x=110, y=102)
        self.inM4 = ttk.Entry(self.propFrame, width=8)
        self.inM4.insert(0, '0.1')
        self.inM4.place(x=110, y=149)
        self.inK = ttk.Entry(self.propFrame, width=8)
        self.inK.insert(0, '0.98')
        self.inK.place(x=110, y=196)
        self.inPop = ttk.Entry(self.paramsFrame, width=8)
        self.inPop.insert(0, '10')
        self.inPop.place(x=130, y=295)
        self.inIt = ttk.Entry(self.paramsFrame, width=8)
        self.inIt.insert(0, '10')
        self.inIt.place(x=130, y=346)

        # Notebook
        self.notebook = ttk.Notebook(self.dataFrame, width=150, height=180)
        self.notebook.place(x=20, y=290)

        # karty w notatniku
        self.tabW = ttk.Frame(self.notebook, width=150, height=150)
        self.notebook.add(self.tabW, text='Hurtownie')
        self.tabC = ttk.Frame(self.notebook, width=150, height=150)
        self.notebook.add(self.tabC, text='Samochody')
        self.tabP = ttk.Frame(self.notebook, width=150, height=150)
        self.notebook.add(self.tabP, text='Produkty')
        self.tabD = ttk.Frame(self.notebook, width=150, height=150)
        self.notebook.add(self.tabD, text='Dystanse')

        # scrolled texts
        self.scrtextW = st.ScrolledText(self.tabW, width=45, height=12, state='disabled')
        self.scrtextW.pack()
        self.scrtextC = st.ScrolledText(self.tabC, width=45, height=12, state='disabled')
        self.scrtextC.pack()
        self.scrtextP = st.ScrolledText(self.tabP, width=45, height=12, state='disabled')
        self.scrtextP.pack()
        self.scrtextD = st.ScrolledText(self.tabD, width=45, height=12, state='disabled')
        self.scrtextD.pack()
        self.scrtextSolution = st.ScrolledText(self.root, width=55, height=14.5, state='disabled')
        self.scrtextSolution.place(x=670, y=313)

        # Buttons
        self.get_wholB = ttk.Button(self.dataFrame, text='Wgraj hurtownie', style='Accentbutton',
                                    command=lambda: self.browser_wholsel(),
                                    width=16)
        self.get_wholB.place(x=20, y=15)
        self.get_carsB = ttk.Button(self.dataFrame, text='Wgraj samochody', style='Accentbutton',
                                    command=lambda: self.browser_cars(), width=16)
        self.get_carsB.place(x=20, y=75)
        self.get_prodB = ttk.Button(self.dataFrame, text='Wgraj produkty', style='Accentbutton',
                                    command=lambda: self.browser_products(),
                                    width=16)
        self.get_prodB.place(x=20, y=135)
        self.get_distB = ttk.Button(self.dataFrame, text='Wgraj dystanse', style='Accentbutton',
                                    command=lambda: self.browser_distances(),
                                    width=16)
        self.get_distB.place(x=20, y=195)
        self.get_all = ttk.Button(self.dataFrame, text='Wgraj automatycznie', style='Accentbutton',
                                  command=lambda: self.browser_all())
        self.get_all.place(x=20, y=250)
        self.startAlgoB = ttk.Button(self.algoFrame, text='Uruchom algorytm', style='Accentbutton',
                                     command=lambda: self.start())
        self.startAlgoB.place(x=60, y=45)

        # Radiobuttons
        self.radio1 = ttk.Radiobutton(self.algoFrame, text='Algorytm 1', variable=self.radioButtonVar, value=1)
        self.radio1.place(x=10, y=5)
        self.radio2 = ttk.Radiobutton(self.algoFrame, text='Algorytm 2', variable=self.radioButtonVar, value=2)
        self.radio2.place(x=130, y=5)

    # ===============================METHODS======================================
    # Reading .txt files
    def browser_distances(self):
        self.distancesData = []
        self.distancesFilePath = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                            filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        if self.distancesFilePath:
            with open(self.distancesFilePath, mode="r", encoding="utf-8") as input_file:
                self.scrtextD.configure(state='normal')
                self.scrtextD.delete(1.0, END)
                for lines in input_file.readlines():
                    self.scrtextD.insert(tk.INSERT, lines)
                    lines = lines.split()
                    if lines:
                        self.distancesData.append([int(i) for i in lines])
                self.scrtextD.configure(state='disabled')
        self.pathD.configure(text='Filepath:\n' + self.distancesFilePath)

    def browser_wholsel(self):
        self.wholsalersData = []
        if self.distancesData == [] or self.distancesData is None:
            self.errorLabel.configure(text='Error: najpierw wgraj plik z dystansami')
            pass
        if self.distancesData:
            self.errorLabel.configure(text='')

        self.wholsalersFilePath = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                             filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        if self.wholsalersFilePath:
            with open(self.wholsalersFilePath, mode="r", encoding="utf-8") as input_file:
                self.scrtextW.configure(state='normal')
                self.scrtextW.delete(1.0, END)
                for count, lines in enumerate(input_file.readlines()):
                    self.scrtextW.insert(tk.INSERT, lines)
                    lines = lines.split()
                    self.wholsalersData.append(lines)
                    # self.shop.add_wholesaler(Wholesaler(lines[:-1], self.shop.max_id_hurt, self.distancesData[count]))
                self.scrtextW.configure(state='disabled')
        self.pathW.configure(text='Filepath:\n' + self.wholsalersFilePath)

    def browser_cars(self):
        self.carsData = []
        self.carsFilePath = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                       filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        if self.carsFilePath:
            with open(self.carsFilePath, mode="r", encoding="utf-8") as input_file:
                self.scrtextC.configure(state='normal')
                self.scrtextC.delete(1.0, END)
                for lines in input_file.readlines():
                    self.scrtextC.insert(tk.INSERT, lines)
                    lines = lines.split()
                    if lines:
                        self.carsData.append([val if count == 0 else int(val) for count, val in enumerate(lines)])
                # for c in self.carsData:
                #     self.shop.add_car(Car(c[0], c[1]))
                self.scrtextC.configure(state='disabled')
        self.pathC.configure(text='Filepath:\n' + self.carsFilePath)

    def browser_products(self):
        self.productsData = []
        self.productsFilePath = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                           filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        if self.productsFilePath:
            with open(self.productsFilePath, mode="r", encoding="utf-8") as input_file:
                self.scrtextP.configure(state='normal')
                self.scrtextP.delete(1.0, END)
                for lines in input_file.readlines():
                    self.scrtextP.insert(tk.INSERT, lines)
                    lines = lines.split()
                    if lines:
                        self.productsData.append(
                            [val.replace("_", " ") if count == 0 else int(val) for count, val in enumerate(lines)])
                # for p in self.productsData:
                #     self.shop.add_product_for_shop(Product(name=p[0], price=p[1], id_p=self.shop.max_id_prod),
                #                                    randint(1, 100))
                self.scrtextP.configure(state='disabled')
        self.pathP.configure(text='Filepath:\n' + self.productsFilePath)

    def browser_all(self):
        self.wholsalersData = []
        self.carsData = []
        self.productsData = []
        self.distancesData = []

        if not self.distancesFilePath:
            with open('Data/distances.txt', mode="r", encoding="utf-8") as input_file:
                self.scrtextD.configure(state='normal')
                self.scrtextD.delete(1.0, END)
                for line in input_file.readlines():
                    self.scrtextD.insert(tk.INSERT, line)
                    line = line.split()
                    if line:
                        self.distancesData.append([int(i) for i in line])
                self.scrtextD.configure(state='disabled')
        self.pathD.configure(text='Filepath:\n' + 'Data/distances.txt')

        if not self.wholsalersFilePath:
            if self.distancesData == [] or self.distancesData is None:
                self.errorLabel.configure(text='Error: najpierw wgraj plik z dystansami')
                pass
            if self.distancesData:
                self.errorLabel.configure(text='')

            with open('Data/Hurtownie.txt', mode="r", encoding="utf-8") as input_file:
                self.scrtextW.configure(state='normal')
                self.scrtextW.delete(1.0, END)
                for count, lines in enumerate(input_file.readlines()):
                    self.scrtextW.insert(tk.INSERT, lines)
                    lines = lines.split()
                    self.wholsalersData.append(lines)
                    if self.distancesData == [] or self.distancesData is None:
                        self.errorLabel.configure(text='Error: najpierw wgraj plik z dystansami')
                        pass
                    # self.shop.add_wholesaler(Wholesaler(lines[:-1], self.shop.max_id_hurt, self.distancesData[count]))
                self.scrtextW.configure(state='disabled')
        self.pathW.configure(text='Filepath:\n' + 'Data/Hurtownie.txt')

        if not self.carsFilePath:
            with open('Data/cars.txt', mode="r", encoding="utf-8") as input_file:
                self.scrtextC.configure(state='normal')
                self.scrtextC.delete(1.0, END)
                for lines in input_file.readlines():
                    self.scrtextC.insert(tk.INSERT, lines)
                    lines = lines.split()
                    if lines:
                        self.carsData.append([val if count == 0 else int(val) for count, val in enumerate(lines)])
                # for c in self.carsData:
                #     self.shop.add_car(Car(c[0], c[1]))
                self.scrtextC.configure(state='disabled')

        self.pathC.configure(text='Filepath:\n' + 'Data/cars.txt')

        if not self.productsFilePath:
            with open('Data/Produkty.txt', mode="r", encoding="utf-8") as input_file:
                self.scrtextP.configure(state='normal')
                self.scrtextP.delete(1.0, END)
                for lines in input_file.readlines():
                    self.scrtextP.insert(tk.INSERT, lines)
                    lines = lines.split()
                    if lines:
                        self.productsData.append(
                            [val.replace("_", " ") if count == 0 else int(val) for count, val in enumerate(lines)])
                # for p in self.productsData:
                #     self.shop.add_product_for_shop(Product(name=p[0], price=p[1], id_p=self.shop.max_id_prod),
                #                                    randint(1, 100))
                self.scrtextP.configure(state='disabled')
        self.pathP.configure(text='Filepath:\n' + 'Data/produkty.txt')

    def cleanData(self):
        self.shop = Shop()

        for p in self.productsData:
            self.shop.add_product_for_shop(Product(name=p[0], price=p[1], id_p=self.shop.max_id_prod), p[1])

        for c in self.carsData:
            self.shop.add_car(Car(c[0], c[1]))

        for count, lines in enumerate(self.wholsalersData):
            if self.distancesData == [] or self.distancesData is None:
                self.errorLabel.configure(text='Error: najpierw wgraj plik z dystansami')
                pass
            self.shop.add_wholesaler(Wholesaler(lines[:-1], self.shop.max_id_hurt, self.distancesData[count]))

    def start(self):
        self.cleanData()
        popVal = self.inPop.get()
        itVal = self.inIt.get()
        propM1 = self.inM1.get()
        propM2 = self.inM2.get()
        propM3 = self.inM3.get()
        propM4 = self.inM4.get()
        propC = self.inK.get()
        self.errorLabel.configure(text='')
        toplot = None

        conditions = 0

        if popVal == '' or itVal == '' or propM1 == '' or propM2 == '' or propM3 == '' or propM4 == '' or propC == '':  # zmienna nie jest wpisana
            self.errorLabel.configure(text='Error:\nuzupełnij parametry')
            conditions += 1

        if not (popVal.isnumeric() and itVal.isnumeric() and propM1.replace('.', '', 1).isdigit() and propM2.replace(
                '.', '', 1).isdigit() and propM3.replace('.', '', 1).isdigit() and propM4.replace('.', '', 1).isdigit()
                and propC.replace('.', '', 1).isdigit()):  # zmienna nie jest liczbą
            self.errorLabel.configure(text='Error:\nniepoprawna wartość parametru')
            conditions += 1
        else:
            popVal = int(popVal)
            itVal = int(itVal)
            propM1 = float(propM1)
            propM2 = float(propM2)
            propM3 = float(propM3)
            propM4 = float(propM4)
            propC = float(propC)

            if propM1 < 0 or propM1 > 1 or propM2 < 0 or propM2 > 1 or propM3 < 0 or propM3 > 1 or propM4 < 0 \
                    or propM4 > 1 or propC < 0 or propC > 1 or popVal < 0 or itVal < 0:
                self.errorLabel.configure(text='Error:\nniepoprawna wartość parametru')
                conditions += 1

        if self.wholsalersData == [] or self.carsData == [] or self.productsData == [] or self.distancesData == []:  # nie ma wgranych danych
            self.errorLabel.configure(text='Error:\nniekompletne pliki z danymi')
            conditions += 1

        if conditions == 0:
            if self.radioButtonVar.get() == 1:  # algorytm 1
                for w in self.shop.wholesalers:
                    for p in self.shop.products:
                        w.add_product_for_wholesaler(p, randint(1, 10))
                solution, toplot = algo(self.shop, itVal, popVal, propM1, propM2, propM3, propM4)

                if toplot and solution:
                    solution2print = solution.__str__()
                    self.scrtextSolution.configure(state='normal')
                    self.scrtextSolution.delete(1.0, END)
                    self.scrtextSolution.insert(tk.INSERT, solution2print)
                    self.scrtextSolution.configure(state='disabled')

                    fig = Figure(figsize=(5.5, 3), dpi=100)
                    canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
                    canvas.draw()
                    canvas.get_tk_widget().place(x=670, y=-10)
                    fig.add_subplot(111).plot(np.linspace(1, itVal, itVal, endpoint=True), toplot)

            elif self.radioButtonVar.get() == 2:  # algorytm 2
                for w in self.shop.wholesalers:
                    for p in self.shop.products:
                        w.add_product_for_wholesaler(p, randint(0, 100))
                solution, toplot = algo2(self.shop, itVal, popVal, propM1, propM2, propM3, propM4, propC)

                if toplot and solution:
                    solution2print = solution.__str__()
                    self.scrtextSolution.configure(state='normal')
                    self.scrtextSolution.delete(1.0, END)
                    self.scrtextSolution.insert(tk.INSERT, solution2print)
                    self.scrtextSolution.configure(state='disabled')

                    fig = Figure(figsize=(5.5, 3), dpi=100)
                    canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
                    canvas.draw()
                    canvas.get_tk_widget().place(x=670, y=-10)
                    fig.add_subplot(111).plot(np.linspace(1, itVal, itVal, endpoint=True), toplot)

            else:
                self.errorLabel.configure(text='Error:\nnie wybrano algorytmu')
