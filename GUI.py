from tkinter import *
from PapaJohns import pizza

root = Tk()
root.title("Papa John's Pizza")
root.geometry("800x500")


greet = pizza("Thank you for choosing Papa John's")

my_label = Label(root, text=greet, font=("Helvetica", 18))
my_label.pack(pady=20)








root.mainloop()