from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path="")

@app.route("/montmartre")
def montmartre():
	return render_template("index.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/background")
def send_background():
	print('Hello')
	return send_from_directory('templates', 'background.png')

@app.route("/music")
def send_music():
	print('Hello')
	return send_from_directory('templates', 'music.wav')


app.run()