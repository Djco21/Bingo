from tkinter import *
import back
import classes
root = Tk()
root.title('Bingo DGSTIC')
root.geometry('1920x1080')
root.config(background= '#000000')
root.attributes('-fullscreen', True)

frm_top = Frame(root, width=1920, height=680, bg='gray')
frm_top.grid(row=0, column=0, padx=2, pady=2)

frm_middle = Frame(root, width=1920, height=200, bg='red')
frm_middle.grid(row=1, column=0, padx=2, pady=2)

frm_bottom = Frame(root, width=1900, height=200, bg='blue')
frm_bottom.grid(row=2, column=0, padx=2, pady=2)

#frm_options = Frame(frm_bottom, width=480, height=98, bg='green')
#frm_options.grid(row=0,column=0,padx=(1920-480)/2, pady=(200-98)/2)
next_button = Button(frm_bottom, text='Próxima', command='', width=10, height=2).grid(column=0, row=0, padx=(1890-10)/2, pady=(200-2)/2)
#quit_button = Button(frm_options, text="Sair", command=root.destroy).grid(column=0, row=2)

'''start_title = Label(frm_options, text="Bingo!").grid()
quit_button = Button(frm_options, text="Sair", command=root.destroy).grid(column=0, row=1)'''


root.mainloop()