import json
import pandas as pd
import re
import numpy as np
from scipy.interpolate import interp1d
from app.resources import dataHandling
from app.services import Inter_Ekstra_Polation_Walls

#Working with the JSON files from the VC database
structuralElements = dataHandling.structuralElements
#Reading the LCA dataframe
LCA_Data = dataHandling.LCA_Data

#for interpolation between 150 and 200 prefab walls
int_A1A3 = Inter_Ekstra_Polation_Walls.int_A1A3
int_C3 = Inter_Ekstra_Polation_Walls.int_C3
int_C4 = Inter_Ekstra_Polation_Walls.int_C4
int_D = Inter_Ekstra_Polation_Walls.int_D
#for extrapolating below 150 mm prefab walls
ext_A1A3 = Inter_Ekstra_Polation_Walls.ext_A1A3
ext_C3 = Inter_Ekstra_Polation_Walls.ext_C3
ext_C4 = Inter_Ekstra_Polation_Walls.ext_C4
ext_D = Inter_Ekstra_Polation_Walls.ext_D
#for extrapolating above 200mm prefab walls
ext_20_A1A3 = Inter_Ekstra_Polation_Walls.ext_20_A1A3
ext_20_C3 = Inter_Ekstra_Polation_Walls.ext_20_C3
ext_20_C4 = Inter_Ekstra_Polation_Walls.ext_20_C4
ext_20_D = Inter_Ekstra_Polation_Walls.ext_20_D

exteriorWallsGWP_list= []
sumGWP_A1tilA3 = 0
sumGWP_C3 = 0
sumGWP_C4 = 0 
sumGWP_D = 0 
#GWP for Walls
if 'ExteriorWall' in structuralElements:
    for exteriorWall in structuralElements['ExteriorWall']:
        if "Concrete" in exteriorWall['Material'] and ("Prefabricated" not in exteriorWall['Material'] and "Precast" not in exteriorWall['Material']):
            if  exteriorWall['Quality'] == "C20/25" or exteriorWall['Quality']=="Concrete, C20/25" or exteriorWall['Quality']=="C12/15" or exteriorWall['Quality']=="Concrete, C12/15" or exteriorWall['Quality']=="C16/20" or exteriorWall['Quality']=="Concrete, C16/20":
                ExteriorWallGWPA1A3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['A1tilA3']
                ExteriorWallGWP_C3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C3']
                ExteriorWallGWP_C4 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C4']
                ExteriorWallGWP_D = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['D']
            elif exteriorWall['Quality'] == "C25/30" or exteriorWall['Quality']=="Concrete, C25/30":
                ExteriorWallGWPA1A3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['A1tilA3']
                ExteriorWallGWP_C3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C3']
                ExteriorWallGWP_C4 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C4']
                ExteriorWallGWP_D = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['D']
            elif exteriorWall['Quality'] == "C30/37" or exteriorWall['Quality'] == "Concrete, C30/37":
                ExteriorWallGWPA1A3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['A1tilA3']
                ExteriorWallGWP_C3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C3']
                ExteriorWallGWP_C4 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C4']
                ExteriorWallGWP_D = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['D']
            elif exteriorWall['Quality']== "C35/45" or exteriorWall['Quality'] == "Concrete, C35/45":
                ExteriorWallGWPA1A3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['A1tilA3']
                ExteriorWallGWP_C3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C3']
                ExteriorWallGWP_C4 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C4']
                ExteriorWallGWP_D = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['D']
            elif exteriorWall['Quality'] == "C40/50" or exteriorWall['Quality'] =="Concrete, C40/50":
                ExteriorWallGWPA1A3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['A1tilA3']
                ExteriorWallGWP_C3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C3']
                ExteriorWallGWP_C4 = (exteriorWall['Thickness']* exteriorWall['Area'])* LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C4']
                ExteriorWallGWP_D = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['D']
            elif exteriorWall['Quality'] =="C45/55" or exteriorWall['Quality'] =="Concrete, C45/55":
                ExteriorWallGWPA1A3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['A1tilA3']
                ExteriorWallGWP_C3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['C3']
                ExteriorWallGWP_C4 = (exteriorWall['Thickness']* exteriorWall['Area'])* LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['C4']
                ExteriorWallGWP_D = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['D']
            else:
                ExteriorWallGWPA1A3 = "Manual input needed"
                ExteriorWallGWP_C3 = "Manual input needed"  
                ExteriorWallGWP_C4 = "Manual input needed" 
                ExteriorWallGWP_D = "Manual input needed" 
        elif "Prefabricated Concrete" in exteriorWall['Material'] or "Precast" in exteriorWall['Material']:
            if exteriorWall['Thickness'] == 0.15:
                ExteriorWallGWPA1A3 = exteriorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['A1tilA3']
                ExteriorWallGWP_C3 = exteriorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['C3']
                ExteriorWallGWP_C4 = exteriorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['C4']
                ExteriorWallGWP_D = exteriorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['D']
            elif exteriorWall['Thickness'] == 0.20:
                ExteriorWallGWPA1A3 = exteriorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 16-25 kg armering']['A1tilA3']
                ExteriorWallGWP_C3 = exteriorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 16-25 kg armering']['C3']
                ExteriorWallGWP_C4 = exteriorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 16-25 kg armering']['C4']
                ExteriorWallGWP_D = exteriorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 16-25 kg armering']['D']
            elif 0.15 < exteriorWall['Thickness'] < 0.20: 
                ExteriorWallGWPA1A3 = exteriorWall['Area'] * int_A1A3(exteriorWall['Thickness'])
                ExteriorWallGWP_C3 = exteriorWall['Area'] * int_C3(exteriorWall['Thickness'])
                ExteriorWallGWP_C4= exteriorWall['Area'] * int_C4(exteriorWall['Thickness'])
                ExteriorWallGWP_D = exteriorWall['Area'] * int_D(exteriorWall['Thickness'])
            elif exteriorWall['Thickness'] < 0.15: 
                ExteriorWallGWPA1A3 = exteriorWall['Area'] * ext_A1A3(exteriorWall['Thickness'])
                ExteriorWallGWP_C3 = exteriorWall['Area'] * ext_C3(exteriorWall['Thickness'])
                ExteriorWallGWP_C4= exteriorWall['Area'] * ext_C4(exteriorWall['Thickness'])
                ExteriorWallGWP_D = exteriorWall['Area'] * ext_D(exteriorWall['Thickness'])
            elif exteriorWall['Thickness'] >0.20:
                ExteriorWallGWPA1A3 = exteriorWall['Area'] * ext_20_A1A3(exteriorWall['Thickness'])
                ExteriorWallGWP_C3 = exteriorWall['Area'] * ext_20_C3(exteriorWall['Thickness'])
                ExteriorWallGWP_C4= exteriorWall['Area'] * ext_20_C4(exteriorWall['Thickness'])
                ExteriorWallGWP_D = exteriorWall['Area'] * ext_20_D(exteriorWall['Thickness'])
            else: 
                ExteriorWallGWPA1A3 = "Manual input needed"
                ExteriorWallGWP_C3 = "Manual input needed"  
                ExteriorWallGWP_C4 = "Manual input needed" 
                ExteriorWallGWP_D = "Manual input needed" 
        elif exteriorWall['Material'] == "Timber" or exteriorWall['Material'] == "Wood":
            if 'C' or 'Timber' in exteriorWall['Quality']:
                ExteriorWallGWPA1A3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran']['A1tilA3'] 
                ExteriorWallGWP_C3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C3'] 
                ExteriorWallGWP_C4 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C4'] 
                ExteriorWallGWP_D = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['D'] 
            elif 'GL' or 'Glulam' in exteriorWall['Quality']:
                ExteriorWallGWPA1A3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran']['A1tilA3']
                ExteriorWallGWP_C3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C3']
                ExteriorWallGWP_C4 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C4']
                ExteriorWallGWP_D = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['D'] 
                ExteriorWallGWPA1A3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ']['A1tilA3']
                ExteriorWallGWP_C3 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C3']
                ExteriorWallGWP_C4 = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C4']
                ExteriorWallGWP_D = (exteriorWall['Thickness']* exteriorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['D']
            else: 
                ExteriorWallGWPA1A3 = "Manual input needed"
                ExteriorWallGWP_C3 = "Manual input needed"
                ExteriorWallGWP_C4 = "Manual input needed"
                ExteriorWallGWP_D = "Manual input needed"
        elif exteriorWall['Material'] == "Reinforcement":
            ExteriorWallGWPA1A3 = exteriorWall['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['A1tilA3']
            ExteriorWallGWP_C3 = exteriorWall['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C3']
            ExteriorWallGWP_C4 = exteriorWall['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C4']
            ExteriorWallGWP_D = exteriorWall['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['D']
        else: 
            print(False)
        
        ExteriorwallsGWP = {"TypeID":exteriorWall['TypeID'], "Material": exteriorWall['Material'], "Quality": exteriorWall['Quality'], "Area": exteriorWall['Area'], "Thickness": exteriorWall['Thickness'], "GWP_A1-A3": np.nansum(ExteriorWallGWPA1A3), "GWP_C3": np.nansum(ExteriorWallGWP_C3), "GWP_C4": np.nansum(ExteriorWallGWP_C4), "GWP_D": np.nansum(ExteriorWallGWP_D)}
        print(ExteriorwallsGWP)
        sumGWP_A1tilA3 +=ExteriorwallsGWP["GWP_A1-A3"]
        sumGWP_C3 +=ExteriorwallsGWP["GWP_C3"]
        sumGWP_C4 +=ExteriorwallsGWP["GWP_C4"]
        sumGWP_D +=ExteriorwallsGWP["GWP_D"]
        exteriorWallForList = [exteriorWall['TypeID'],np.nansum(ExteriorWallGWPA1A3), np.nansum(ExteriorWallGWP_C3), np.nansum(ExteriorWallGWP_C4), np.nansum(ExteriorWallGWP_D)]
        exteriorWallsGWP_list.append(exteriorWallForList)


exteriorWallsGWP_Total = sumGWP_A1tilA3 + sumGWP_C3 + sumGWP_C4 + sumGWP_D 
print(sumGWP_A1tilA3, sumGWP_C3, sumGWP_C4, sumGWP_D)
print(exteriorWallsGWP_Total) 

exteriorWallsGWP_summed = {"A1-A3":sumGWP_A1tilA3, "C3":sumGWP_C3, "C4": sumGWP_C4, "D":sumGWP_D, "Total":exteriorWallsGWP_Total}
with open ("resultsFiles/ExteriorWalls_GWP.json","w") as outfile:
    json.dump(exteriorWallsGWP_summed, outfile, indent=2)
with open("resultsFiles/ExteriorWalls_list.json","w") as outfile:
    json.dump(exteriorWallsGWP_list, outfile, indent=1)