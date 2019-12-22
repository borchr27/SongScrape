# Based off of a LucidProgramming Tutorial
# Environment: anaconda cloud borchr27/songscrape
# https://www.youtube.com/watch?v=x5o0XFozYnE
# Created/Modified by AV 4/16/19
# bs4 v 4.6.3
# selenium v 3.141.0
# pandas v 0.23.4
# urllib3 v 1.23

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
import numpy as np


############ FUNCTIONS #############

def getChord(htmlInfo):
    # Takes in info shown below and returns chord i.e "A_maj"
    # '<div class="label-wrapper"><span class="chord-label label-A_maj"></span><span class="bass-label"></span></div>'
    if len(htmlInfo) > 100 and len(htmlInfo) < 130:
        # Finds the third instance of the dash and gives us the first coord to snip the chord from the string
        dashArray = findOccurrences(htmlInfo, '-')
        quoteArray = findOccurrences(htmlInfo, '"')
        # Finds the fourt instance of quotes and gives us the last coord to snip the chord from the string
        startSnip = dashArray[2]
        endSnip = quoteArray[3]
        chord = htmlInfo[startSnip+1:endSnip]
    else:
        chord = np.NaN
    return chord
    
def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def main(linkToSite):
    url = linkToSite

    browser = webdriver.Chrome()
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')

    #posts = soup.find_all(class_='chord')
    chords = soup.find_all(class_='label-wrapper')

    data = []
    for chord in chords:
        data.append(getChord(str(chord)))

    df = pd.DataFrame(data, columns=['Chords']).dropna()
    df.to_excel('chords.xlsx')
    browser.close()


chordifySite = f"https://chordify.net/chords/open-up-your-heart-handmade-moments-topic"
main(chordifySite)