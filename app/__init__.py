from flask import Flask

app = Flask(__name__)

from app.resources import jSONHandler