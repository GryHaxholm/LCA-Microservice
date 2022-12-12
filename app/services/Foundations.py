import json
import pandas as pd
import re
import numpy as np
from app.resources import dataHandling

#Working with the JSON files from the VC database
structuralElements = dataHandling.structuralElements
#Reading the LCA dataframe
LCA_Data = dataHandling.LCA_Data

foundationsGWP_list= []
sumGWP_A1tilA3 = 0
sumGWP_C3 = 0
sumGWP_C4 = 0 
sumGWP_D = 0 
#GWP for Foundations 
if 'Foundation' in structuralElements:
    for foundation in structuralElements['Foundation']:
        if foundation['Material'] == "Concrete":
            if foundation['Quality'] == "C20/25" or "C12/15" or "C16/20":
                FoundationGWPA1A3 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (fundament)']['A1tilA3']
                FoundationGWP_C3 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (fundament)']['C3']
                FoundationGWP_C4 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (fundament)']['C4']
                FoundationGWP_D = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (fundament)']['D']
            elif foundation['Quality'] == "C25/30":
                FoundationGWPA1A3 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['A1tilA3']
                FoundationGWP_C3 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C3']
                FoundationGWP_C4 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C4']
                FoundationGWP_D = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['D']
            elif foundation['Quality'] =="C30/37":
                FoundationGWPA1A3 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['A1tilA3']
                FoundationGWP_C3 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C3']
                FoundationGWP_C4 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C4']
                FoundationGWP_D = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['D']
            elif foundation['Quality'] == "C35/45":
                FoundationGWPA1A3 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['A1tilA3']
                FoundationGWP_C3 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C3']
                FoundationGWP_C4 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C4']
                FoundationGWP_D = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['D']
            elif foundation['Quality'] == "C40/50":
                FoundationGWPA1A3 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Fundament)']['A1tilA3']
                FoundationGWP_C3 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Fundament)']['C3']
                FoundationGWP_C4 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Fundament)']['C4']
                FoundationGWP_D = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Fundament)']['D']
            elif foundation['Quality'] == "C45/55":
                FoundationGWPA1A3 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Fundament)']['A1tilA3']
                FoundationGWP_C3 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Fundament)']['C3']
                FoundationGWP_C4 = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Fundament)']['C4']
                FoundationGWP_D = foundation['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Fundament)']['D']
            else:
                FoundationGWPA1A3 = "Manual input needed"
                FoundationGWP_C3 = "Manual input needed"  
                FoundationGWP_C4 = "Manual input needed" 
                FoundationGWP_D = "Manual input needed" 
        elif foundation['Material'] == "Steel":
            FoundationGWPA1A3 = foundation['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Stål, valsede profiler og plader']['A1tilA3'] / 1000)
            FoundationGWP_C3 = foundation['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Stål, valsede profiler og plader']['C3'] / 1000)
            FoundationGWP_C4 = foundation['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Stål, valsede profiler og plader']['C4'] / 1000)
            FoundationGWP_D = foundation['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Stål, valsede profiler og plader']['D'] / 1000)
        elif foundation['Material'] == "Reinforcement":
            FoundationGWPA1A3 = foundation['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['A1tilA3']
            FoundationGWP_C3 = foundation['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C3']
            FoundationGWP_C4 = foundation['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C4']
            FoundationGWP_D = foundation['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['D']
        else: 
            print(False)
    
    foundationsGWP = {"TypeID":foundation['TypeID'], "Material": foundation['Material'], "Quality": foundation['Quality'], "Volume": foundation['Volume'], "Weight": foundation['Weight'], "GWP_A1-A3": np.nansum(BeamGWPA1A3), "GWP_C3": np.nansum(BeamGWP_C3), "GWP_C4": np.nansum(BeamGWP_C4), "GWP_D": np.nansum(BeamGWP_D)}
    print(foundationsGWP)
    sumGWP_A1tilA3 +=foundationsGWP["GWP_A1-A3"]
    sumGWP_C3 +=foundationsGWP["GWP_C3"]
    sumGWP_C4 +=foundationsGWP["GWP_C4"]
    sumGWP_D +=foundationsGWP["GWP_D"]
    foundationsForList = [foundation['TypeID'],np.nansum(FoundationGWPA1A3), np.nansum(FoundationGWP_C3), np.nansum(FoundationGWP_C4), np.nansum(FoundationGWP_D)]
    foundationsGWP_list.append(foundationsForList)

foundationsGWP_Total = sumGWP_A1tilA3 + sumGWP_C3 + sumGWP_C4 + sumGWP_D 
print(sumGWP_A1tilA3, sumGWP_C3, sumGWP_C4, sumGWP_D)
print(foundationsGWP_Total) 

foundationsGWP_summed = {"A1-A3":sumGWP_A1tilA3, "C3":sumGWP_C3, "C4": sumGWP_C4, "D":sumGWP_D, "Total":foundationsGWP_Total}
with open ("Foundations_GWP.json","w") as outfile:
    json.dump(foundationsGWP_summed, outfile, indent=2)
with open("Foundations_list.json","w") as outfile:
    json.dump(foundationsGWP_list, outfile, indent=1)