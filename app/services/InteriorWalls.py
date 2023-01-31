import json
import numpy as np
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

#Initializing list for interior walls
interiorWallsGWP_list= []
#Initialising summing values
sumGWP_A1tilA3 = 0
sumGWP_C3 = 0
sumGWP_C4 = 0 
sumGWP_D = 0 
#GWP for Walls
if 'InteriorWall' in structuralElements:
    for interiorWall in structuralElements['InteriorWall']:
        if "Concrete" in interiorWall['Material'] and ("Prefabricated" not in interiorWall['Material'] and "Precast" not in interiorWall['Material']):
            if  interiorWall['Quality'] == "C20/25" or interiorWall['Quality']=="Concrete, C20/25" or interiorWall['Quality']=="C12/15" or interiorWall['Quality']=="Concrete, C12/15" or interiorWall['Quality']=="C16/20" or interiorWall['Quality']=="Concrete, C16/20":
                InteriorWallGWPA1A3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['A1tilA3']
                InteriorWallGWP_C3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C3']
                InteriorWallGWP_C4 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C4']
                InteriorWallGWP_D = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['D']
            elif interiorWall['Quality'] == "C25/30" or interiorWall['Quality']=="Concrete, C25/30":
                InteriorWallGWPA1A3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['A1tilA3']
                InteriorWallGWP_C3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C3']
                InteriorWallGWP_C4 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C4']
                InteriorWallGWP_D = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['D']
            elif interiorWall['Quality'] == "30/37" or interiorWall['Quality'] == "Concrete, C30/37":
                InteriorWallGWPA1A3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['A1tilA3']
                InteriorWallGWP_C3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C3']
                InteriorWallGWP_C4 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C4']
                InteriorWallGWP_D = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['D']
            elif interiorWall['Quality']== "C35/45" or interiorWall['Quality'] == "Concrete, C35/45":
                InteriorWallGWPA1A3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['A1tilA3']
                InteriorWallGWP_C3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C3']
                InteriorWallGWP_C4 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C4']
                InteriorWallGWP_D = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['D']
            elif interiorWall['Quality'] == "C40/50" or interiorWall['Quality'] =="Concrete, C40/50":
                InteriorWallGWPA1A3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['A1tilA3']
                InteriorWallGWP_C3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C3']
                InteriorWallGWP_C4 = (interiorWall['Thickness']* interiorWall['Area'])* LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C4']
                InteriorWallGWP_D = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['D']
            elif interiorWall['Quality'] =="C45/55" or interiorWall['Quality'] =="Concrete, C45/55":
                InteriorWallGWPA1A3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['A1tilA3']
                InteriorWallGWP_C3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['C3']
                InteriorWallGWP_C4 = (interiorWall['Thickness']* interiorWall['Area'])* LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['C4']
                InteriorWallGWP_D = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['D']
            else:
                InteriorWallGWPA1A3 = "Manual input needed"
                InteriorWallGWP_C3 = "Manual input needed"  
                InteriorWallGWP_C4 = "Manual input needed" 
                InteriorWallGWP_D = "Manual input needed" 
        elif "Prefabricated" or "Precast" in interiorWall['Material']:
            if interiorWall['Thickness'] == 0.15:
                InteriorWallGWPA1A3 = interiorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['A1tilA3']
                InteriorWallGWP_C3 = interiorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['C3']
                InteriorWallGWP_C4 = interiorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['C4']
                InteriorWallGWP_D = interiorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['D']
            elif interiorWall['Thickness'] == 0.20:
                InteriorWallGWPA1A3 = interiorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 16-25 kg armering']['A1tilA3']
                InteriorWallGWP_C3 = interiorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 16-25 kg armering']['C3']
                InteriorWallGWP_C4 = interiorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 16-25 kg armering']['C4']
                InteriorWallGWP_D = interiorWall['Area'] * LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 16-25 kg armering']['D']
            elif 0.15 < interiorWall['Thickness'] < 0.20: 
                InteriorWallGWPA1A3 = interiorWall['Area'] * int_A1A3(interiorWall['Thickness'])
                InteriorWallGWP_C3 = interiorWall['Area'] * int_C3(interiorWall['Thickness'])
                InteriorWallGWP_C4= interiorWall['Area'] * int_C4(interiorWall['Thickness'])
                InteriorWallGWP_D = interiorWall['Area'] * int_D(interiorWall['Thickness'])
            elif interiorWall['Thickness'] < 0.15: 
                InteriorWallGWPA1A3 = interiorWall['Area'] * ext_A1A3(interiorWall['Thickness'])
                InteriorWallGWP_C3 = interiorWall['Area'] * ext_C3(interiorWall['Thickness'])
                InteriorWallGWP_C4= interiorWall['Area'] * ext_C4(interiorWall['Thickness'])
                InteriorWallGWP_D = interiorWall['Area'] * ext_D(interiorWall['Thickness'])
            elif interiorWall['Thickness'] >0.20:
                InteriorWallGWPA1A3 = interiorWall['Area'] * ext_20_A1A3(interiorWall['Thickness'])
                InteriorWallGWP_C3 = interiorWall['Area'] * ext_20_C3(interiorWall['Thickness'])
                InteriorWallGWP_C4= interiorWall['Area'] * ext_20_C4(interiorWall['Thickness'])
                InteriorWallGWP_D = interiorWall['Area'] * ext_20_D(interiorWall['Thickness'])
            else: 
                InteriorWallGWPA1A3 = "Manual input needed"
                InteriorWallGWP_C3 = "Manual input needed"  
                InteriorWallGWP_C4 = "Manual input needed" 
                InteriorWallGWP_D = "Manual input needed" 
        elif interiorWall['Material'] == "Timber" or "Wood":
            if 'C' or 'Timber' in interiorWall['Quality']:
                InteriorWallGWPA1A3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran']['A1tilA3'] 
                InteriorWallGWP_C3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C3'] 
                InteriorWallGWP_C4 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C4'] 
                InteriorWallGWP_D = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['D'] 
            elif 'GL' or 'Glulam' in interiorWall['Quality']:
                InteriorWallGWPA1A3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran']['A1tilA3']
                InteriorWallGWP_C3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C3']
                InteriorWallGWP_C4 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C4']
                InteriorWallGWP_D = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['D'] 
                InteriorWallGWPA1A3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ']['A1tilA3']
                InteriorWallGWP_C3 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C3']
                InteriorWallGWP_C4 = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C4']
                InteriorWallGWP_D = (interiorWall['Thickness']* interiorWall['Area']) * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['D']
            else: 
                InteriorWallGWPA1A3 = "Manual input needed"
                InteriorWallGWP_C3 = "Manual input needed"
                InteriorWallGWP_C4 = "Manual input needed"
                InteriorWallGWP_D = "Manual input needed"
        elif interiorWall['Material'] == "Reinforcement":
            InteriorWallGWPA1A3 = interiorWall['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['A1tilA3']
            InteriorWallGWP_C3 = interiorWall['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C3']
            InteriorWallGWP_C4 = interiorWall['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C4']
            InteriorWallGWP_D = interiorWall['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['D']
        else: 
            print(False)
        
        InteriorwallsGWP = {"TypeID":interiorWall['TypeID'], "Material": interiorWall['Material'], "Quality": interiorWall['Quality'], "Area": interiorWall['Area'], "Thickness": interiorWall['Thickness'], "GWP_A1-A3": np.nansum(InteriorWallGWPA1A3), "GWP_C3": np.nansum(InteriorWallGWP_C3), "GWP_C4": np.nansum(InteriorWallGWP_C4), "GWP_D": np.nansum(InteriorWallGWP_D)}
        print(InteriorwallsGWP)
        sumGWP_A1tilA3 +=InteriorwallsGWP["GWP_A1-A3"]
        sumGWP_C3 +=InteriorwallsGWP["GWP_C3"]
        sumGWP_C4 +=InteriorwallsGWP["GWP_C4"]
        sumGWP_D +=InteriorwallsGWP["GWP_D"]
        interiorWallForList = [interiorWall['TypeID'],np.nansum(InteriorWallGWPA1A3), np.nansum(InteriorWallGWP_C3), np.nansum(InteriorWallGWP_C4), np.nansum(InteriorWallGWP_D)]
        interiorWallsGWP_list.append(interiorWallForList)


interiorWallsGWP_Total = sumGWP_A1tilA3 + sumGWP_C3 + sumGWP_C4 + sumGWP_D 
print(sumGWP_A1tilA3, sumGWP_C3, sumGWP_C4, sumGWP_D)
print(interiorWallsGWP_Total) 

interiorWallsGWP_summed = {"A1-A3":sumGWP_A1tilA3, "C3":sumGWP_C3, "C4": sumGWP_C4, "D":sumGWP_D, "Total":interiorWallsGWP_Total}
with open ("resultsFiles/InteriorWalls_GWP.json","w") as outfile:
    json.dump(interiorWallsGWP_summed, outfile, indent=2)
with open("resultsFiles/InteriorWalls_list.json","w") as outfile:
    json.dump(interiorWallsGWP_list, outfile, indent=1)