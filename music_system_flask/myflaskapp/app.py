from flask import Flask, render_template, flash, redirect, url_for, request
from Recommendations import popular_recommender, similar_recommender

app = Flask(__name__)

popular_songs = popular_recommender()

@app.route('/')
def intro():
    return render_template("intro.html")

@app.route('/popularity')
def popular():
    return render_template("popularity.html", popularSongs = popular_songs)

@app.route('/similarity')
def similar():
    return render_template("similarity.html")

@app.route('/similarity', methods = ["GET","POST"] )
def get_data():
    if request.method == "POST":
      song_from_form = request.form["song"]
      artist_from_form = request.form["artist"]  
      similar_songs = similar_recommender(song_from_form, artist_from_form)
    return render_template("similarity.html", similarSongs = similar_songs)  


if __name__=="__main__":
    app.run(debug=True)