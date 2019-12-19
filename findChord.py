text = '<div class="label-wrapper"><span class="chord-label label-A_maj"></span><span class="bass-label"></span></div>'
text2 = 'sadmked'


def getChord(htmlInfo):
    # Takes in info shown below and returns chord i.e "A_maj"
    # '<div class="label-wrapper"><span class="chord-label label-A_maj"></span><span class="bass-label"></span></div>'
    if len(htmlInfo) > 100 and len(htmlInfo) < 130:
        # Finds the third instance of the dash and gives us the first coord to snip the chord from the string
        dashArray = findOccurrences(htmlInfo, '-')
        quoteArray = findOccurrences(htmlInfo, '"')
        # Finds the fourt instance of quotes and gives us the last coord to snip the chord from the string
        startSnip = dashArray[2]
        endSnip = quoteArray[3]
        chord = htmlInfo[startSnip+1:endSnip]
    else:
        chord = ' test '
    return chord
    
def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


print(getChord(text))