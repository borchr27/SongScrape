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
        # First block gets chord data, second block gets song youtube link
        driver = webdriver.Chrome()
        driver.get("https://www.ultimate-guitar.com/")
        #driver.get('https://www.ultimate-guitar.com/search.php?search_type=title&value=STRING%20STRING')
        # Finds the search input box
        search = driver.find_element_by_name("value")
        search.clear()
        search.send_keys('Jimmy Buffett Margaritaville')
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        html = driver.page_source
        self.soup = BeautifulSoup(html, 'lxml')
        # The class name here is used to indicate the song name
        options = self.soup.find_all(class_='pZcWD')
        #options = driver.find_element_by_class_name('pZcWD')
        # The class name here is used to tell how many users have ranked the song
        rankings = self.soup.find_all(class_='_31dWM')
        # The class name here is used to tell the rating of the song

        
        for option in options[3:7]:
            print(option.get_text())
        for ranking in rankings[1:5]:
            print(ranking.get_text())
        options = options.find_all('a')
        for a in options[3:7]:
            print(a.get('href')) 
        """
        for item in options:
            self.soup.find_all('a')
            print(link.get('href'))
        """
        driver.close()

new = WebsiteScraper()
new.website_scraper()