import numpy as np

class create_song_data:
    #takes the raw data from the chordify website example below and returns just the chord
    def __init__(self, singleChordData):
        self.singleChordData = singleChordData
        self.getChord(singleChordData)

    def getChord(self, singleChordData):
        # Takes in info shown below and returns chord i.e "A_maj"
        # '<div class="label-wrapper"><span class="chord-label label-A_maj"></span><span class="bass-label"></span></div>'
        if len(singleChordData) > 100 and len(singleChordData) < 130:
            # Finds the third instance of the dash and gives us the first coordinate to snip the chord from the string
            dashArray = self.findOccurrences(singleChordData, '-')
            quoteArray = self.findOccurrences(singleChordData, '"')
            # Finds the fourt instance of quotes and gives us the last coordinate to snip the chord from the string
            startSnip = dashArray[2]
            endSnip = quoteArray[3]
            chord = singleChordData[startSnip+1:endSnip]
            chord = chord.replace('min', 'm')
            chord = chord.replace('maj','')
            chord = chord.replace('s', '#')
            chord = chord.replace('_', '')
            chord = chord.replace('re#t', 'rest')
        else:
            chord = np.NaN
        return chord

    def findOccurrences(self, string, char):
        return [i for i, letter in enumerate(string) if letter == char]
