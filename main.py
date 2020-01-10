# Environment: anaconda cloud borchr27/songscrape
# bs4 v 4.6.3
# selenium v 3.141.0
# pandas v 0.23.4
# urllib3 v 1.23
import keyboard
import threading
import sys
import time
from WebsiteScraper import WebsiteScraper
from PlayLink import PlayLink


def main():
    #url = input('Enter a chordify URL: \n')
    #url = 'https://chordify.net/chords/buffalo-springfield-for-what-its-worth-buttholesurferss'
    #new_scrape = WebsiteScraper(url)
    #new_scrape.website_scraper()
    new_play_link = PlayLink()
    # Gets the youtube link for the song you are playing (USE MULTIPROCESSING TO PLAY SONG AND CHORDS)
    thread_two = threading.Thread(new_play_link.play_link(), daemon=True).start()

# Press ESC to exit code
thread_one = threading.Thread(target=main, daemon=True).start()
keyboard.wait("esc")
sys.exit()

if __name__ == "__main__":
    main()

def notes():
    # A funtion merely to hold and hide some of the notes and tuts that were used to build this program
    pass
    # Helpful tuts for structuring program:
    # CLASSES https://www.youtube.com/watch?v=m6hhUBXcA-E
    # CLASSES CONT https://www.youtube.com/watch?v=apACNr7DC_s
    # INIT/NAME METHODS https://www.youtube.com/watch?v=WIP3-woodlU
    # METHODS https://docs.quantifiedcode.com/python-anti-patterns/correctness/method_has_no_argument.html
    # METHODS https://www.python.org/dev/peps/pep-0008/#function-and-method-arguments
    # SELF AND SHARING VARIABLES https://stackoverflow.com/questions/7670415/python-3-sharing-variables-between-methods-in-a-class
    # HIT ESC TO EXIT https://stackoverflow.com/questions/56622170/how-to-use-the-esc-key-to-end-the-program-at-any-point-go-back-to-previous-men
    # THREADING https://www.youtube.com/watch?time_continue=1&v=5JSloPGocSY&feature=emb_logo