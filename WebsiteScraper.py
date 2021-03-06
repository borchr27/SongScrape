from datetime import date
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import pandas as pd
import requests 
from bs4 import BeautifulSoup
import re
from CreateSongData import CreateSongData
from FindCharLoc import FindCharLoc

class WebsiteScraper:
    """ 
    Invokes a chrome browser and using selenium creates the soup object
    then searches soup for the 'label-wrapper' to find all the data for chords
    then iterates thru that data and scrubs it with the CreateSongData class
    so we are left with just the raw chord, then code outputs this to an excel
    """
    def __init__(self, chordifyUrl):
        self.chordifyUrl = chordifyUrl
        self.soup = None

    def website_scraper(self):
        # First block gets chord data, second block gets song youtube link
        options = webdriver.ChromeOptions()
        browser = webdriver.Chrome(options=options)
        browser.get(self.chordifyUrl)
        html = browser.page_source
        self.soup = BeautifulSoup(html, 'lxml')
        chords = self.soup.find_all(class_='label-wrapper')
        data = []
        for chord in chords:
            chord_data = CreateSongData(str(chord))
            data.append(chord_data.get_chord())
        df = pd.DataFrame(data, columns=['Chords']).dropna()
        df.to_excel('chords.xlsx')
        browser.close()

        # [<a href="https://www.youtube.com/watch?v=LKrnR3aJKQA" rel="nofollow" target="_blank">Explainer Video</a>]
        fcl = FindCharLoc()
        tag = self.soup.find_all('div', attrs = {'data-stream': re.compile('https://www.youtube.com/')} )
        #tag = requests.get(soup.find('iframe'))
        #tag = soup.find_all('a', attrs = {'href': re.compile('^https://www.youtube.com')} )
        quote_array = fcl.find_char_loc(str(tag[0]), '"')
        start_snip = quote_array[8]
        end_snip = quote_array[9]
        tag = str(tag[0])
        tag = tag[start_snip+1:end_snip]
        link_file = open("YoutubeLink.txt", "w")
        link_file.write(tag)
        link_file.close()