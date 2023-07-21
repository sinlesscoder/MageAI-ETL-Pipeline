from spotipy import Spotify
from client_authorization import client
from typing import Optional, Union

# Setup a function to get artist data as JSON
def retrieve_artist_data(artist_link: str, client: Spotify) -> Optional[Union[list, dict]]:
    # Convert an artist's link into an ID
    artist_id = artist_link.split("?")[0].split("/")[-1]

    # Get the actual results
    results = client.artist(artist_id)

    return results


