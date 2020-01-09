# Environment: anaconda cloud borchr27/songscrape
# bs4 v 4.6.3
# selenium v 3.141.0
# pandas v 0.23.4
# urllib3 v 1.23
import keyboard
import threading
import sys
from WebsiteScraper import WebsiteScraper
from DisplayOutput import DisplayOutput

def main():
    #url = input('Enter a chordify URL: \n')
    url = 'https://chordify.net/chords/buffalo-springfield-for-what-its-worth-buttholesurferss'
    new_scrape = WebsiteScraper(url)
    new_scrape.website_scraper()

    # Gets the youtube link for the song you are playing (CURRENTLY NOT GRABBING CORRECT LINK)
    new_youtube_link = new_scrape.youtube_link()
    print(new_youtube_link)

    # Plays the chords in the console window
    new_display = DisplayOutput()
    new_display.display_output()

# Press ESC to exit code
my_thread = threading.Thread(target = main, daemon=True).start()
keyboard.wait("esc")
sys.exit()

if __name__ == '__main__':
    main()

def notes():
    # A funtion merely to hold and hide some of the notes and tuts that were used to build this program
    pass
    # Helpful tuts for structuring program:
    # Classes: https://www.youtube.com/watch?v=m6hhUBXcA-E
    # Classes Cont: https://www.youtube.com/watch?v=apACNr7DC_s
    # Init / Name Method: https://www.youtube.com/watch?v=WIP3-woodlU
    # https://docs.quantifiedcode.com/python-anti-patterns/correctness/method_has_no_argument.html
    # https://www.python.org/dev/peps/pep-0008/#function-and-method-arguments
    # https://stackoverflow.com/questions/7670415/python-3-sharing-variables-between-methods-in-a-class
    # https://stackoverflow.com/questions/56622170/how-to-use-the-esc-key-to-end-the-program-at-any-point-go-back-to-previous-men