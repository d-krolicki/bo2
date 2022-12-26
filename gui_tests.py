import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

# Set window
root = tk.Tk()
root.title('Sklep')
root.resizable(width=False, height=False)  # rozmiar okna jest stały

window_height = 500
window_width = 800
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
# TODO: zmiana czcionki i ramek frame 'Parametry' oraz 'Dane'
paramsFrame = ttk.LabelFrame(root, text='Parametry', width=250, height=360)
paramsFrame.place(x=20, y=12)
propFrame = ttk.LabelFrame(paramsFrame, text='Prawdopodobieństwo', width=200, height=215)
propFrame.place(x=20, y=15)
dataFrame = ttk.LabelFrame(root, text='Dane', width=450, height=300)
dataFrame.place(x=300, y=12)

# Labels
ttk.Label(propFrame, text="Mutacji 1").place(x=20, y=15)
ttk.Label(propFrame, text="Mutacji 2").place(x=20, y=62)
ttk.Label(propFrame, text="Mutacji 3").place(x=20, y=109)
ttk.Label(propFrame, text="Krzyżowania").place(x=20, y=156)
ttk.Label(paramsFrame, text="Liczebność\npopulacji").place(x=40, y=245)
ttk.Label(paramsFrame, text="Liczba iteracji").place(x=40, y=303)
pathW = tk.Label(dataFrame, text="Filepath: -")
pathW.place(x=20, y=60)
pathC = tk.Label(dataFrame, text="Filepath: -")
pathC.place(x=20, y=145)
pathP = tk.Label(dataFrame, text="Filepath: -")
pathP.place(x=20, y=230)

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


# Reading .txt files
def browser_wholsel():
    global hurtownie
    hurtownie = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                           filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    # if hurtownie:
    #     with open(hurtownie, mode="r", encoding="utf-8") as input_file:
    #         for line in input_file.readlines():
    #             print(line)
    pathW.configure(text='Filepath:' + hurtownie)


# Buttons
# TODO: napisanie funkcji browser dla samochodów oraz produktów
get_paramsB = ttk.Button(root, text='Zapisz parametry', style='Accentbutton', command=get_params)
get_paramsB.place(x=80, y=400)
get_whols = ttk.Button(dataFrame, text='Wgraj hurtownie', style='Accentbutton', command=browser_wholsel)
get_whols.place(x=20, y=15)
get_whols = ttk.Button(dataFrame, text='Wgraj samochody', style='Accentbutton', command=browser_wholsel)
get_whols.place(x=20, y=100)
get_whols = ttk.Button(dataFrame, text='Wgraj produkty', style='Accentbutton', command=browser_wholsel)
get_whols.place(x=20, y=185)

root.mainloop()
