import json
import pandas as pd
import re
import numpy as np
from scipy.interpolate import interp1d
from app.services import Inter_Ekstra_Polation

#Working with the JSON files from the VC databse (Or this case directly from the c# codes)
with open('StructuralElements2.json') as f:
    structuralElements = json.load(f)

#Reading the LCA dataframe based on a .csv file
LCA_Data = pd.read_csv('Table7.csv', sep=';')

#Converting relevant columns to floats
LCA_Data['A1tilA3'] = LCA_Data['A1tilA3'].astype(np.double)
LCA_Data['C3'] = LCA_Data['C3'].astype(np.double)
LCA_Data['C4'] = LCA_Data['C4'].astype(np.double)
LCA_Data['D'] = LCA_Data['D'].astype(np.double)
LCA_Data['Massefaktor'] = LCA_Data['Massefaktor'].str.replace(',','.')
LCA_Data['Massefaktor'] = LCA_Data['Massefaktor'].astype(np.double)

#for interpolation between 220 and 320 hollowcore deck
int_A1A3 = Inter_Ekstra_Polation.int_A1A3
int_C3 = Inter_Ekstra_Polation.int_C3
int_C4 = Inter_Ekstra_Polation.int_C4
int_D = Inter_Ekstra_Polation.int_D
#for extrapolating below 220 mm hollowcore deck
ext_A1A3 = Inter_Ekstra_Polation.ext_A1A3
ext_C3 = Inter_Ekstra_Polation.ext_C3
ext_C4 = Inter_Ekstra_Polation.ext_C4
ext_D = Inter_Ekstra_Polation.ext_D
#for extrapolating above 320mm hollowcore deck
ext_32_A1A3 = Inter_Ekstra_Polation.ext_32_A1A3
ext_32_C3 = Inter_Ekstra_Polation.ext_32_C3
ext_32_C4 = Inter_Ekstra_Polation.ext_32_C4
ext_32_D = Inter_Ekstra_Polation.ext_32_D


sumGWP_A1tilA3 = 0
sumGWP_C3 = 0
sumGWP_C4 = 0 
sumGWP_D = 0 
#GWP for Decks 
if 'Deck' in structuralElements:
    for deck in structuralElements['Deck']:
        if deck['Material'] == "Concrete":
            if deck['Quality'] == "C20/25" or "C12/15" or "C16/20":
                DeckGWPA1A3 = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['A1tilA3']
                DeckGWP_C3 = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C3']
                DeckGWP_C4 = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C4']
                DeckGWP_D = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['D']
            elif deck['Quality'] == "C25/30":
                DeckGWPA1A3 = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['A1tilA3']
                DeckGWP_C3 = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C3']
                DeckGWP_C4 = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C4']
                DeckGWP_D = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['D']
            elif deck['Quality'] =="C30/37":
                DeckGWPA1A3 = deck['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['A1tilA3']
                DeckGWP_C3 = deck['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C3']
                DeckGWP_C4 = deck['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C4']
                DeckGWP_D = deck['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['D']
            elif deck['Quality'] == "C35/45":
                DeckGWPA1A3 = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['A1tilA3']
                DeckGWP_C3 = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C3']
                DeckGWP_C4 = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C4']
                DeckGWP_D = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['D']
            elif deck['Quality'] == "C40/50":
                DeckGWPA1A3 = deck['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['A1tilA3']
                DeckGWP_C3 = deck['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C3']
                DeckGWP_C4 = deck['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C4']
                DeckGWP_D = deck['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['D']
            elif deck['Quality'] == "C45/55":
                DeckGWPA1A3 = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['A1tilA3']
                DeckGWP_C3 = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['C3']
                DeckGWP_C4 = (deck['Thickness']* deck['Area'])* LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['C4']
                DeckGWP_D = (deck['Thickness']* deck['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['D']
            else:
                DeckGWPA1A3 = "Manual input needed"
                DeckGWP_C3 = "Manual input needed"  
                DeckGWP_C4 = "Manual input needed" 
                DeckGWP_D = "Manual input needed" 
        elif deck['Material'] == "Prefabricated Concrete":
            if deck['Thickness'] == 0.22:
                DeckGWPA1A3 = deck['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 22 cm, 6-10 liner']['A1tilA3']
                DeckGWP_C3 = deck['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 22 cm, 6-10 liner']['C3']
                DeckGWP_C4 = deck['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 22 cm, 6-10 liner']['C4']
                DeckGWP_D = deck['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 22 cm, 6-10 liner']['D']
            elif deck['Thickness'] == 0.32:
                DeckGWPA1A3 = deck['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 32 cm, 11-17 liner']['A1tilA3']
                DeckGWP_C3 = deck['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 32 cm, 11-17 liner']['C3']
                DeckGWP_C4 = deck['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 32 cm, 11-17 liner']['C4']
                DeckGWP_D = deck['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 32 cm, 11-17 liner']['D']
            elif 0.22 < deck['Thickness'] < 0.32: 
                DeckGWPA1A3 = deck['Area'] * int_A1A3(deck['Thickness'])
                DeckGWP_C3 = deck['Area'] * int_C3(deck['Thickness'])
                DeckGWP_C4= deck['Area'] * int_C4(deck['Thickness'])
                DeckGWP_D = deck['Area'] * int_D(deck['Thickness'])
            elif deck['Thickness'] < 0.22: 
                DeckGWPA1A3 = deck['Area'] * ext_A1A3(deck['Thickness'])
                DeckGWP_C3 = deck['Area'] * ext_C3(deck['Thickness'])
                DeckGWP_C4= deck['Area'] * ext_C4(deck['Thickness'])
                DeckGWP_D = deck['Area'] * ext_D(deck['Thickness'])
            elif deck['Thickness'] >0.32:
                DeckGWPA1A3 = deck['Area'] * ext_32_A1A3(deck['Thickness'])
                DeckGWP_C3 = deck['Area'] * ext_32_C3(deck['Thickness'])
                DeckGWP_C4= deck['Area'] * ext_32_C4(deck['Thickness'])
                DeckGWP_D = deck['Area'] * ext_32_D(deck['Thickness'])
            else: 
                DeckGWPA1A3 = "Manual input needed"
                DeckGWP_C3 = "Manual input needed"  
                DeckGWP_C4 = "Manual input needed" 
                DeckGWP_D = "Manual input needed" 
        elif deck['Material'] == "Timber":
            if 'C' in deck['Quality']:
                DeckGWPA1A3 = deck['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran']['A1tilA3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran']['Massefaktor'])
                DeckGWP_C3 = deck['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['Massefaktor'])
                DeckGWP_C4 = deck['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C4'] / LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['Massefaktor'])
                DeckGWP_D = deck['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['D'] / LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['Massefaktor'])
            elif 'GL' in deck['Quality']:
                DeckGWPA1A3 = deck['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran']['A1tilA3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran']['Massefaktor'])
                DeckGWP_C3 = deck['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['Massefaktor'])
                DeckGWP_C4 = deck['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C4'] / LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['Massefaktor'])
                DeckGWP_D = deck['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['D'] / LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['Massefaktor'])
            elif 'L(T)' in deck ['Quality']:
                DeckGWPA1A3 = deck['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ']['A1tilA3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ']['Massefaktor'])
                DeckGWP_C3 = deck['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['Massefaktor'])
                DeckGWP_C4 = deck['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C4'] / LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['Massefaktor'])
                DeckGWP_D = deck['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['D'] / LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['Massefaktor'])
            else: 
                DeckGWPA1A3 = "Manual input needed"
                DeckGWP_C3 = "Manual input needed"
                DeckGWP_C4 = "Manual input needed"
                DeckGWP_D = "Manual input needed"
        elif deck['Material'] == "Reinforcement":
            DeckGWPA1A3 = deck['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['A1tilA3']
            DeckGWP_C3 = deck['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C3']
            DeckGWP_C4 = deck['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C4']
            DeckGWP_D = deck['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['D']
        else: 
            print(False)
        
        decksGWP = {"TypeID":deck['TypeID'], "Material": deck['Material'], "Quality": deck['Quality'], "Area": deck['Area'], "Weight": deck['Weight'], "GWP_A1-A3": np.nansum(DeckGWPA1A3), "GWP_C3": np.nansum(DeckGWP_C3), "GWP_C4": np.nansum(DeckGWP_C4), "GWP_D": np.nansum(DeckGWP_D)}
        print(decksGWP)
        sumGWP_A1tilA3 +=decksGWP["GWP_A1-A3"]
        sumGWP_C3 +=decksGWP["GWP_C3"]
        sumGWP_C4 +=decksGWP["GWP_C4"]
        sumGWP_D +=decksGWP["GWP_D"]

decksGWP_Total = sumGWP_A1tilA3 + sumGWP_C3 + sumGWP_C4 + sumGWP_D 
print(sumGWP_A1tilA3, sumGWP_C3, sumGWP_C4, sumGWP_D)
print(decksGWP_Total) 