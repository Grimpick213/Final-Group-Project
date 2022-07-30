from select import select
from tkinter import *

pizza = Tk()
pizza.geometry("700x400")
pizza.title("Papa Johns Ordering System")

def pizzaSmall():
    myLabel = Label(pizza, text="You chose a small pizza!")
    myLabel.place(x=400, y=300)
    

pizza.config(bg='#006D56')

pizza_size = Label(pizza,text="Pizza Sizes",font="Helvetica 28 bold",bg='#006D56',fg='white')
pizza_size.place(x=400, y=5)

pizza_small = Label(pizza,text="Small - $9.00",font="Helvetica 12 bold",bg='#006D56',fg='white')
pizza_small.place(x=400, y=50)

pizza_medium = Label(pizza,text="Medium - $12.00",font="Helvetica 12 bold",bg='#006D56',fg='white')
pizza_medium.place(x=400, y=70)

pizza_large = Label(pizza,text="Large - $15.00",font="Helvetica 12 bold",bg='#006D56',fg='white')
pizza_large.place(x=400, y=90)

pizza_toppings = Label(pizza,text="Pizza Toppings",font="Helvetica 28 bold",bg='#006D56',fg='white')
pizza_toppings.place(x=400, y=120)

pepperoni = Label(pizza,text="pepperoni - $0.50",font="Helvetica 12 bold",bg='#006D56',fg='white')
pepperoni.place(x=400, y=160)

sausage = Label(pizza,text="sausage - $0.65",font="Helvetica 12 bold",bg='#006D56',fg='white')
sausage.place(x=400, y=180)

mushrooms = Label(pizza,text="mushrooms - $0.35",font="Helvetica 12 bold",bg='#006D56',fg='white')
mushrooms.place(x=400, y=200)

pinapple = Label(pizza,text="pinapple - $0.45",font="Helvetica 12 bold",bg='#006D56',fg='white')
pinapple.place(x=400, y=220)

select_items = Label(pizza,text="Select your items",font="Helvetica 28 bold",bg='#006D56',fg='white')
select_items.place(x=0, y=5)

select_pizza = Label(pizza, text="Select Pizza Size",font="Helvetica 12 bold",bg='#006D56',fg='white')
select_pizza.place(x=10, y=50)

small_button = Button(pizza,text='S',width=5,command=pizzaSmall)
small_button.place(x=150, y=50)

medium_button = Button(pizza,text='M',width=5)
medium_button.place(x=200, y=50)

large_button = Button(pizza,text='L',width=5)
large_button.place(x=250, y=50)

select_toppings = Label(pizza, text="Select toppings",font="Helvetica 12 bold",bg='#006D56',fg='white')
select_toppings.place(x=10, y=90)

pepperoni_button = Button(pizza,text='Pepperoni',width=20)
pepperoni_button.place(x=150, y=100)

sausage_button = Button(pizza,text='Sausage',width=20)
sausage_button.place(x=150, y=130)

mushroom_button = Button(pizza,text='Mushrooms',width=20)
mushroom_button.place(x=150, y=160)

pinapple_button = Button(pizza,text='Pinapple',width=20)
pinapple_button.place(x=150, y=190)

bill_button = Button(pizza,text='Total Bill',width=10)
bill_button.place(x=10,y=230)







pizza.mainloop()