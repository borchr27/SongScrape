# Environment: anaconda cloud borchr27/songscrape
# bs4 v 4.6.3
# selenium v 3.141.0
# pandas v 0.23.4
# urllib3 v 1.23

from WebsiteScraper import WebsiteScraper
from DisplayOutput import DisplayOutput

def main():
    url = input('Please paste the chordify URL here: \n')
    song_data = WebsiteScraper(url)
    song_data.website_scraper()
    # Gets the youtube link for the song you are playing
    yt_link = song_data.youtube_link()
    print(yt_link)

    output_to_terminal = DisplayOutput()
    output_to_terminal.display_output()

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