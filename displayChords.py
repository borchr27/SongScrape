import pandas as pd
import time
excel_file = 'chords.xlsx'
songChords = pd.read_excel(excel_file)

# Add for loop here, print chords next to each other in a row, bigger font, pause for x seconds

songLen = len(songChords[0][:])
i = 0
while (i < songLen):
    j = 0
    while j < 9:
        print(songChords[0][i+j] + "  ", end = '')
        j+=1
    time.sleep(2)
    print(" ")
    i+=1