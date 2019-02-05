from flask import Flask, send_file
from main import Allosession 

app = Flask(__name__, static_url_path='/files/')

@app.route('/')
def index():
    a = Allosession()
    return a.as_html()
    
@app.route('/scenario/')
def scenario():
    return send_file('files/Maxime_Bettinelli_Le_Bulletin.pdf')
    #return 'iih'
    
@app.route('/hello/')
def hello():
    return 'hello'
    
