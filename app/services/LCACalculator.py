import json
import pandas as pd
import re
import numpy as np

#Working with the JSON files from the VC databse (Or this case directly from the c# codes)
with open('structuralElements.json') as f:
    structuralElements = json.load(f)

#Reading the LCA dataframe based on a .csv file
LCA_Data = pd.read_csv('Table.csv', sep=';')

#Converting relevant columns to floats
LCA_Data['A1tilA3'] = LCA_Data['A1tilA3'].astype(np.double)
LCA_Data['C3'] = LCA_Data['C3'].astype(np.double)
LCA_Data['C4'] = LCA_Data['C4'].astype(np.double)
LCA_Data['D'] = LCA_Data['D'].astype(np.double)

#A1-A3
for deck in structuralElements['Deck']:
    if deck['MaterialID'] == "Concrete":
        deckGWP = deck['Area'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (fundament)']['A1tilA3']
    elif deck['MaterialID'] == "Stone":
        deckGWP = deck['Area']*2
    elif deck['MaterialID'] == "<By Category>":
        deckGWP = deck['Area']*2
    else: 
        print(False)
    deckList = {"TypeID":deck['TypeID'], "MaterialID": deck['MaterialID'], "Area": deck['Area'], "GWP A1-A3": deckGWP}
    print(deckList)
