import json
from os import getcwd, environ
from spotipy import Spotify

# Set up environment variables for your credentials

## Data Path to the JSON File
data_path = getcwd() + "/src/project_4/spotify_credentials.json"

## Load the JSON
with open(data_path) as f:
    # Create a dictionary of Spotify Variables
    spotify_vars = json.load(f)

# Update your environment variables
environ.update(spotify_vars)

# Bearer Token
bearer_token = environ['SPOTIFY_BEARER_TOKEN']

# Create a Spotify Client
client = Spotify(auth=bearer_token)