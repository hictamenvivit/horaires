from flask import Flask
from main import Allosession 

app = Flask(__name__)

@app.route('/')
def index():
    a = Allosession()
    return a.as_html()
