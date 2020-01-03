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
            dash_array = self.find_occurrences(self.single_chord_data, '-')
            quote_array = self.find_occurrences(self.single_chord_data, '"')
            # Finds the third instance of the dash and gives us the first coordinate to snip the chord from the string
            startSnip = dash_array[2]
            # Finds the fourth instance of quotes and gives us the last coordinate to snip the chord from the string
            endSnip = quote_array[3]
            # Clean up the chord formatting with all the 
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
        # Takes website string data with chord and returns an array of the position of certain charaacters within the string
        # Then we use these coordinates to grab the chord
        return [i for i, letter in enumerate(string) if letter == char]