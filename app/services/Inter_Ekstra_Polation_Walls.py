from scipy.interpolate import interp1d
from app.resources import dataHandling

#Working with the JSON files from the STR elements database
structuralElements = dataHandling.structuralElements
#Reading the LCA dataframe
LCA_Data = dataHandling.LCA_Data

#for interpolation between 150 and 200 prefab walls
x_data = (0.15,0.20)
y_A1A3 = (sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['A1tilA3']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 5-15 kg armering']['A1tilA3']))
y_C3 = (sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['C3']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 5-15 kg armering']['C3']))
y_C4 = (sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['C4']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 5-15 kg armering']['C4']))
y_D=(sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['D']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 5-15 kg armering']['D']))
int_A1A3 = interp1d(x_data, y_A1A3, 'linear')
int_C3 = interp1d(x_data, y_C3, 'linear')
int_C4 = interp1d(x_data, y_C4, 'linear')
int_D = interp1d(x_data, y_D, 'linear')

#for extrapolating below 150 mm prefab walls
ext_A1A3 = interp1d(x_data, y_A1A3, 'linear', fill_value='extrapolate')
ext_C3 = interp1d(x_data, y_C3, 'linear', fill_value='extrapolate')
ext_C4 = interp1d(x_data, y_C4, 'linear', fill_value='extrapolate')
ext_D = interp1d(x_data, y_D, 'linear', fill_value='extrapolate')

#for extrapolating above 200 mm prefab walls
x_data = (0.15,0.20)
y_A1A3_20 = (sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['A1tilA3']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 16-25 kg armering']['A1tilA3']))
y_C3_20 = (sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['C3']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 16-25 kg armering']['C3']))
y_C4_20 = (sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['C4']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 16-25 kg armering']['C4']))
y_D_20=(sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 15 cm tyk væg med 5-15 kg armering']['D']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Beton vægelementer, Beton vægelementer, 20 cm tyk væg, med 16-25 kg armering']['D']))

ext_20_A1A3 = interp1d(x_data, y_A1A3_20, 'linear', fill_value='extrapolate')
ext_20_C3 = interp1d(x_data, y_C3_20, 'linear', fill_value='extrapolate')
ext_20_C4 = interp1d(x_data, y_C4_20, 'linear', fill_value='extrapolate')
ext_20_D = interp1d(x_data, y_D_20, 'linear', fill_value='extrapolate')