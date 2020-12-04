"""
Server to run the playlist converter web consumer program.
"""
import os
import flask
from flask import request
import logging
import mysql.connector
import json


# Globals
app = flask.Flask(__name__)

#Normally would store this in a config file
mydb = mysql.connector.connect(
        host="ix.cs.uoregon.edu",
        user="guest",
        password="guest",
        database="apple_music_db",
        port=3114
    )


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('playlist.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return "Page not found", 404


@app.route('/_submit', methods=['POST'])
def submit():

    song_id = json.loads(request.form['songid'])
    song = json.loads(request.form['song'])
    time = json.loads(request.form['time'])
    artist_id = json.loads(request.form['artistid'])
    artist = json.loads(request.form['artist'])

    print(song_id, song, time, artist_id, artist)

    mycursor = mydb.cursor()
   
    '''
    Clear all entries in the database
    =============================================
    '''
    sql = "DELETE FROM SONG"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

    sql = "DELETE FROM ARTIST"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
    '''
    =============================================
    '''

    #insert each entry into song table
    for i in range(0, len(song_id)):
        sql = "INSERT INTO SONG (song_id, song_name, song_length) VALUES (%s, %s, %s)"
        val = (int(song_id[i]), song[i], int(time[i]))
        
        mycursor.execute(sql, val)

    #insert each entry into artist table
    for i in range(0, len(song_id)):
        sql = "INSERT INTO ARTIST (artist_id, artist_name) VALUES (%s, %s)"
        val = (int(artist_id[i]), artist[i])

        mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    return "Submit works"

    

@app.route('/_display', methods=['GET', 'POST'])
def display():

    mycursor = mydb.cursor()

    mycursor.execute("SELECT song_name, song_length FROM SONG")

    temp = mycursor.fetchall()

    name = []
    length = []
    for t in temp:
        name.append(t[0])
        length.append(t[1])

    mycursor.execute("SELECT artist_name FROM ARTIST")

    artist = mycursor.fetchall()
 
    res = {
        'name' : name,
        'length' : length,
        'artist' : artist
    }

    return flask.render_template('display.html', result=res)

#############

app.debug = True
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port 5000")
    app.run(port=5000, host="0.0.0.0")
