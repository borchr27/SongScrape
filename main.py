from WebsiteScraper import WebsiteScraper
from DisplayOutput import DisplayOutput

def main():
    #url = input('Please paste the chordify URL here: \n')
    #song_data = WebsiteScraper(url)
    #song_data.website_scraper()

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