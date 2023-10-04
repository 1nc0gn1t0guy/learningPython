import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your credentials here
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:8080/callback'

# Set the scope for authorization
scope = 'playlist-modify-public playlist-read-private user-library-read'

# Authenticate and create a Spotipy instance
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

# Get the user's ID
user_id = sp.me()['id']

# Find the Discover Weekly playlist
playlists = sp.current_user_playlists(limit=50)
discover_weekly_id = None
for playlist in playlists['items']:
    if playlist['name'] == 'Descubrimiento Semanal' and playlist['owner']['id'] == 'spotify':
        discover_weekly_id = playlist['id']
        break

if discover_weekly_id is None:
    print('Discover Weekly playlist not found.')
    exit()

# Get the tracks from Discover Weekly
tracks = sp.playlist_tracks(discover_weekly_id)
track_ids = [track['track']['id'] for track in tracks['items']]
print(track_ids)

# Provide the ID of the existing playlist you want to add the tracks to
existing_playlist_id = 'WeeklyDiscover Forever'

# Add the tracks from Discover Weekly to the existing playlist
sp.playlist_add_items(existing_playlist_id, track_ids)

print(f'Successfully added {len(track_ids)} tracks from Discover Weekly to the existing playlist.')
