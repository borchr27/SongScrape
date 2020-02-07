from datetime import date
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import pandas as pd
import requests 
from bs4 import BeautifulSoup
import re

class WebsiteScraper:
    """ 
    Type
    """
    def __init__(self):
        self.soup = None

    def website_scraper(self):
        # Jimmy Buffet Margaritaville
        song_info = input("Enter Artist Name and Song Name: ")
        # Modifies entered text to be concatenated to URL
        song_info.replace(' ', '%20')
        driver = webdriver.Chrome()
        # Uses user entered search terms to search Ultimate Guitar
        driver.get('https://www.ultimate-guitar.com/search.php?search_type=title&value={}'.format(song_info))
        # Create the soup to search for items
        html = driver.page_source
        self.soup = BeautifulSoup(html, 'lxml')
        # The class name here is used to indicate the song name
        options = self.soup.find_all(class_='pZcWD')
        # The class name here is used to tell how many users have ranked the song
        rankings = self.soup.find_all(class_='_31dWM')
        # The class name here is used to tell the rating of the song

        choices = df = pd.DataFrame(columns=["Rating","Description","Link"])
        for description, ranking, link in zip(options[3:7], rankings[1:5], options[3:7]):
            link = link.find('a')
            choices = df.append(pd.Series([ranking.get_text(), description.get_text(), link.get('href')], index=df.columns ), ignore_index=True)
        
        for row in choices.itertuples():
            print(row)
        
        # Need to sort data frame and then select / open link that has the highes ratings
        # Scrape chords and lyrics from page
        # really need to hop back into this er mer gerug

        driver.close()

new = WebsiteScraper()
new.website_scraper()