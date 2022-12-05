import json

with open('structuralElements.json') as f:
    structuralElements = json.load(f)

for beam in structuralElements['Beam']:
    print(beam['Material'],beam['Volume'])

for column in structuralElements['Column']:
    print(column['Material'],column['Volume'])

for deck in structuralElements['Deck']:
    print(deck['Material'],deck['Area'])

for Wall in structuralElements['Wall']:
    print(Wall['Material'],Wall['Area'])

#for foundation in structuralElements['Foundation']:#
    #print(foundation['Material'],foundation['Volume'])