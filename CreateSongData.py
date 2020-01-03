import numpy as np

class CreateSongData:
    """
    Takes the raw data from the chordify website (example below) 
    and returns just the chord, all cleaned up
    """
    
    def __init__(self, single_chord_data):
        self.single_chord_data = single_chord_data

    def get_chord(self):
        # Takes in info shown below and returns chord i.e "A_maj"
        # '<div class="label-wrapper"><span class="chord-label label-A_maj"></span><span class="bass-label"></span></div>'
        if len(self.single_chord_data) > 100 and len(self.single_chord_data) < 130:
            # Finds the third instance of the dash and gives us the first coordinate to snip the chord from the string
            dashArray = self.find_occurrences(self.single_chord_data, '-')
            quoteArray = self.find_occurrences(self.single_chord_data, '"')
            # Finds the fourt instance of quotes and gives us the last coordinate to snip the chord from the string
            startSnip = dashArray[2]
            endSnip = quoteArray[3]
            chord = self.single_chord_data[startSnip+1:endSnip]
            chord = chord.replace('min', 'm')
            chord = chord.replace('maj','')
            chord = chord.replace('s', '#')
            chord = chord.replace('_', '')
            chord = chord.replace('re#t', 'rest')
        else:
            chord = np.NaN
        return chord

    def find_occurrences(self, string, char):
        return [i for i, letter in enumerate(string) if letter == char]
