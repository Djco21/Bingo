# Import Module
from tkinter import *

# Create Tkinter Object
root = Tk()

# Set Geometry
root.geometry("400x400")

# Frame 1
frame1 = Frame(root,bg="black",width=1000,height=600)
frame1.pack()

# Frame 2
frame2 = Frame(frame1,bg="white",width=100,height=100)
frame2.pack(pady=20,padx=20)

# Execute Tkinter
root.mainloop()
