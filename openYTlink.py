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

url = f"https://chordify.net/chords/rescue-by-alysha-brilla-on-ctv-live-regina-alysha-brilla"
browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

#posts = soup.find_all(class_='chord')
chords = soup.find_all('a')
print(chords)