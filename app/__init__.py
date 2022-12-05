from flask import Flask

app = Flask(__name__)

from app.services import Beams
from app.services import Decks
from app.services import Columns
from app.services import Foundations
