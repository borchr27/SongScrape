import pandas as pd
import time

def displayOutput():
    # Time.sleep value = tempo
    excel_file = 'chords.xlsx'
    df = pd.read_excel(excel_file)
    tempo = .5
    songLen = len(df['Chords'][:])
    i = 0
    y = '\t'
    while (i < songLen):
        j = 0
        while j < 8:
            print(df['Chords'][i+j] + '\t', end = ' ')
            j+=1
        print("\n", end = ' ')
        for x in range(0,8):
            if x == 0: print('| ', end = '\r')
            elif x == 8: 
                print(y*(x) + '  |', end='\r')
            else: print(y*(x) + '  |', end='\r')
            time.sleep(tempo)
        i+=8

displayOutput()
