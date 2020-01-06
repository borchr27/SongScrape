class FindCharLoc:
    """
    Class used to find the location of a certain character in a string, returns an array with 
    the positions of that character (which is then used to snip the desired info)
    """
    def __init__(self):
        pass

    def find_char_loc(self, string, char):
        # Takes website string data with chord and returns an array of the position of certain charaacters within the string
        # Then we use these coordinates to grab the chord
        return [i for i, letter in enumerate(string) if letter == char]