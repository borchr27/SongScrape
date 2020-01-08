from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pandas as pd
import requests 
from bs4 import BeautifulSoup
import re
from selenium.webdriver.chrome.options import Options
from datetime import date
import time

class PlayLink:
    """
    Opens the youtube link in a browser window
    """
    def __init__(self):
        pass
        
    def play_link(self, link):
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(10)
        #chrome_options = Options()
        #chrome_options.add_experimental_option("detach", True)
        browser.close()

