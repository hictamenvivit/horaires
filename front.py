from flask import Flask
from main import Allosession 

app = Flask(__name__, static_url_path='/files')

@app.route('/')
def index():
    a = Allosession()
    return a.as_html()
    
@app.route('/scenario/')
def scenario():
    return app.send_static_file('Maxime_Bettinelli_Le_Bulletin.pdf')
    
