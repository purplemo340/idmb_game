from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

import io
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
def pics():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    picture=[]
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.imdb.com/chart/top/")
    pictures=driver.find_elements(By.CLASS_NAME, "ipc-image")

    # for pic in pictures:
    #     pic=display_image_from_url(pic.get_attribute("src"))
    #     picture.append(pic)
    url = []
    for x in range(len(pictures)):
        url.append(pictures[x].get_attribute('src'))
    m = open("images.csv", "w")
    url_1=pd.DataFrame(url)
    url_1.to_csv("images.csv", header=['url'])
    return pictures
p=pics()
# window= Tk()
# pictures=pics()
# url=pictures[0].get_attribute('src')
# response = requests.get(url)
# img_data = response.content
# image_1 = Image.open(io.BytesIO(img_data))
# photo = ImageTk.PhotoImage(image_1)
# print(response)
# print(pictures)
#
# panel=Label(image=photo)
# panel.grid(row=0, column=0)
# window.mainloop()