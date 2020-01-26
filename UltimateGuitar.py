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
        search = driver.find_element_by_name("value")
        search.clear()
        search.send_keys('Jimmy Buffet')
        search.send_keys(Keys.RETURN)
        time.sleep(10)
        
        driver.close()

new = WebsiteScraper()
new.website_scraper()