import json
import pandas as pd
import re
import numpy as np

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

foundationsGWP_Total = sumGWP_A1tilA3 + sumGWP_C3 + sumGWP_C4 + sumGWP_D 
print(sumGWP_A1tilA3, sumGWP_C3, sumGWP_C4, sumGWP_D)
print(foundationsGWP_Total) 