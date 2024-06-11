from tkinter import *
import pandas as pd
import random

global index_left
global index_right
global movies
movies= pd.read_csv("movies.csv")
def rand():
    global index_left
    global index_right
    index_left = random.randint(0, 249)
    index_right = random.randint(0, 249)

    begin_left = movies["Movie"][index_left]
    begin_right = movies["Movie"][index_right]
    begin = [begin_left, begin_right]
    return begin
def next():
    global index_right
    global index_left
    if movies["Rating"][index_left] > movies["Rating"][index_right]:
       print("Better Left")
       index_right = random.randint(0, 249)
       right=movies["Movie"][index_right]
       right_img.config(text=right)
    elif movies["Rating"][index_left] < movies["Rating"][index_right]:
        print("Better Right")
        index_left = random.randint(0, 249)
        left = movies["Movie"][index_left]
        left_img.config(text=left)
    else:
        print("Both")
        index_right = random.randint(0, 249)
        right = movies["Movie"][index_right]
        right_img.config(text=right)

window=Tk()
window.title("Movie Ratings")
window.config(padx=50, pady=50)

game=pd.read_csv("movies.csv")

begin = rand()

left_img= Button(height=20, width=50, text=begin[0], fg='black', command = next)
left_img.grid(column=0, row=0)



right_img= Button(height= 20, width=50, text=begin[1], command=next)
right_img.grid(column=1, row=0)

window.mainloop()