from flask import Flask, send_file, render_template, jsonify
import json
from models import get_formatted_showtimes
from datetime import datetime as dt
from matrix import get_positif_cdc_grades

app = Flask(__name__, static_url_path='/files/')
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    with open('theater_codes.json', 'r') as f:
        theater_codes = json.load(f)
    showtimes = get_formatted_showtimes(theater_codes, jour_choisi=dt.strftime(dt.today(),"%Y-%m-%d"))
    return render_template('hello.html', content=showtimes)
    
@app.route('/scenario/')
def scenario():
    return send_file('files/Maxime_Bettinelli_Le_Bulletin.pdf')
    #return 'iih'
    
@app.route('/hello/')
def hello():
    return 'hello'

@app.route('/matrix/')
def matrix():
    return render_template("matrix.html", content=get_positif_cdc_grades())
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
