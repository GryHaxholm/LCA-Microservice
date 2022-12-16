import pandas as pd
import re
import numpy as np
from scipy.interpolate import interp1d, interp2d
import json
from app.resources import dataHandling

#Working with the JSON files from the VC database
structuralElements = dataHandling.structuralElements
#Reading the LCA dataframe
LCA_Data = dataHandling.LCA_Data

#for interpolation between 220 and 320 hollowcore deck
x_data = (0.22,0.32)
y_A1A3 = (sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 22 cm, 6-10 liner']['A1tilA3']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 32 cm, 6-10 liner']['A1tilA3']))
y_C3 = (sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 22 cm, 6-10 liner']['C3']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 32 cm, 6-10 liner']['C3']))
y_C4 = (sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 22 cm, 6-10 liner']['C4']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 32 cm, 6-10 liner']['C4']))
y_D=(sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 22 cm, 6-10 liner']['D']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 32 cm, 6-10 liner']['D']))
int_A1A3 = interp1d(x_data, y_A1A3, 'linear')
int_C3 = interp1d(x_data, y_C3, 'linear')
int_C4 = interp1d(x_data, y_C4, 'linear')
int_D = interp1d(x_data, y_D, 'linear')

#for extrapolating below 220 mm hollowcore deck
ext_A1A3 = interp1d(x_data, y_A1A3, 'linear', fill_value='extrapolate')
ext_C3 = interp1d(x_data, y_C3, 'linear', fill_value='extrapolate')
ext_C4 = interp1d(x_data, y_C4, 'linear', fill_value='extrapolate')
ext_D = interp1d(x_data, y_D, 'linear', fill_value='extrapolate')

#for extrapolating above 320 mm hollowcore deck
x_data = (0.22,0.32)
y_A1A3_32 = (sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 22 cm, 6-10 liner']['A1tilA3']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 32 cm, 11-17 liner']['A1tilA3']))
y_C3_32 = (sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 22 cm, 6-10 liner']['C3']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 32 cm, 11-17 liner']['C3']))
y_C4_32 = (sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 22 cm, 6-10 liner']['C4']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 32 cm, 11-17 liner']['C4']))
y_D_32=(sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 22 cm, 6-10 liner']['D']),sum(LCA_Data.loc[LCA_Data['Navn']== 'Huldæk element, 32 cm, 11-17 liner']['D']))

ext_32_A1A3 = interp1d(x_data, y_A1A3_32, 'linear', fill_value='extrapolate')
ext_32_C3 = interp1d(x_data, y_C3_32, 'linear', fill_value='extrapolate')
ext_32_C4 = interp1d(x_data, y_C4_32, 'linear', fill_value='extrapolate')
ext_32_D = interp1d(x_data, y_D_32, 'linear', fill_value='extrapolate')