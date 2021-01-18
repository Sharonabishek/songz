from flask import Flask, render_template, request, jsonify, url_for, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def login():
    return render_template("index.html")

@app.route('/result', methods = ['GET', 'POST'])
def result():
    song_name = request.form.get('song')
    print(song_name)

    #if (song_name = song_details.song_name):

    

    song_details = [
        {
            "song_name" : "Vaathi Raid",
            "movie_name": "Master",
            "music_director" : "Anirudh",
            "singer_name" : "Arivu"
        },
        {
            "song_name" : "Chellama",
            "movie_name": "Doctor",
            "music_director" : "Anirudh",
            "singer_name" : "Anirudh"
        }
    ]

    return render_template("index.html", song_details=song_details,song_name=song_name)
   

if __name__ == "__main__":
    app.run(debug=True, port=3000)
