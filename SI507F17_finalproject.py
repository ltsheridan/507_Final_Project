import requests_oauthlib
import webbrowser
import json
import pprint
import spotipy
# import spotify_data
import requests
import unittest
import psycopg2
import psycopg2.extras
from psycopg2 import sql
from config import *

#Links to access Spotify
AUTHORIZATION_URL = 'https://accounts.spotify.com/authorize'
REDIRECT_URI = 'https://www.programsinformationpeople.org/runestone/oauth'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
spotify_session = False

#Caching the data and making a request to the API
def makeSpotifyRequest(url, params=None):
    global spotify_session
    if not spotify_session:
        start_spotify_session()
    if not params:
        params = {}
    return spotify_session.get(url, params=params)

def start_spotify_session():
    global spotify_session
    try:
        cached_token = get_saved_cache()
    except FileNotFoundError:
        cached_token = None

    if cached_token:
        spotify_session = requests_oauthlib.OAuth2Session(CLIENT_ID, token=cached_token)
    else:
        spotify_session = requests_oauthlib.OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI) # Create an instance of an OAuth2Session
        authorization_url, state = spotify_session.authorization_url(AUTHORIZATION_URL)
        webbrowser.open(authorization_url)
        authorization_response = input('Authenticate and then enter the full callback URL: ').strip()
        token = spotify_session.fetch_token(TOKEN_URL, authorization_response=authorization_response, client_secret=CLIENT_SECRET)
        print("got token")
        save_cache(token)
        print("saved token to cache")
        # r = spotify_session.get('https://api.spotify.com/v1/')
        # response_diction = json.loads(r.text)
        # print(json.dumps(response_diction, indent=2))

def get_saved_cache():
    with open('token.json', 'r') as f:
        token_json = f.read()
        token_dict = json.loads(token_json)
        return token_dict

def save_cache(token_dict):
    with open('token.json', 'w') as f:
        token_json = json.dumps(token_dict)
        f.write(token_json)

Spotify_data = makeSpotifyRequest('https://api.spotify.com/v1/search')
#use https://developer.spotify.com/web-api/search-item/ to search for specific artist
#
# request1=makeSpotifyRequest('https://api.spotify.com/v1/search', "Head and the Heart")
# response_diction2=json.loads(data.text)
# print(response_diction2)

data = makeSpotifyRequest('https://api.spotify.com/v1/artists/0n94vC3S9c3mb2HyNAOcjg/related-artists')
response_diction = json.loads(data.text)
# print(json.dumps(response_diction, indent=2))



#CLASS holds artist and list of related artists

class SpotifyArtist(object):
    def __init__(self, artist_name, popularity, image_url):
        self.artist_name=artist_name
        self.popularity=popularity
        self.image_url=image_url

    def __repr__(self):
        return "This artist {} has a popularity score of {} and the image url: {}".format(self.artist_name, self.popularity, self.image_url)

    def __contains__(self, x):
        return x in self.artist_name

related_artists_obj=[]
for item in response_diction['artists']:
    artist_object=SpotifyArtist((item['name']), (item['popularity']),(item['images'][2]['url']))
    related_artists_obj.append(artist_object)

# print(related_artists_obj)

# artist_popularity=[]
# for item in response_diction['artists']:
#     artist_popularity.append(item['popularity'])
# # print(artist_popularity)
#
# image_url=[]
# for item in response_diction['artists']:
#     image_url.append(item['images'][2]['url'])
# print(image_url)





#Setting up the database
db_connection, db_cursor = None, None

def get_connection_and_cursor():
    global db_connection, db_cursor
    if not db_connection:
        try:
            if db_password != "":
                db_connection = psycopg2.connect("dbname='{0}' user='{1}' password='{2}'".format(db_name, db_user, db_password))
                print("Success connecting to database")
            else:
                db_connection = psycopg2.connect("dbname='{0}' user='{1}'".format(db_name, db_user))
        except:
            print("Unable to connect to the database. Check server and credentials.")
            sys.exit(1) # Stop running program if there's no db connection.

    if not db_cursor:
        db_cursor = db_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    return db_connection, db_cursor


# Code functions to create tables and database setup

def setup_database():
    conn, db_cursor = get_connection_and_cursor()

    db_cursor.execute("DROP TABLE IF EXISTS Artists")
    db_cursor.execute("DROP TABLE IF EXISTS Artists Popularity")
    db_cursor.execute("DROP TABLE IF EXISTS Image URL")


    db_cursor.execute("CREATE TABLE Artists(ID SERIAL PRIMARY KEY, Artist VARCHAR (50) UNIQUE)")
    db_cursor.execute("CREATE TABLE Artists Popularity(ID SERIAL PRIMARY KEY, Artist VARCHAR(50) UNIQUE, Artist_ID INTEGER REFERENCES Artist (ID), Artists Popularity INTEGER")
    db_cursor.execute("CREATE TABLE Image URL(ID SERIAL PRIMARY KEY, Artist VARCHAR (50) UNIQUE, Image URL VARCHAR (255))")
    conn.commit()

# Code to insert data into the database here.

def insert_data(artist_name, popularity, url):
    sql = "INSERT INTO Artists(Artist) VALUES(%s)"
    db_cursor.execute(sql,(Artist))
    db_connection.commit()

# Code to invoke functions
get_connection_and_cursor()
setup_database()
