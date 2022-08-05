from re import I
from tkinter import *



#basic data
Menu = Tk()
Menu.title("한식양식중식일식")
Menu.geometry()
Menu.resizable(True,True)




#korean_food_toggle
korean_food_active = 0
korean_food_disabled = 1
def korean_food_method():
    global korean_food_active
    global korean_food_disabled
    if (korean_food_active == 0):
        korean_food_active = 1
        korean_food.config(bg = "yellow")
    elif (korean_food_active == 1):
        korean_food_disabled = 1
        korean_food_active = 0
        korean_food.config(bg = "white")



#chinese_food_toggle
chinese_food_active = 0
chinese_food_disabled = 1
def chinese_food_method():
    global chinese_food_active
    global chinese_food_disabled
    if (chinese_food_active == 0):
        chinese_food_active = 1
        chinese_food.config(bg = "yellow")
    elif (chinese_food_active == 1):
        chinese_food_disabled = 1
        chinese_food_active = 0
        chinese_food.config(bg = "white")


#western_food_toggle
western_food_active = 0
western_food_disabled = 1
def western_food_method():
    global western_food_active
    global western_food_disabled
    if (western_food_active == 0):
        western_food_active = 1
        western_food.config(bg = "yellow")
    elif (western_food_active == 1):
        western_food_disabled = 1
        western_food_active = 0
        western_food.config(bg = "white")


#japanese_food_toggle
japanese_food_active = 0
japanese_food_disabled = 1
def japanese_food_method():
    global japanese_food_active
    global japanese_food_disabled
    if (japanese_food_active == 0):
        japanese_food_active = 1
        japanese_food.config(bg = "yellow")
    elif (japanese_food_active == 1):
        japanese_food_disabled = 1
        japanese_food_active = 0
        japanese_food.config(bg = "white")


#rice_toggle
rice_active = 0
rice_disabled = 1
def rice_method():
    global rice_active
    global rice_disabled
    if (rice_active == 0):
        rice_active = 1
        rice.config(bg = "yellow")
    elif (rice_active == 1):
        rice_disabled = 1
        rice_active = 0
        rice.config(bg = "white")


#bread_toggle
bread_active = 0
bread_disabled = 1
def bread_method():
    global bread_active
    global bread_disabled
    if (bread_active == 0):
        bread_active = 1
        bread.config(bg = "yellow")
    elif (bread_active == 1):
        bread_disabled = 1
        bread_active = 0
        bread.config(bg = "white")


#noodle_toggle
noodle_active = 0
noodle_disabled = 1
def noodle_method():
    global noodle_active
    global noodle_disabled
    if (noodle_active == 0):
        noodle_active = 1
        noodle.config(bg = "yellow")
    elif (noodle_active == 1):
        noodle_disabled = 1
        noodle_active = 0
        noodle.config(bg = "white")


#rice_cake_toggle
rice_cake_active = 0
rice_cake_disabled = 1
def rice_cake_method():
    global rice_cake_active
    global rice_cake_disabled
    if (rice_cake_active == 0):
        rice_cake_active = 1
        rice_cake.config(bg = "yellow")
    elif (rice_cake_active == 1):
        rice_cake_disabled = 1
        rice_cake_active = 0
        rice_cake.config(bg = "white")


#sweetness_toggle
sweetness_active = 0
sweetness_disabled = 1
def sweetness_method():
    global sweetness_active
    global sweetness_disabled
    if (sweetness_active == 0):
        sweetness_active = 1
        sweetness.config(bg = "yellow")
    elif (sweetness_active == 1):
        sweetness_disabled = 1
        sweetness_active = 0
        sweetness.config(bg = "white")


#sourness_toggle
sourness_active = 0
sourness_disabled = 1
def sourness_method():
    global sourness_active
    global sourness_disabled
    if (sourness_active == 0):
        sourness_active = 1
        sourness.config(bg = "yellow")
    elif (sourness_active == 1):
        sourness_disabled = 1
        sourness_active = 0
        sourness.config(bg = "white")


#salty_toggle
salty_active = 0
salty_disabled = 1
def salty_method():
    global salty_active
    global salty_disabled
    if (salty_active == 0):
        salty_active = 1
        salty.config(bg = "yellow")
    elif (salty_active == 1):
        salty_disabled = 1
        salty_active = 0
        salty.config(bg = "white")


#spicy_toggle
spicy_active = 0
spicy_disabled = 1
def spicy_method():
    global spicy_active
    global spicy_disabled
    if (spicy_active == 0):
        spicy_active = 1
        spicy.config(bg = "yellow")
    elif (spicy_active == 1):
        spicy_disabled = 1
        spicy_active = 0
        spicy.config(bg = "white")


#play
def play():
    global korean_food_active
    if (korean_food_active == 1):
        korea = Toplevel(Menu)




#Button1
korean_food = Button(Menu, text="한식", fg = "red", width = 10, height = 5,bg = "white" , command = korean_food_method)
chinese_food = Button(Menu, text = "중식", fg = "black", width = 10, height = 5, command = chinese_food_method, bg = "white")
western_food = Button(Menu, text = "양식", fg = "brown", width = 10, height = 5, command = western_food_method, bg = "white")
japanese_food = Button(Menu, text = "일식", fg = "green", width = 10, height = 5, command = japanese_food_method, bg = "white")


#Button2
rice = Button(Menu, text="밥", fg = "red", width = 10, height = 5, bg = "white" , command = rice_method)
bread = Button(Menu, text = "빵", fg = "black", width = 10, height = 5, bg = "white" , command = bread_method)
noodle = Button(Menu, text = "면", fg = "brown", width = 10, height = 5, bg = "white" , command = noodle_method)
rice_cake = Button(Menu, text = "떡", fg = "green", width = 10, height = 5, bg = "white" , command = rice_cake_method)


#Button3
sweetness = Button(Menu, text = "단맛", fg = "hotpink", width = 10, height = 5, bg = "white" , command = sweetness_method)
sourness = Button(Menu, text = "신맛", fg = "black", width = 10, height = 5, bg = "white" , command = sourness_method)
salty = Button(Menu, text = "짠맛", fg = "brown", width = 10, height = 5, bg = "white" , command = salty_method)
spicy = Button(Menu, text = "매운맛", fg = "red", width = 10, height = 5, bg = "white" , command = spicy_method)


#Button4
decision = Button(Menu, text="결정", fg="black", width = 10, height = 3, command = play)





#grid
korean_food.grid(row = 0, column = 0)
chinese_food.grid(row = 0, column = 1)
western_food.grid(row = 0, column = 2)
japanese_food.grid(row = 0, column = 3)
rice.grid(row = 1, column = 0)
bread.grid(row = 1, column = 1)
noodle.grid(row = 1, column = 2)
rice_cake.grid(row = 1, column = 3)
sweetness.grid(row = 2, column = 0)
sourness.grid(row = 2, column = 1)
salty.grid(row = 2, column = 2)
spicy.grid(row = 2, column = 3)
decision.grid(row=3, column = 3)


Menu.mainloop()