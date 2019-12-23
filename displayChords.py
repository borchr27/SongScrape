import pandas as pd
import time
excel_file = 'chords.xlsx'
df = pd.read_excel(excel_file)

# Add for loop here, print chords next to each other in a row, bigger font, pause for x seconds


songLen = len(df['Chords'][:])
print(songLen)
i = 0
y = '            '
while (i < songLen):
    j = 0
    while j < 8:
        print(df['Chords'][i+j] + '     ', end = ' ')
        j+=1
    print("\n", end = ' ')
    for x in range(0,8):
        if x == 0: print('  ' + '|', end = '\r')
        else: print(y*(x) + '|', end='\r')
        time.sleep(.75)
    print(' ')
    i+=8
