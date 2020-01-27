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
        search = driver.find_element_by_name("value")
        search.clear()
        search.send_keys('Jimmy Buffett Margaritaville')
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        html = driver.page_source
        self.soup = BeautifulSoup(html, 'lxml')
        options = self.soup.find_all(class_='pZcWD')
        rankings = self.soup.find_all(class_='_31dWM')
        
        for option in options[3:7]:
            print(option.get_text())
        for ranking in rankings[1:5]:
            print(ranking.get_text())
        
        driver.close()

new = WebsiteScraper()
new.website_scraper()