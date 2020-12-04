# playlist_converter

CONTENTS OF THIS FILE
---------------------

 * Summary
 * Contents
 * How to Use
 * Maintainers


SUMMARY
------------

 * Built a flask server and client consumer program which is meant to retrieve data from a user’s Apple Music account, store that data in my apple_music_db database running on MySQL ix server, and then query that database to retrieve information in order to create a new playlist in the user’s Spotify account. Because gaining access to Apple Music and Spotify APIs cost money, I’ve implemented everything in between the playlist conversion. More specifically, I wrote a consumer program which asks the user for a sample playlist (this is just a dummy playlist because I have no access to the Apple Music api), stores that playlist in my apple_music_db database, and then queries the database and displays what would be uploaded to the user’s Spotify.


CONTENTS
------------
 * templates : this folder holds both the display.html and playlist.html files. playlist.html is the index page when opening on localhost:5000. display.html is rendered after clicking the "display" button
 * Dockerfile : Dockerfile to build a container to run the program.
 * connectionData.txt : contains relevant information to connect to my MySQL database
 * requirements.txt : requirements used by the Dockerfile to build the container
 * server.py : main driver program. Server which responds to client requests and inserts/queries database, as well as renders templates. Implemented using pythons Flask microservice framework.


HOW TO USE
------------

* Clone this repo to your local machine
* Navigate into the main repo folder
* Execute the following command from the terminal:
```console
docker build .
```
* Get the container id from the docker success message from the last line of the output (should be a random string of letters and numbers).
* Following build run the docker container:
```console
docker run -d -p 5000:5000 <conatiner-id>
```
* Open "localhost:5000" in your browser and use the consumer program.


MAINTAINERS
-----------

 * Mac Weinstock



