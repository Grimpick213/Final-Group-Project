from tkinter import *
from turtle import onclick

pizza = Tk()
pizza.geometry("700x380")
pizza.title("Papa Johns Ordering System")

#PRICES
small_pizza = 9.00
medium_pizza = 12.00
large_pizza = 15.00
pepperoni_topping = 0.50
sausage_topping = 0.65
mushroom_topping = 0.35
pinapple_topping = 0.45

#DEFINES
def pizzaSmall():
    myLabel = Label(pizza, text="You chose a small pizza!",font="Helvetica 12 bold",bg='#006D56',fg='white')
    myLabel.place(x=400, y=250)

def pizzaMedium():
    myLabel = Label(pizza, text="You chose a medium pizza!",font="Helvetica 12 bold",bg='#006D56',fg='white')
    myLabel.place(x=400, y=250)

def pizzaLarge():
    myLabel = Label(pizza, text="You chose a large pizza!",font="Helvetica 12 bold",bg='#006D56',fg='white')
    myLabel.place(x=400, y=250)

def toppingPepperoni():
    myLabel = Label(pizza, text="With pepperoni!",font="Helvetica 12 bold",bg='#006D56',fg='white')
    myLabel.place(x=400, y=270)

def toppingSausage():
    myLabel = Label(pizza, text="With sausage!",font="Helvetica 12 bold",bg='#006D56',fg='white')
    myLabel.place(x=400, y=290)

def toppingMushrooms():
    myLabel = Label(pizza, text="With mushrooms!",font="Helvetica 12 bold",bg='#006D56',fg='white')
    myLabel.place(x=400, y=310)

def toppingPinapple():
    myLabel = Label(pizza, text="With pinapple!",font="Helvetica 12 bold",bg='#006D56',fg='white')
    myLabel.place(x=400, y=330)

def finalBill():
    myLabel = Label(pizza, text="CONGRATULATIONS!! Your pizza is FREE!",font="Helvetica 12 bold",bg='#006D56',fg='white')
    myLabel.place(x=50, y=300)
   
total = 0

def calculate():
      small=small_pizza
      medium=medium_pizza
      large=large_pizza
      pepperoni=pepperoni_topping
      sausage=sausage_topping
      mushrooms=mushroom_topping
      pinapple=pinapple_topping
      print("Your total is $" + str(total))

pizza.config(bg='#006D56')

#LABELS
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

#BUTTONS
small_button = Button(pizza,text='S',width=5,command=pizzaSmall)
small_button.place(x=150, y=50)

medium_button = Button(pizza,text='M',width=5,command=pizzaMedium)
medium_button.place(x=200, y=50)

large_button = Button(pizza,text='L',width=5,command=pizzaLarge)
large_button.place(x=250, y=50)

select_toppings = Label(pizza, text="Select toppings",font="Helvetica 12 bold",bg='#006D56',fg='white')
select_toppings.place(x=10, y=90)

pepperoni_button = Button(pizza,text='Pepperoni',width=20,command=toppingPepperoni)
pepperoni_button.place(x=150, y=100)

sausage_button = Button(pizza,text='Sausage',width=20,command=toppingSausage)
sausage_button.place(x=150, y=130,)

mushroom_button = Button(pizza,text='Mushrooms',width=20,command=toppingMushrooms)
mushroom_button.place(x=150, y=160)

pinapple_button = Button(pizza,text='Pinapple',width=20,command=toppingPinapple)
pinapple_button.place(x=150, y=190)

if small_button == onclick:
    total = total + small_pizza
elif medium_button == onclick:
    total = total + medium_pizza
elif large_button == onclick:
    total = total + large_pizza
else: 
    total = 0

#def new():
    #win = Tk()
    #win.geometry("250x180")
    #win.title('Your receipt')
    #win.mainloop()

bill_button = Button(pizza,text='Total Bill',width=10,command=finalBill)
bill_button.place(x=10,y=230)







pizza.mainloop()