import csv
import io
import os
from tkinter import *
import pandas as pd
import random

global index_left
global index_right
global movies
global score
global image
score=0
movies= pd.read_csv("movies.csv")
image = pd.read_csv("images.csv")
#Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

from PIL import ImageTk, Image
import tkinter as tk
import urllib.request
global pic
global photo_left
global photo_right
def display_image_from_url(url):
    response = requests.get(url)
    img_data = response.content
    image = Image.open(io.BytesIO(img_data))
    photo = ImageTk.PhotoImage(image)

    return photo


# keep chrome open

def rand():
    global index_left
    global index_right

    index_left = random.randint(0, 250)
    index_right = random.randint(0, 250)

    begin_left = movies["Movie"][index_left]
    begin_right = movies["Movie"][index_right]
    begin = [begin_left, begin_right]
    return begin
def next_left():
    global index_right
    global index_left
    global score
    global photo_left
    global photo_right


    if movies["Rating"][index_left] > movies["Rating"][index_right]:
       print("Better Left")
       index_right = random.randint(0, 250)
       right=movies["Movie"][index_right]

       photo_right = display_image_from_url(image['url'][index_right])
       right_img.config(image=photo_right, text=right)
       #canvas.create_image(20, 20, image=photo)
       print('test')
       score+=1
       score_label.config(text=f"Score: {score}")

    elif movies["Rating"][index_left] < movies["Rating"][index_right]:
        print("Better Right")
        index_left = random.randint(0, 250)
        left = movies["Movie"][index_left]
        photo_left = display_image_from_url(image['url'][index_left])
        right_img.config(image=photo_left, text=left)
        end()
    else:
        print("Both")
        index_right = random.randint(0, 250)
        right = movies["Movie"][index_right]
        photo_right = display_image_from_url(image['url'][index_right])
        right_img.config(image=photo_right, text=right)
        score+=1
        score_label.config(text=f"Score: {score}")

def next_right():
    global index_right
    global index_left
    global score
    global photo_right
    global photo_left
    if movies["Rating"][index_left] > movies["Rating"][index_right]:
        print("Better Left")
        index_right = random.randint(0, 250)
        right = movies["Movie"][index_right]
        photo_right = display_image_from_url(image['url'][index_right])
        right_img.config(image=photo_right, text=right)
        end()
    elif movies["Rating"][index_left] < movies["Rating"][index_right]:
        print("Better Right")
        index_left = random.randint(0, 250)
        left = movies["Movie"][index_left]
        photo_left = display_image_from_url(image['url'][index_left])
        left_img.config(image=photo_left, text=left)
        score+=1
        score_label.config(text=f"Score: {score}")

    else:
        print("Both")
        index_right = random.randint(0, 250)
        right = movies["Movie"][index_right]
        photo_right = display_image_from_url(image['url'][index_right])
        right_img.config(image=photo_right, text=right)
        score += 1
        score_label.config(text=f"Score: {score}")
def end():

    end_label = Label(text="End")
    left_img.destroy()
    right_img.destroy()
    end_label.grid(column=0, row=1, columnspan=2)
def beginning():
    beg_title.grid(column=0, row=0, pady=20)
    dir_button.grid(column=0, row=1)
    start_button.grid(column=0, row=2)
    scores_button.grid(column=0, row=3)
def game_beg():
    start_button.destroy()
    dir_button.destroy()
    scores_button.destroy()
    beg_title.destroy()

    #canvas.grid(row=0, column=0)
    left_img.grid(column=0, row=1)
    right_img.grid(column=1, row=1)
    score_label.grid(column=0, row=0, columnspan=2)
    f = open("scores.csv", "a", encoding="utf8")
    f.write(str(score) + "\n")
    f.close()
window=Tk()
window.title("Movie Ratings")
window.config(padx=20, pady=20, width=500, height=500)
beg_title=Label(text="Movies: Higher or Lower")
dir_button=Button(width=50, height=5, text="Directions")# directions button
start_button=Button(width=50, height=5,text="Start", command=game_beg) #start game
scores_button=Button(width=50, height=5, text="High Scores") #Top five scores


game=pd.read_csv("movies.csv")

begin = rand()
canvas = Canvas(width=100, height=100)
photo_left = display_image_from_url(image['url'][index_left])
photo_right = display_image_from_url(image['url'][index_right])

left_img= Button( text=begin[0], image=photo_left, command=next_left)

right_img= Button( text=begin[1], image=photo_right, command=next_right)


score_label = Label(text=f"Score: {score}")
beginning()




#canvas.create_image(20,20, image=photo)
window.mainloop()

print(score)