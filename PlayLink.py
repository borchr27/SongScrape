import vlc
import pafy
import threading
import time
from DisplayOutput import DisplayOutput

class PlayLink(threading.Thread):
    """
    Opens the youtube link in a browser window
    """
    def __init__(self):
        super(PlayLink, self).__init__()
        
    def play_link(self):
        # Uses VLC and Pafy to play the video for the song you are playing!
        new_display = DisplayOutput()
        link_file = open("Link.txt", "r")
        link = link_file.read()
        link_file.close()
        url = link
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
        time.sleep(3)
        while True: 
            t2 = threading.Thread(new_display.display_output(), daemon=True).start()