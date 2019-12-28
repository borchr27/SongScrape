# Environment: anaconda cloud borchr27/songscrape
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
import time


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
        chord = chord.replace('min', 'm')
        chord = chord.replace('maj','')
        chord = chord.replace('s', '#')
        chord = chord.replace('_', '')
        chord = chord.replace('re#t', 'rest')
    else:
        chord = np.NaN
    return chord
    
def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def main(url):
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

def displayOutput():
    # Time.sleep value = tempo
    excel_file = 'chords.xlsx'
    df = pd.read_excel(excel_file)
    tempo = .5
    songLen = len(df['Chords'][:])
    i = 0
    y = '\t'
    while (i < songLen):
        j = 0
        while j < 8:
            print(df['Chords'][i+j] + '\t', end = ' ')
            j+=1
        print("\n", end = ' ')
        for x in range(0,8):
            if x == 0: print('| ', end = '\r')
            elif x == 8: 
                print(y*(x) + '  |', end='\r')
            else: print(y*(x) + '  |', end='\r')
            time.sleep(tempo)
        i+=8


#chordifySite = f"https://chordify.net/chords/open-up-your-heart-handmade-moments-topic"
chordifySite = f"https://chordify.net/chords/rescue-by-alysha-brilla-on-ctv-live-regina-alysha-brilla"
#main(chordifySite)
displayOutput()