from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI') 
mongo = PyMongo(app)
song = mongo.db.song_details 

@app.route('/', methods = ['GET', 'POST'])
def login():
    return render_template("index.html")

@app.route('/result', methods = ['GET', 'POST'])
def result():

    song_name = None

    if(request.method == 'get'):
        return render_template("index.html")

    song_name = request.form.get('song')
    print(song_name)

    song_det = None

    if(song_name):
        song_det = song.find()

    print('song_det: ', song_det)

    return render_template("index.html", song_details = song_det, song_name = song_name)
   

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True, port = 3000)