from app import app
from flask import request
from app.services import Beams, Decks, Foundations, Columns, Walls, ExteriorWalls, InteriorWalls

@app.route('/beams', methods=['GET'])
def beams():
    return Beams.beamsGWP_summed 
    
@app.route('/decks', methods=['GET'])
def decks():
    return Decks.decksGWP_summed 
    
@app.route('/foundations', methods=['GET'])
def foundations():
    return Foundations.foundationsGWP_summed 

@app.route('/columns', methods=['GET'])
def columns():
    return Columns.columnsGWP_summed 

@app.route('/walls', methods=['GET'])
def walls():
    return Walls.wallsGWP_summed 
      
@app.route('/exteriorwalls', methods=['GET'])
def exteriorwalls():
    return ExteriorWalls.exteriorWallsGWP_summed     

@app.route('/interiorwalls', methods=['GET'])
def interiorwalls():
    return InteriorWalls.interiorWallsGWP_summed
   