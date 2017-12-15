# 507_Final_Project

BASICS:
To run the code you should use the file SI507F17_finalproject.py
The other files included are the config.py and the plotlyconfig.py

You should fork this repository to your own GitHub account.
You should then clone your fork of the repository, so you have your own copy and can make edits on your own computer.

HOW THIS WORKS:

This code accesses the Spotify API (Spotify API Developer: https://developer.spotify.com/web-api/) and makes a request to get related artists for a single specified artist. In this case, I have chosen Head and the Heart. The request returns data on related artists to the chosen artist, the rank of artist popularity with any score from (0 to 100) and the image URL's with the related artists' album.

When you run this file a few things will happen and these are the steps to take to set it up so it runs properly.
Please make sure to complete these steps before running the code:


SETUP:

1) The code will make a Spotify request to the Spotify API. You must first have a valid Spotify user account (Premium or Free). To get one go to www.spotify.com. When you have a user account, go to the My Applications (https://developer.spotify.com/my-applications/) page and Create a new application. Note that this name will be shown in the pop-up that asks the user for authorization to access their Spotify data. Once you have completed the registration of your application click Save.
2) In the config.py file, you must enter in a valid Spotify CLIENT_ID and CLIENT_SECRET in order for you to access this API. Each of these can be found in the application you just created. Always store the client secret key securely! #Description referenced from the developer.spotify.com site.
2) Also, two database tables were created: One with a column of Related artists and their IDs and another table with the Artists, popularity number, an image url and the artist ID. Located in the config.py file is the db_username, db_user and db_password to use to get these tables.
4) Lastly, in the plotlyconfig.py file there is a username and an api_key for credentials. These are imported in to the code and will be used to run the visualization part.


RUN THE CODE:
1) This code works with Python3
2) Once you have created your virtual environment you should type in to your command prompt python SI507F17_finalproject.py and hit return

WHAT TO EXPECT ONCE THE CODE HAS BEEN RUN:

1) The first thing that will happen is a new tab in your browser will open with your Spotify API Application. Click Ok to proceed. You will then receive a URL that you need to copy exactly and paste it in to the command prompt where it says "Authenticate and then enter the full callback URL:"
2) The code will print out a command prompt that says:
saved token to cache
(One thing to note, if you use/run this program again, the token after about an hour will cause an error: raise TokenExpiredError() and will need to be deleted in order to run the program again).
3) The code will also print out a list of related_artist_objects in the command prompt
4) The code will run through the unittests in the command prompt.
5) The code will also open up a new webbrowser and will use plotly to visualize a graph or related artists and their popularity rank.
6) Lastly, the code has 6 different unittest subclasses that test part of the code and will print out in the command prompt if they have passed.


REFERENCES:

I cited code from the facebook_example.py  and spotify_data.py and spotify_oauth2_example.py file to help with setting up and caching my data using the OAuth2 method.
I used code from my SI507_project6.py file to set up the database connection and cursor and setup the database.
I cited code from plot1_simplerexample.py to help set up my plotly visualization.

I worked with Stefan Deuchler, Vibhuti Kanitkar and Kenji Kaneko and Anand Doshi for advice and tips on this project.
