#Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
# keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


# response = requests.get("https://www.imdb.com/chart/top/", headers={'Accept-Language': 'en-US,en;q=0.9', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
# text = response.text
# #Collect top 250 tv shows from online
# soup = BeautifulSoup(text, "html.parser")
# movies = soup.find_all(name='a', class_="ipc-title-link-wrapper")
# for movie in movies:
#     print(movie.getText().strip())
driver.get("https://www.imdb.com/chart/top/")
movies=driver.find_elements(By.CLASS_NAME, value="ipc-title--base.ipc-title--on-textPrimary ")
x=0
movie_list=[]
rating_list=[]
#add movies to a list
for movie in movies[2:252]:
    movie_list.append(movie.text)
ratings= driver.find_elements(By.CLASS_NAME, value="ratingGroup--imdb-rating")
for rating in ratings:
    rating_list.append(rating.text.split('\n')[0])

driver.close()


#Add tv shows and ratings to a dictionary

#Game in new script