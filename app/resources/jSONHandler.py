import json

with open('structuralElements.json') as f:
    structuralElements = json.load(f)

for beam in structuralElements['Beam']:
    print(beam['MaterialID'],beam['Volume'])

for column in structuralElements['Column']:
    print(column['MaterialID'],column['Volume'])

for deck in structuralElements['Deck']:
    print(deck['MaterialID'],deck['Area'])

for exteriorWall in structuralElements['ExteriorWall']:
    print(exteriorWall['MaterialID'],exteriorWall['Area'])

for interiorWall in structuralElements['InteriorWall']:
    print(interiorWall['MaterialID'],interiorWall['Area'])

for foundation in structuralElements['Foundation']:
    print(foundation['MaterialID'],foundation['Volume'])