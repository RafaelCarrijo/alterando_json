from flask import Flask


app = Flask(__name__, static_folder='templates')

from app.controlers import pages
