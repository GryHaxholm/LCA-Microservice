import json
import pandas as pd
import re
import numpy as np
from scipy.interpolate import interp1d
from app.resources import dataHandling
from app.services import Inter_Ekstra_Polation

#Working with the JSON files from the VC database
structuralElements = dataHandling.structuralElements
#Reading the LCA dataframe
LCA_Data = dataHandling.LCA_Data


wallsGWP_list= []
sumGWP_A1tilA3 = 0
sumGWP_C3 = 0
sumGWP_C4 = 0 
sumGWP_D = 0 
#GWP for Walls
if 'Wall' in structuralElements:
    for wall in structuralElements['Wall']:
        if wall['Material'] == "Concrete":
            if wall['Quality'] == "C20/25" or "C12/15" or "C16/20":
                WallGWPA1A3 = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['A1tilA3']
                WallGWP_C3 = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C3']
                WallGWP_C4 = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C4']
                WallGWP_D = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['D']
            elif wall['Quality'] == "C25/30":
                WallGWPA1A3 = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['A1tilA3']
                WallGWP_C3 = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C3']
                WallGWP_C4 = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C4']
                WallGWP_D = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['D']
            elif wall['Quality'] =="C30/37":
                WallGWPA1A3 = wall['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['A1tilA3']
                WallGWP_C3 = wall['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C3']
                WallGWP_C4 = wall['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C4']
                WallGWP_D = wall['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['D']
            elif wall['Quality'] == "C35/45":
                WallGWPA1A3 = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['A1tilA3']
                WallGWP_C3 = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C3']
                WallGWP_C4 = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C4']
                WallGWP_D = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['D']
            elif wall['Quality'] == "C40/50":
                WallGWPA1A3 = wall['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['A1tilA3']
                WallGWP_C3 = wall['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C3']
                WallGWP_C4 = wall['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C4']
                WallGWP_D = wall['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['D']
            elif wall['Quality'] == "C45/55":
                WallGWPA1A3 = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['A1tilA3']
                WallGWP_C3 = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['C3']
                WallGWP_C4 = (wall['Thickness']* wall['Area'])* LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['C4']
                WallGWP_D = (wall['Thickness']* wall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['D']
            else:
                WallGWPA1A3 = "Manual input needed"
                WallGWP_C3 = "Manual input needed"  
                WallGWP_C4 = "Manual input needed" 
                WallGWP_D = "Manual input needed" 
        elif wall['Material'] == "Timber":
            if 'C' in wall['Quality']:
                WallGWPA1A3 = wall['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran']['A1tilA3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran']['Massefaktor'])
                WallGWP_C3 = wall['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['Massefaktor'])
                WallGWP_C4 = wall['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C4'] / LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['Massefaktor'])
                WallGWP_D = wall['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['D'] / LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['Massefaktor'])
            elif 'GL' in wall['Quality']:
                WallGWPA1A3 = wall['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran']['A1tilA3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran']['Massefaktor'])
                WallGWP_C3 = wall['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['Massefaktor'])
                WallGWP_C4 = wall['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C4'] / LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['Massefaktor'])
                WallGWP_D = wall['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['D'] / LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['Massefaktor'])
            elif 'L(T)' in wall['Quality']:
                WallGWPA1A3 = wall['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ']['A1tilA3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ']['Massefaktor'])
                WallGWP_C3 = wall['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['Massefaktor'])
                WallGWP_C4 = wall['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C4'] / LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['Massefaktor'])
                WallGWP_D = wall['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['D'] / LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['Massefaktor'])
            else: 
                WallGWPA1A3 = "Manual input needed"
                WallGWP_C3 = "Manual input needed"
                WallGWP_C4 = "Manual input needed"
                WallGWP_D = "Manual input needed"
        elif wall['Material'] == "Reinforcement":
            WallGWPA1A3 = wall['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['A1tilA3']
            WallGWP_C3 = wall['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C3']
            WallGWP_C4 = wall['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C4']
            WallGWP_D = wall['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['D']
        else: 
            print(False)
        
        wallsGWP = {"TypeID":wall['TypeID'], "Material": wall['Material'], "Quality": wall['Quality'], "Area": wall['Area'], "Weight": wall['Weight'], "GWP_A1-A3": np.nansum(WallGWPA1A3), "GWP_C3": np.nansum(WallGWP_C3), "GWP_C4": np.nansum(WallGWP_C4), "GWP_D": np.nansum(WallGWP_D)}
        print(wallsGWP)
        sumGWP_A1tilA3 +=wallsGWP["GWP_A1-A3"]
        sumGWP_C3 +=wallsGWP["GWP_C3"]
        sumGWP_C4 +=wallsGWP["GWP_C4"]
        sumGWP_D +=wallsGWP["GWP_D"]
        wallForList = [wall['TypeID'],np.nansum(WallGWPA1A3), np.nansum(WallGWP_C3), np.nansum(WallGWP_C4), np.nansum(WallGWP_D)]
        wallsGWP_list.append(wallForList)


wallsGWP_Total = sumGWP_A1tilA3 + sumGWP_C3 + sumGWP_C4 + sumGWP_D 
print(sumGWP_A1tilA3, sumGWP_C3, sumGWP_C4, sumGWP_D)
print(wallsGWP_Total) 

wallsGWP_summed = {"A1-A3":sumGWP_A1tilA3, "C3":sumGWP_C3, "C4": sumGWP_C4, "D":sumGWP_D, "Total":wallsGWP_Total}
with open ("Walls_GWP.json","w") as outfile:
    json.dump(wallsGWP_summed, outfile, indent=2)
with open("Walls_list.json","w") as outfile:
    json.dump(wallsGWP_list, outfile, indent=1)