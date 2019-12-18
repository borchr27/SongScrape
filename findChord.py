text = '<div class="label-wrapper"><span class="chord-label label-A_maj"></span><span class="bass-label"></span></div>'

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

# Finds the third instance of the dash and gives us the first coord to snip the chord from the string
dashArray = findOccurrences(text, '-')
dashArray[2]

# Finds the fourt instance of quotes and gives us the last coord to snip the chord from the string
quoteArray = findOccurrences(text, '"')
quoteArray[4]

