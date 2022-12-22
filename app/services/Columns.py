import json
import pandas as pd
import re
import numpy as np
from app.resources import dataHandling

#Working with the JSON files from the VC database
structuralElements = dataHandling.structuralElements
#Reading the LCA dataframe
LCA_Data = dataHandling.LCA_Data

columnsGWP_list= []
sumGWP_A1tilA3 = 0
sumGWP_C3 = 0
sumGWP_C4 = 0 
sumGWP_D = 0 
#GWP for Columns 
if 'Column' in structuralElements:
    for column in structuralElements['Column']:
        if column['Material'] == "Concrete":
            if column['Quality'] == "C20/25" or column['Quality']=="Concrete, C20/25" or column['Quality']=="C12/15" or column['Quality']=="Concrete, C12/15" or column['Quality']=="C16/20" or column['Quality']=="Concrete, C16/20":
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['D']
            elif column['Quality'] == "C25/30" or column['Quality'] =="Concrete, C25/30":
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['D']
            elif column['Quality'] == "30/37" or column['Quality'] == "Concrete, C30/37":
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['D']
            elif column['Quality']== "C35/45" or column['Quality'] == "Concrete, C35/45":
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['D']
            elif column['Quality'] == "C40/50" or column['Quality'] =="Concrete, C40/50":
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['D']
            elif column['Quality']== "C45/55" or column['Quality']=="Concrete, C45/55":
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C45/55 (Indvendig væg)']['D']
            else:
                ColumnGWPA1A3 = "Manual input needed"
                ColumnGWP_C3 = "Manual input needed"  
                ColumnGWP_C4 = "Manual input needed" 
                ColumnGWP_D = "Manual input needed" 
        elif column['Material'] == "Steel":
            ColumnGWPA1A3 = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Stål, valsede profiler og plader']['A1tilA3'] / 1000)
            ColumnGWP_C3 = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Stål, valsede profiler og plader']['C3'] / 1000)
            ColumnGWP_C4 = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Stål, valsede profiler og plader']['C4'] / 1000)
            ColumnGWP_D = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Stål, valsede profiler og plader']['D'] / 1000)
        elif column['Material'] == "Timber" or "Wood":
            if 'C' or 'Timber' in column['Quality']:
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['D'] 
            elif 'GL' or 'Glulam' in column['Quality']:
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C3'] 
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['D'] 
            elif 'L(T)' in column['Quality']:
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C4'] 
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['D']
            else: 
                ColumnGWPA1A3 = "Manual input needed"
                ColumnGWP_C3 = "Manual input needed"
                ColumnGWP_C4 = "Manual input needed"
                ColumnGWP_D = "Manual input needed"
        elif column['Material'] == "Reinforcement":
            ColumnGWPA1A3 = column['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['A1tilA3']
            ColumnGWP_C3 = column['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C3']
            ColumnGWP_C4 = column['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['C4']
            ColumnGWP_D = column['Weight'] * LCA_Data.loc[LCA_Data['Navn'] == "Armeringsnet"]['D']
        else: 
            print(False)
        

        columnGWP = {"TypeID":column['TypeID'], "Material": column['Material'], "Quality": column['Quality'], "Volume": column['Volume'], "GWP_A1-A3": np.nansum(ColumnGWPA1A3), "GWP_C3": np.nansum(ColumnGWP_C3), "GWP_C4": np.nansum(ColumnGWP_C4), "GWP_D": np.nansum(ColumnGWP_D)}
        print(columnGWP)
        sumGWP_A1tilA3 +=columnGWP["GWP_A1-A3"]
        sumGWP_C3 +=columnGWP["GWP_C3"]
        sumGWP_C4 +=columnGWP["GWP_C4"]
        sumGWP_D +=columnGWP["GWP_D"]
        columnForList = [column['TypeID'],np.nansum(ColumnGWPA1A3), np.nansum(ColumnGWP_C3), np.nansum(ColumnGWP_C4), np.nansum(ColumnGWP_D)]
        columnsGWP_list.append(columnForList)

columnGWP_Total = sumGWP_A1tilA3 + sumGWP_C3 + sumGWP_C4 + sumGWP_D 
print(sumGWP_A1tilA3, sumGWP_C3, sumGWP_C4, sumGWP_D)
print(columnGWP_Total) 

columnsGWP_summed = {"A1-A3":sumGWP_A1tilA3, "C3":sumGWP_C3, "C4": sumGWP_C4, "D":sumGWP_D, "Total":columnGWP_Total}
with open ("resultsFiles/Columns_GWP.json","w") as outfile:
    json.dump(columnsGWP_summed, outfile, indent=2)
with open("resultsFiles/Columns_list.json","w") as outfile:
    json.dump(columnsGWP_list, outfile, indent=1)