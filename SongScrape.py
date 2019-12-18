# Based off of a LucidProgramming Tutorial
# Environment: anaconda cloud borchr27/songscrape
# https://www.youtube.com/watch?v=x5o0XFozYnE
# Created/Modified by AV 4/16/19
# bs4 v 4.6.3
# selenium v 3.141.0
# pandas v 0.23.4
# urllib3 v 1.23

"""
This program is used to scrape craigslist for a certain item with the specified parameters. In this case it is used to monitor cragislist for a Toyota in Grand Rapids MI for less than $7000. The program opens a browser directs itself to the inteded site, scrapes the data, then throws the Date, Price, Title, and Link into an excel file. 

"""
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pandas as pd
import requests 
from bs4 import BeautifulSoup
import urllib.request

url = f"https://chordify.net/chords/handmade-moments-where-do-you-find-the-time-official-music-video-handmade-moments"

browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

#posts = soup.find_all(class_='chord')
chords = soup.find_all(class_='label-wrapper')


data = []
for chord in chords:
    data.append(chord)
print(type(chord))

df = pd.DataFrame(data)
df.to_excel('chords.xlsx')