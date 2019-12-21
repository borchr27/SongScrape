import pandas as pd
excel_file = 'chords.xlsx'
songChords = pd.read_excel(excel_file)

# Add for loop here, print chords next to each other in a row, bigger font, pause for x seconds
i = 0
print(songChords[0][i:i+8])