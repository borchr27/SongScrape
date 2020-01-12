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
        # Below used for threading
        super(PlayLink, self).__init__()
        
    def play_link(self):
        # Uses VLC and Pafy to play the video for the song you are playing!
        new_display = DisplayOutput()
        link_file = open("YoutubeLink.txt", "r")
        url = link_file.read()
        link_file.close()
        video = pafy.new(url)
        video_length = video.length
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
        time.sleep(1.5)
        while True: 
            # Plays the chords in the console window
            thread_three = threading.Thread(new_display.display_output(video_length), daemon=True).start()