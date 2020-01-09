import pandas as pd
from datetime import date
import time

class DisplayOutput:
    """
    Takes the chords from the excel file and ouputs two measures (8 chords)
    then the class moves the vertical bar under the notes at a certain tempo
    """
    def __init__(self):
        pass

    def display_output(self):
        # Time.sleep value = tempo
        excel_file = 'chords.xlsx'
        data_frame = pd.read_excel(excel_file)
        tempo = .25
        data_frame_length = len(data_frame['Chords'][:])
        i = 0
        y = '\t'
        while (i < data_frame_length):
            j = 0
            while j < 8:
                print(data_frame['Chords'][i+j] + '\t', end = ' ')
                j+=1
            print("\n", end = ' ')
            for x in range(0,8):
                if x == 0: print('| ', end = '\r')
                elif x == 8: 
                    print(y*(x) + '  |', end='\r')
                else: print(y*(x) + '  |', end='\r')
                time.sleep(tempo)
            i+=8