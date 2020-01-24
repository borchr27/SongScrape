# Environment: anaconda cloud borchr27/songscrape
import keyboard
import threading
import sys
import time
from WebsiteScraper import WebsiteScraper
from PlayLink import PlayLink


def main():
    url = input('Enter a chordify URL: \n')
    #url = 'https://chordify.net/chords/buffalo-springfield-for-what-its-worth-good-sound-quality-circle2491'
    new_scrape = WebsiteScraper(url)
    new_scrape.website_scraper()
    new_play_link = PlayLink()
    # Gets the youtube link for the song you are playing
    thread_two = threading.Thread(new_play_link.play_link(), daemon=True).start()

# Thread allows us to exit program by pressing ESC

if __name__ == "__main__":
    main()

thread_one = threading.Thread(target=main, daemon=True).start() 
keyboard.wait("esc")
sys.exit()