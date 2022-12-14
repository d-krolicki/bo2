import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.scrolledtext as st
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

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
        self.purchaseSumData = []

        self.purSumDisp = []

        self.radioButtonVar = tk.IntVar()

        self.toPlot = None

        self.solution = None

        # ===============================WINDOW======================================
        # Frames
        self.paramsFrame = ttk.LabelFrame(self.root, text='Parametry', width=250, height=410)
        self.paramsFrame.place(x=390, y=0)
        self.propFrame = ttk.LabelFrame(self.paramsFrame, text='Prawdopodobie??stwo', width=200, height=255)
        self.propFrame.place(x=20, y=5)
        self.dataFrame = ttk.LabelFrame(self.root, text='Dane', width=355, height=530)
        self.dataFrame.place(x=10, y=0)
        self.algoFrame = ttk.LabelFrame(self.root, text='Algorytm', width=250, height=102)
        self.algoFrame.place(x=390, y=428)
        self.solFrame = ttk.LabelFrame(self.root, text='Wyniki', width=520, height=530)
        self.solFrame.place(x=665, y=0)

        # Labels
        ttk.Label(self.propFrame, text="Mutacji 1").place(x=20, y=15)
        ttk.Label(self.propFrame, text="Mutacji 2").place(x=20, y=62)
        ttk.Label(self.propFrame, text="Mutacji 3").place(x=20, y=109)
        ttk.Label(self.propFrame, text="Mutacji 4").place(x=20, y=156)
        ttk.Label(self.propFrame, text="Krzy??owania").place(x=20, y=203)
        ttk.Label(self.paramsFrame, text="Liczebno????\npopulacji").place(x=40, y=270)
        ttk.Label(self.paramsFrame, text="Liczba iteracji").place(x=40, y=320)
        ttk.Label(self.paramsFrame, text="PenalityVal").place(x=40, y=360)

        self.pathW = tk.Label(self.dataFrame, text="Filepath:", justify=LEFT)
        self.pathW.place(x=160, y=13)
        self.pathC = tk.Label(self.dataFrame, text="Filepath:", justify=LEFT)
        self.pathC.place(x=160, y=73)
        self.pathP = tk.Label(self.dataFrame, text="Filepath:", justify=LEFT)
        self.pathP.place(x=160, y=133)
        self.pathD = tk.Label(self.dataFrame, text="Filepath:", justify=LEFT)
        self.pathD.place(x=160, y=193)

        self.errorLabel = tk.Label(self.root, text='', justify=LEFT)
        self.errorLabel.place(x=1030, y=450)
        self.penFunValLabel = tk.Label(self.root, text='', justify=LEFT)
        self.penFunValLabel.place(x=1030, y=350)

        # Inputs (Entry)
        self.inM1 = ttk.Entry(self.propFrame, width=8)
        self.inM1.insert(0, '0.2')
        self.inM1.place(x=110, y=8)
        self.inM2 = ttk.Entry(self.propFrame, width=8)
        self.inM2.insert(0, '0.2')
        self.inM2.place(x=110, y=55)
        self.inM3 = ttk.Entry(self.propFrame, width=8)
        self.inM3.insert(0, '0.2')
        self.inM3.place(x=110, y=102)
        self.inM4 = ttk.Entry(self.propFrame, width=8)
        self.inM4.insert(0, '0.2')
        self.inM4.place(x=110, y=149)
        self.inK = ttk.Entry(self.propFrame, width=8)
        self.inK.insert(0, '0.98')
        self.inK.place(x=110, y=196)
        self.inPop = ttk.Entry(self.paramsFrame, width=8)
        self.inPop.insert(0, '15')
        self.inPop.place(x=130, y=270)
        self.inIt = ttk.Entry(self.paramsFrame, width=8)
        self.inIt.insert(0, '10')
        self.inIt.place(x=130, y=310)
        self.inPenVal = ttk.Entry(self.paramsFrame, width=8)
        self.inPenVal.insert(0, '100')
        self.inPenVal.place(x=130, y=353)

        # Notebook
        self.notebookData = ttk.Notebook(self.dataFrame, width=150, height=180)
        self.notebookData.place(x=20, y=290)

        self.notebookSol = ttk.Notebook(self.solFrame, width=330, height=200)
        self.notebookSol.place(x=15, y=270)

        # karty w notatniku
        self.tabW = ttk.Frame(self.notebookData, width=150, height=150)
        self.notebookData.add(self.tabW, text='Hurtownie')
        self.tabC = ttk.Frame(self.notebookData, width=150, height=150)
        self.notebookData.add(self.tabC, text='Samochody')
        self.tabP = ttk.Frame(self.notebookData, width=150, height=150)
        self.notebookData.add(self.tabP, text='Produkty')
        self.tabD = ttk.Frame(self.notebookData, width=150, height=150)
        self.notebookData.add(self.tabD, text='Dystanse')

        self.tabSol = ttk.Frame(self.notebookSol, width=250, height=200)
        self.notebookSol.add(self.tabSol, text='Rozwi??zanie')
        self.tabDemand = ttk.Frame(self.notebookSol, width=250, height=200)
        self.notebookSol.add(self.tabDemand, text='Pokrycie zapotrzebowania')

        # scrolled texts
        self.scrtextW = st.ScrolledText(self.tabW, width=45, height=12, state='disabled')
        self.scrtextW.pack()
        self.scrtextC = st.ScrolledText(self.tabC, width=45, height=12, state='disabled')
        self.scrtextC.pack()
        self.scrtextP = st.ScrolledText(self.tabP, width=45, height=12, state='disabled')
        self.scrtextP.pack()
        self.scrtextD = st.ScrolledText(self.tabD, width=45, height=12, state='disabled')
        self.scrtextD.pack()

        self.scrtextSolution = st.ScrolledText(self.tabSol, width=60, height=12.5, state='disabled')
        self.scrtextSolution.pack()
        # self.scrtextDemand = st.ScrolledText(self.tabDemand, width=60, height=12.5, state='disabled')
        # self.scrtextDemand.pack()

        self.printPurchase = Entry(self.tabDemand, relief=GROOVE)

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
        self.purchaseSumData = []

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

        for w in self.shop.wholesalers:
            id_ = 0
            for p in self.shop.products.items():
                w.add_product_for_wholesaler(Product(p[0], randint(1, 10), id_), np.inf)
                id_ += 1

    def printPurchaseSummary(self, solution):
        toPrintData = [['Produkt', 'Zapotrzebowanie', 'Zakup', 'R????nica']]
        self.purchaseSumData = [0] * len(solution.solution[0][0])

        for cID, car in enumerate(solution.solution):  # iteracja po samochodach
            for p in range(len(solution.solution[cID][0])):  # iteracja po produktach (kolumnach)
                for h in range(len(solution.paths[cID])):  # iteracja po hurtowniach (wierszach)
                    self.purchaseSumData[p] += solution.solution[cID][h][p][1]  # suma zakupionego produktu

        for i, p in enumerate(self.productsData):
            toPrintData.append([p[0], p[1], self.purchaseSumData[i], p[1] - self.purchaseSumData[i]])

        if not self.purSumDisp:
            for i in range(len(toPrintData)):
                tempLst = []
                for j in range(len(toPrintData[0])):
                    e = Entry(self.tabDemand, relief=GROOVE, width=15)
                    e.grid(row=i, column=j, sticky=NSEW)
                    e.insert(END, str(toPrintData[i][j]))
                    e.configure(state=DISABLED)
                    tempLst.append(e)
                self.purSumDisp.append(tempLst)
        else:
            for i in range(len(self.purSumDisp)):
                for j in range(len(self.purSumDisp[0])):
                    self.purSumDisp[i][j].destroy()
            self.purSumDisp = []

            for i in range(len(toPrintData)):
                tempLst = []
                for j in range(len(toPrintData[0])):
                    e = Entry(self.tabDemand, relief=GROOVE, width=15)
                    e.grid(row=i, column=j, sticky=NSEW)
                    e.insert(END, str(toPrintData[i][j]))
                    e.configure(state=DISABLED)
                    tempLst.append(e)
                self.purSumDisp.append(tempLst)

    def start(self):
        self.cleanData()
        popVal = self.inPop.get()
        itVal = self.inIt.get()
        penVal = self.inPenVal.get()
        propM1 = self.inM1.get()
        propM2 = self.inM2.get()
        propM3 = self.inM3.get()
        propM4 = self.inM4.get()
        propC = self.inK.get()

        self.errorLabel.configure(text='')
        toplot = None

        conditions = 0

        if popVal == '' or itVal == '' or penVal == '' or propM1 == '' or propM2 == '' or propM3 == '' or propM4 == '' or propC == '':  # zmienna nie jest wpisana
            self.errorLabel.configure(text='Error:\nuzupe??nij parametry')
            conditions += 1

        if not (popVal.isnumeric() and itVal.isnumeric() and penVal.isnumeric() and propM1.replace('.', '',
                                                                                                   1).isdigit() and propM2.replace(
                '.', '', 1).isdigit() and propM3.replace('.', '', 1).isdigit() and propM4.replace('.', '', 1).isdigit()
                and propC.replace('.', '', 1).isdigit()):  # zmienna nie jest liczb??
            self.errorLabel.configure(text='Error:\nniepoprawna warto???? parametru')
            conditions += 1
        else:
            popVal = int(popVal)
            itVal = int(itVal)
            penVal = int(penVal)
            propM1 = float(propM1)
            propM2 = float(propM2)
            propM3 = float(propM3)
            propM4 = float(propM4)
            propC = float(propC)

            if propM1 < 0 or propM1 > 1 or propM2 < 0 or propM2 > 1 or propM3 < 0 or propM3 > 1 or propM4 < 0 \
                    or propM4 > 1 or propC < 0 or propC > 1 or popVal < 0 or itVal < 0 or penVal < 0:
                self.errorLabel.configure(text='Error:\nniepoprawna warto????\nparametru')
                conditions += 1

        if self.wholsalersData == [] or self.carsData == [] or self.productsData == [] or self.distancesData == []:  # nie ma wgranych danych
            self.errorLabel.configure(text='Error:\nniekompletne pliki\nz danymi')
            conditions += 1

        if conditions == 0:
            if self.radioButtonVar.get() == 1:  # algorytm 1
                solution, toplot = algo(shop=self.shop, iterationStop=itVal, populationSize=popVal, probablityM1=propM1,
                                        probablityM2=propM2, probablityM3=propM3, probablityM4=propM4,
                                        probabilityC=propC, penaltyVal=penVal)

                if toplot and solution:
                    solution2print = solution.__str__()
                    self.scrtextSolution.configure(state='normal')
                    self.scrtextSolution.delete(1.0, END)
                    self.scrtextSolution.insert(tk.INSERT, solution2print)
                    self.scrtextSolution.configure(state='disabled')

                    self.printPurchaseSummary(solution)

                    fig = Figure(figsize=(4.9, 2.6), dpi=100)
                    canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
                    canvas.draw()
                    canvas.get_tk_widget().place(x=690, y=15)
                    fig.add_subplot(111).plot(np.linspace(1, itVal, itVal, endpoint=True), toplot)

                    tempStr = 'Warto???? funkcji celu:\n' + str(solution.cost)
                    self.penFunValLabel.configure(text=tempStr)

            elif self.radioButtonVar.get() == 2:  # algorytm 2
                solution, toplot = algo2(shop=self.shop, iterationStop=itVal, populationSize=popVal,
                                         probablityM1=propM1, probablityM2=propM2, probablityM3=propM3,
                                         probablityM4=propM4, probabilityC=propC, changesInPopulationValue=50,
                                         penaltyVal=penVal)

                if toplot and solution:
                    solution2print = solution.__str__()
                    self.scrtextSolution.configure(state='normal')
                    self.scrtextSolution.delete(1.0, END)
                    self.scrtextSolution.insert(tk.INSERT, solution2print)
                    self.scrtextSolution.configure(state='disabled')

                    self.printPurchaseSummary(solution)

                    fig = Figure(figsize=(4.9, 2.6), dpi=100)
                    canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
                    canvas.draw()
                    canvas.get_tk_widget().place(x=690, y=15)
                    fig.add_subplot(111).plot(np.linspace(1, itVal, itVal, endpoint=True), toplot)

                    tempStr = 'Warto???? funkcji celu:\n' + str(solution.cost)
                    self.penFunValLabel.configure(text=tempStr)

            else:
                self.errorLabel.configure(text='Error:\nnie wybrano\nalgorytmu')
