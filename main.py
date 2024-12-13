from tkinter import *
from tkinter import ttk
import back
import classes
root = Tk()
root.title('Bingo DGSTIC')
root.geometry('1920x1080')
root.config(background= '#000000')
frm = ttk.Frame(root)
frm.grid(padx=960,pady=650)
frm.config(height=1000,width=1000)
start_title = ttk.Label(frm, text="Bingo!").grid()
start_button = ttk.Button(frm, text='Iniciar', command='').grid(column=0, row=2)
quit_button = ttk.Button(frm, text="Sair", command=root.destroy).grid(column=0, row=4)
root.mainloop()