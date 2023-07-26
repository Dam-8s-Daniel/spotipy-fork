"""
This script allows you to search for information about an artist on Spotify.

Prerequisites: Must have an access token. Follow these steps to create an app and get the token here:
https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token.
And then set the environmental variables as shown here: https://www.youtube.com/watch?v=3RGm4jALukM.

How to run the script:
    python search.py SEARCH_STRING
        - SEARCH_STRING: an optional string of the artist. The default string, if not provided, is "Radiohead"

Returns:
    search response
    The program will display the search results in pretty-print, or a human-readable format.

How to access the fields:
    result = sp.search(search_str)
    result['FIELD']

FIELD = { tracks, artists albums, playlists, shows, episodes, audiobooks }

See search reference for full response at https://developer.spotify.com/documentation/web-api/reference/search
"""

# shows artist info for a URN or URL

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Radiohead'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
result = sp.search(search_str)
pprint.pprint(result)
