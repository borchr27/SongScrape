from datetime import date
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pandas as pd
import requests 
from bs4 import BeautifulSoup

from create_song_data import create_song_data


class website_scraper:
    def init(self, chordifyUrl):
        self.chordifyUrl = chordifyUrl

    def main(self, chordifyUrl):
        browser = webdriver.Chrome()
        browser.get(chordifyUrl)
        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')

        #posts = soup.find_all(class_='chord')
        #otherstuff = soup.find_all('data-stream')
        chords = soup.find_all(class_='label-wrapper')
        
        data = []
        for chord in chords:
            data.append(create_song_data(str(chord)))

        df = pd.DataFrame(data, columns=['Chords']).dropna()
        df.to_excel('chords.xlsx')
        #print(otherstuff)
        browser.close()