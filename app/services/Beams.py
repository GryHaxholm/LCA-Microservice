import json
import numpy as np
from app.resources import dataHandling

#Working with the JSON files from the STR elements database
structuralElements = dataHandling.structuralElements
#Reading the LCA dataframe
LCA_Data = dataHandling.LCA_Data

#Initializing list for beams
beamsGWP_list= []
#Initialising summing values
sumGWP_A1tilA3 = 0
sumGWP_C3 = 0
sumGWP_C4 = 0 
sumGWP_D = 0 
#GWP for Beams  
if 'Beam' in structuralElements:
    for beam in structuralElements['Beam']:
        if beam['Material'] == "Concrete":
            if beam['Quality'] == "C20/25" or beam['Quality']=="Concrete, C20/25" or beam['Quality']=="C12/15" or beam['Quality']=="Concrete, C12/15" or beam['Quality']=="C16/20" or beam['Quality']=="Concrete, C16/20":
                BeamGWPA1A3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['A1tilA3']
                BeamGWP_C3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C3']
                BeamGWP_C4 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C4']
                BeamGWP_D = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['D']
            elif beam['Quality'] == "C25/30" or beam['Quality'] =="Concrete, C25/30":
                BeamGWPA1A3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['A1tilA3']
                BeamGWP_C3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C3']
                BeamGWP_C4 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C4']
                BeamGWP_D = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['D']
            elif beam['Quality'] == "C30/37" or beam['Quality'] == "Concrete, C30/37":
                BeamGWPA1A3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['A1tilA3']
                BeamGWP_C3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C3']
                BeamGWP_C4 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C4']
                BeamGWP_D = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['D']
            elif beam['Quality']== "C35/45" or beam['Quality'] == "Concrete, C35/45":
                BeamGWPA1A3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (Indvendig væg)']['A1tilA3']
                BeamGWP_C3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (Indvendig væg)']['C3']
                BeamGWP_C4 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (Indvendig væg)']['C4']
                BeamGWP_D = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (Indvendig væg)']['D']
            elif beam['Quality'] == "C40/50" or beam['Quality'] =="Concrete, C40/50":
                BeamGWPA1A3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['A1tilA3']
                BeamGWP_C3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C3']
                BeamGWP_C4 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C4']
                BeamGWP_D = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['D']
            elif beam['Quality']== "C45/55" or beam['Quality']=="Concrete, C45/55":
                BeamGWPA1A3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['A1tilA3']
                BeamGWP_C3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['C3']
                BeamGWP_C4 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['C4']
                BeamGWP_D = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['D']
            else:
                BeamGWPA1A3 = "Manual input needed"
                BeamGWP_C3 = "Manual input needed"  
                BeamGWP_C4 = "Manual input needed" 
                BeamGWP_D = "Manual input needed" 
        elif beam['Material'] == "Steel":
            BeamGWPA1A3 = beam['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Stål, valsede profiler og plader']['A1tilA3'] / 1000)
            BeamGWP_C3 = beam['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Stål, valsede profiler og plader']['C3'] / 1000)
            BeamGWP_C4 = beam['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Stål, valsede profiler og plader']['C4'] / 1000)
            BeamGWP_D = beam['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Stål, valsede profiler og plader']['D'] / 1000)
        elif beam['Material'] == "Timber" or beam['Material'] == "Wood":
            if 'C' in beam['Quality'] or "D" in beam['Quality'] or 'Timber' in beam['Quality'] or 'Lumber' in beam['Quality']:
                BeamGWPA1A3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran']['A1tilA3']
                BeamGWP_C3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C3']
                BeamGWP_C4 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C4']
                BeamGWP_D = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['D']
            elif 'GL' in beam['Quality'] or 'Glulam' in beam['Quality']:
                BeamGWPA1A3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran']['A1tilA3']
                BeamGWP_C3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C3']
                BeamGWP_C4 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C4']
                BeamGWP_D = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['D']
            elif 'L(T)' in beam['Quality'] in beam ['Quality']:
                BeamGWPA1A3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ']['A1tilA3']
                BeamGWP_C3 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C3']
                BeamGWP_C4 = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C4']
                BeamGWP_D = beam['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['D']
            else: 
                BeamGWPA1A3 = "Manual input needed"
                BeamGWP_C3 = "Manual input needed"
                BeamGWP_C4 = "Manual input needed"
                BeamGWP_D = "Manual input needed"
        elif beam['Material'] == "Reinforcement":
            BeamGWPA1A3 = beam['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['A1tilA3']
            BeamGWP_C3 = beam['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C3']
            BeamGWP_C4 = beam['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C4']
            BeamGWP_D = beam['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['D']
        elif beam['Material'] == "Other" and beam['Quality'] == "Aluminum":
            BeamGWPA1A3 = beam['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Aluminiumsprofil"]['A1tilA3']
            BeamGWP_C3 = beam['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Aluminium, plade og profil, Genanvendelse"]['C3']
            BeamGWP_C4 = beam['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Aluminium, plade og profil, Genanvendelse"]['C4']
            BeamGWP_D = beam['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Aluminium, plade og profil, Genanvendelse"]['D']   
        else: 
            print(False)

        beamsGWP = {"TypeID":beam['TypeID'], "Material": beam['Material'], "Quality": beam['Quality'], "Volume": beam['Volume'], "GWP_A1-A3": np.nansum(BeamGWPA1A3), "GWP_C3": np.nansum(BeamGWP_C3), "GWP_C4": np.nansum(BeamGWP_C4), "GWP_D": np.nansum(BeamGWP_D)}
        print(beamsGWP)
        sumGWP_A1tilA3 +=beamsGWP["GWP_A1-A3"]
        sumGWP_C3 +=beamsGWP["GWP_C3"]
        sumGWP_C4 +=beamsGWP["GWP_C4"]
        sumGWP_D +=beamsGWP["GWP_D"]
        beamForList = [beam['TypeID'],np.nansum(BeamGWPA1A3), np.nansum(BeamGWP_C3), np.nansum(BeamGWP_C4), np.nansum(BeamGWP_D)]
        beamsGWP_list.append(beamForList)
        

beamsGWP_Total = sumGWP_A1tilA3 + sumGWP_C3 + sumGWP_C4 + sumGWP_D 
print(sumGWP_A1tilA3, sumGWP_C3, sumGWP_C4, sumGWP_D)
print(beamsGWP_Total) 
print(beamsGWP_list)

beamsGWP_summed = {"A1-A3":sumGWP_A1tilA3, "C3":sumGWP_C3, "C4": sumGWP_C4, "D":sumGWP_D, "Total":beamsGWP_Total}
with open ("resultsFiles/Beams_GWP.json","w") as outfile:
    json.dump(beamsGWP_summed, outfile, indent=2)
with open("resultsFiles/Beams_list.json","w") as outfile:
    json.dump(beamsGWP_list, outfile, indent=1)