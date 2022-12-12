import json
import pandas as pd
import re
import numpy as np

#Working with the JSON files from the VC database (Or this case directly from the c# codes)
with open('app/resources/StructuralElements2.json') as f:
    structuralElements = json.load(f)

#Reading the LCA dataframe based on a .csv file
LCA_Data = pd.read_csv('app/resources/Table7.csv', sep=';')

#Converting relevant columns to floats
LCA_Data['A1tilA3'] = LCA_Data['A1tilA3'].astype(np.double)
LCA_Data['C3'] = LCA_Data['C3'].astype(np.double)
LCA_Data['C4'] = LCA_Data['C4'].astype(np.double)
LCA_Data['D'] = LCA_Data['D'].astype(np.double)
LCA_Data['Massefaktor'] = LCA_Data['Massefaktor'].str.replace(',','.')
LCA_Data['Massefaktor'] = LCA_Data['Massefaktor'].astype(np.double)