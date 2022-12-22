from app import app
from flask import request
from app.services import Beams, Decks, Foundations, Columns, Walls, ExteriorWalls, InteriorWalls

#@app.route('/') Måske lav noget til 'forsiden'.
@app.route('/beams', methods=['GET'])
def beams():
    return Beams.beamsGWP_summed 
     #Mangler listen af bjælker.  

@app.route('/decks', methods=['GET'])
def decks():
    return Decks.decksGWP_summed 
      #Mangler listen af decks.  

@app.route('/foundations', methods=['GET'])
def foundations():
    return Foundations.foundationsGWP_summed 
      #Mangler listen af foundation

@app.route('/columns', methods=['GET'])
def columns():
    return Columns.columnsGWP_summed 
     #Mangler listen af columns.      

@app.route('/walls', methods=['GET'])
def walls():
    return Walls.wallsGWP_summed 
     #Mangler listen af walls.     

@app.route('/exteriorwalls', methods=['GET'])
def exteriorwalls():
    return ExteriorWalls.exteriorWallsGWP_summed
     #Mangler listen af walls.    

@app.route('/interiorwalls', methods=['GET'])
def interiorwalls():
    return InteriorWalls.interiorWallsGWP_summed
     #Mangler listen af walls.    