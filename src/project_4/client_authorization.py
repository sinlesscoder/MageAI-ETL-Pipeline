import json
from os import getcwd, environ
from spotipy import Spotify
from spotipy.oauth2 import ClientCredentialsManager

# Set up environment variables for your credentials

## Data Path to the JSON File
data_path = getcwd() + "/src/project_4/spotify_credentials.json"

## Load the JSON
with open(data_path) as f:
    # Create a dictionary of Spotify Variables
    spotify_vars = json.load(f)

# Update your environment variables
environ.update(spotify_vars)

# Client ID and Client Secret
client_id = environ['SPOTIFY_CLIENT_ID']
client_secret = environ['SPOTIFY_CLIENT_SECRET']

# Manager variable
manager = ClientCredentialsManager(client_id, client_secret)

# Create a Spotify Client
client = Spotify(manager)