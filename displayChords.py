import pandas as pd
excel_file = 'chords.xlsx'
songChords = pd.read_excel(excel_file)

songChords.head()