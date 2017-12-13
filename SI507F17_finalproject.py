import requests_oauthlib
import webbrowser
import json
import pprint
import spotipy
# import spotify_data
import requests
import unittest
# import psycopg2
# import psycopg2.extras
# from psycopg2 import sql
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

data = makeSpotifyRequest('https://api.spotify.com/v1/artists/0n94vC3S9c3mb2HyNAOcjg/related-artists')
response_diction = json.loads(data.text)
# print(json.dumps(response_diction, indent=2))

# related_artists = 'https://api.spotify.com/v1/artists/{0}/related-artists.format(artist_id)
# head_and_the_heart = makeSpotifyRequest(related_artists params={'head and the heart'})
# related_artists_dict = head_and_the_heart.json()
# print(related_artists_dict)

#CLASS

class SpotifyData(object):
    def __init__(self, artist_list, rank_list, url_list):
        self.artists=artist_list
        self.popularity=rank_list
        self.images=url_list

    def ArtistNameList(self):
        related_artists=[]
        for item in response_diction['artists']:
            related_artists.append(item['name'])
        return related_artists.sort()

    def __repr__(self):
        return "Image URL: {}".format(self.images)

    def __contains__(self, x):
        return x in self.artists

# related_artists=[]
# for item in response_diction['artists']:
#     related_artists.append(item['name'])
# related_artists.sort()
# print(related)

artist_popularity=[]
for item in response_diction['artists']:
    artist_popularity.append(item['popularity'])
# print(artist_popularity)

image_url=[]
for item in response_diction['artists']:
    image_url.append(item['images'][2]['url'])
# print(image_url)

# my_data=SpotifyData(related_artists, artist_popularity, image_url)
# print(my_data)


#Setting up the database
# db_connection, db_cursor = None, None

# # def get_connection_and_cursor():
#     global db_connection, db_cursor
#     if not db_connection:
#         try:
#             if db_password != "":
#                 db_connection = psycopg2.connect("dbname='{0}' user='{1}' password='{2}'".format(db_name, db_user, db_password))
#                 print("Success connecting to database")
#             else:
#                 db_connection = psycopg2.connect("dbname='{0}' user='{1}'".format(db_name, db_user))
#         except:
#             print("Unable to connect to the database. Check server and credentials.")
#             sys.exit(1) # Stop running program if there's no db connection.
#
#     if not db_cursor:
#         db_cursor = db_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
#
#     return db_connection, db_cursor

# def setup_database():
    # conn, db_cursor = get_connection_and_cursor()
    #
    # db_cursor.execute("DROP TABLE IF EXISTS Artists")
    # db_cursor.execute("DROP TABLE IF EXISTS Artist Popularity")
    #
    #
    # db_cursor.execute("CREATE TABLE Artists(ID SERIAL PRIMARY KEY, Name VARCHAR (40) UNIQUE)")
    # db_cursor.execute("CREATE TABLE Artist Popularity(ID SERIAL PRIMARY KEY, Name VARCHAR(128) UNIQUE, Type VARCHAR(128), Location VARCHAR(255), Description TEXT)")
    # conn.commit()
