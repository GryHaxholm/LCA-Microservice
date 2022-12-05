import pandas as pd
import re
import numpy as np

#Reading the dataframe based on a .csv file
LCA_Data = pd.read_csv('Table7.csv', sep=';')

#Converting relevant columns to floats
LCA_Data['A1tilA3'] = LCA_Data['A1tilA3'].astype(np.double)
LCA_Data['C3'] = LCA_Data['C3'].astype(np.double)
LCA_Data['C4'] = LCA_Data['C4'].astype(np.double)
LCA_Data['D'] = LCA_Data['D'].astype(np.double)

#Searching for materials based on key words. 
print(LCA_Data.loc[(LCA_Data['Navn'].str.contains('Fabriksbeton', na=False)) & (LCA_Data['Navn'].str.contains('C20/25', na=False))])
#print(LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) ieksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (fundament)'])

#fabriksbeton = (LCA_Data.loc[LCA_Data['Navn'].str.contains('Fabriksbeton', na=False)])
#print(fabriksbeton)

#FB_C2025_fundament = LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) ieksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (fundament)']
#GWP = FB_C2025_fundament['A1tilA3']*2
#print(GWP)

#Getting the GWP based on a name and multiplyed with a value (will later be value from JSON)
#GWP = LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) ieksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (fundament)']['A1tilA3']*2
#print(GWP)