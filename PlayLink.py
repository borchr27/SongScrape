import vlc
import pafy

class PlayLink:
    """
    Opens the youtube link in a browser window
    """
    def __init__(self):
        pass
        
    def play_link(self, link):
        # Uses VLC and Pafy to play the video for the song you are playing!
        url = link
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
        while True: 
            pass