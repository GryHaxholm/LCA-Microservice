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
#GWP for Columns 
if 'Column' in structuralElements:
    for column in structuralElements['Column']:
        if column['Material'] == "Concrete":
            if column['Quality'] == "C20/25" or "C12/15" or "C16/20":
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C20/25 SCC (indvendig væg)']['D']
            elif column['Quality'] == "C25/30":
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C20/25 SCC og C25/30) i eksponeringsklasserne X0 og XC1, Fabriksbeton C25/30 (indervæg)']['D']
            elif column['Quality'] =="C30/37":
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C30/37(Indvendig væg)']['D']
            elif column['Quality'] == "C35/45":
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton (C30/37, C35/45 SCC), C35/45SCC (gulv)']['D']
            elif column['Quality'] == "C40/50":
                ColumnGWPA1A3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['A1tilA3']
                ColumnGWP_C3 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C3']
                ColumnGWP_C4 = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['C4']
                ColumnGWP_D = column['Volume'] * LCA_Data.loc[LCA_Data['Navn'] == 'Fabriksbeton(C40/50, C45/55), C40/50 CEM I (Indvendig væg)']['D']
            elif column['Quality'] == "C45/55":
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
        elif column['Material'] == "Timber":
            if 'C' in column['Quality']:
                ColumnGWPA1A3 = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran']['A1tilA3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran']['Massefaktor'])
                ColumnGWP_C3 = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['Massefaktor'])
                ColumnGWP_C4 = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['C4'] / LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['Massefaktor'])
                ColumnGWP_D = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['D'] / LCA_Data.loc[LCA_Data['Navn'] == 'Høvlede konstruktionstræsprodukter af fyrog gran, Forbrænding']['Massefaktor'])
            elif 'GL' in column['Quality']:
                ColumnGWPA1A3 = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran']['A1tilA3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran']['Massefaktor'])
                ColumnGWP_C3 = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['Massefaktor'])
                ColumnGWP_C4 = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['C4'] / LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['Massefaktor'])
                ColumnGWP_D = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['D'] / LCA_Data.loc[LCA_Data['Navn'] == 'Limtræs-produkter af fyr og gran, Forbrænding']['Massefaktor'])
            elif 'L(T)' in column['Quality']:
                ColumnGWPA1A3 = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ']['A1tilA3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ']['Massefaktor'])
                ColumnGWP_C3 = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C3'] / LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['Massefaktor'])
                ColumnGWP_C4 = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['C4'] / LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['Massefaktor'])
                ColumnGWP_D = column['Weight'] * (LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['D'] / LCA_Data.loc[LCA_Data['Navn'] == 'Krydslamineret træ, Forbrænding']['Massefaktor'])
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
        

        columnGWP = {"TypeID":column['TypeID'], "Material": column['Material'], "Quality": column['Quality'], "Volume": column['Volume'], "Weight": column['Weight'], "GWP_A1-A3": np.nansum(ColumnGWPA1A3), "GWP_C3": np.nansum(ColumnGWP_C3), "GWP_C4": np.nansum(ColumnGWP_C4), "GWP_D": np.nansum(ColumnGWP_D)}
        print(columnGWP)
        sumGWP_A1tilA3 +=columnGWP["GWP_A1-A3"]
        sumGWP_C3 +=columnGWP["GWP_C3"]
        sumGWP_C4 +=columnGWP["GWP_C4"]
        sumGWP_D +=columnGWP["GWP_D"]

columnGWP_Total = sumGWP_A1tilA3 + sumGWP_C3 + sumGWP_C4 + sumGWP_D 
print(sumGWP_A1tilA3, sumGWP_C3, sumGWP_C4, sumGWP_D)
print(columnGWP_Total) 