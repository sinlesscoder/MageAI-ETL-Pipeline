## Spotify API

### Description

- The Spotify API is a `REST` API that allows an end user to get information from Spotify's data sources related to artists, playlists, and tracks.

### Setup

- We can use a software development kit (SDK) from Python which is called `spotipy` which allows an end user to use Python to work with Spotify's API directly in a package.

  - [Spotipy Client](https://spotipy.readthedocs.io/en/2.22.1/)

- `spotipy` can be installed using `pip`

```bash
pip install spotipy
```

- In order to use `spotipy` successfully, it is important to authorize the end user using `oauth2` authentication. `OAuth2` is a security protocol which asks for an end user to have a `client_id` and a `client_secret`.
- These can be obtained from several single sign on options (e.g. Facebook, Google) when trying to log into Spotify.

- To retrieve the credentials, we need to make an account at [Spotify's Developer website](http://developer.spotify.com).

![](https://p131.p1.n0.cdn.getcloudapp.com/items/OAulj5zr/8d32e117-6f61-4f15-b88e-293f25dc8e80.jpg?v=57dbbce1c72d8014f9bc0d598c1de4e4)

### Retrieving the Credentials

1. Open your Developer Dashboard on Spotify's Developer website.
2. Select / Create a new App.
3. Select `Settings`
4. Copy your Client ID and Client Secret.

### Usage

```python
from spotipy import Spotify
from spotipy.oauth2 import ClientCredentialsManager

# Supply the Client ID and Client Secret
client_id = ''
client_secret = ''

# Instantiate a Manager
manager = ClientCredentialsManager(client_id, client_secret)

# Instantiate Spotify client
client = Spotify(client_credentials_manager=manager)
```

### Resources

- [SpyVanilla is the GOAT](https://github.com/spotipy-dev/spotipy/issues/687)
