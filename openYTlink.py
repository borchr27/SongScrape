from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pandas as pd
import requests 
#import lxml.html
from bs4 import BeautifulSoup
import urllib.request

# https://www.youtube.com/watch?v=5N066ISH8og&feature=emb_logo

url = f"https://chordify.net/chords/rescue-by-alysha-brilla-on-ctv-live-regina-alysha-brilla"
browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
soup1 = str(html.find_all('aside'))
soup2 = soup.xpath('//div[id="data-stream"]')[0]

#file2write = open("SoupData",'w')
#file2write.write(soup1)
#file2write.close()

print(soup2)


browser.close()