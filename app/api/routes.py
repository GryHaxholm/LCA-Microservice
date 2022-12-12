from app import app
from flask import request
from app.services import Beams, Decks, Foundations, Columns, Walls

@app.route('/')
@app.route('/beams', methods=['POST'])
def beams():
    return Beams.beamsGWP_summed 
     #Mangler listen af bjælker.  

@app.route('/decks', methods=['POST'])
def decks():
    return Decks.decksGWP_summed 
      #Mangler listen af decks.  

@app.route('/foundations', methods=['POST'])
def foundations():
    return Foundations.foundationsGWP_summed 
      #Mangler listen af foundation

@app.route('/columns', methods=['POST'])
def columns():
    return Columns.columnsGWP_summed 
     #Mangler listen af columns.      

@app.route('/walls', methods=['POST'])
def walls():
    return Walls.wallsGWP_summed 
     #Mangler listen af walls.       