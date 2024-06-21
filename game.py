import csv
from tkinter import *
import pandas as pd
import random

global index_left
global index_right
global movies
global score
score=0
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
def next_left():
    global index_right
    global index_left
    global score
    if movies["Rating"][index_left] > movies["Rating"][index_right]:
       print("Better Left")
       index_right = random.randint(0, 249)
       right=movies["Movie"][index_right]
       right_img.config(text=right)
       score+=1
       score_label.config(text=f"Score: {score}")
    elif movies["Rating"][index_left] < movies["Rating"][index_right]:
        print("Better Right")
        index_left = random.randint(0, 249)
        left = movies["Movie"][index_left]
        left_img.config(text=left)
        end()
    else:
        print("Both")
        index_right = random.randint(0, 249)
        right = movies["Movie"][index_right]
        right_img.config(text=right)
        score+=1
        score_label.config(text=f"Score: {score}")
def next_right():
    global index_right
    global index_left
    global score
    if movies["Rating"][index_left] > movies["Rating"][index_right]:
        print("Better Left")
        index_right = random.randint(0, 249)
        right = movies["Movie"][index_right]
        right_img.config(text=right)
        end()
    elif movies["Rating"][index_left] < movies["Rating"][index_right]:
        print("Better Right")
        index_left = random.randint(0, 249)
        left = movies["Movie"][index_left]
        left_img.config(text=left)
        score+=1
        score_label.config(text=f"Score: {score}")

    else:
        print("Both")
        index_right = random.randint(0, 249)
        right = movies["Movie"][index_right]
        right_img.config(text=right)
        score += 1
        score_label.config(text=f"Score: {score}")
def end():

    end_label = Label(text="End")
    left_img.destroy()
    right_img.destroy()
    end_label.grid(column=0, row=1, columnspan=2)
def beginning():
    dir_button.grid(column=0, row=0)
    start_button.grid(column=0, row=1)
    scores_button.grid(column=0, row=2)
def game_beg():
    start_button.destroy()
    dir_button.destroy()
    scores_button.destroy()
    left_img.grid(column=0, row=1)
    right_img.grid(column=1, row=1)
    score_label.grid(column=0, row=0, columnspan=2)
    f = open("scores.csv", "a", encoding="utf8")
    f.write(str(score) + "\n")
    f.close()
window=Tk()
window.title("Movie Ratings")
window.config(padx=50, pady=50)
dir_button=Button(text="Directions")# directions button
start_button=Button(text="Start", command=game_beg) #start game
scores_button=Button(text="High Scores") #Top five scores


game=pd.read_csv("movies.csv")

begin = rand()
left_img= Button(height=20, width=50, text=begin[0], fg='black', command = next_left)




right_img= Button(height= 20, width=50, text=begin[1], command=next_right)


score_label = Label(text=f"Score: {score}")
beginning()


window.mainloop()

print(score)