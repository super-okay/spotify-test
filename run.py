import requests
import json
import base64
from creds import *

def get_bearer() -> str:
    ''' gets new bearer token from Spotify, returns bearer token '''
    url='https://accounts.spotify.com/api/token'
    id_string = '{}:{}'.format(CLIENT_ID, CLIENT_SECRET)
    base64_id = base64.b64encode(id_string.encode('ascii'))
    final_id = base64_id.decode('ascii')
    headers = {
        'Authorization': 'Basic {}'.format(final_id)
    }
    data = {
        'grant_type': 'client_credentials'
    }

    r = requests.post(url=url, headers=headers, data=data)
    bearer = r.json()['access_token']
    return bearer

def get_album(bearer, album_id):
    ''' 
        makes request to the get album endpoint
        bearer: bearer token
        album_id: album id
        returns nothing, prints result
    '''
    url = 'https://api.spotify.com/v1/albums/{}'.format(album_id)
    headers = {
        'Authorization': 'Bearer {}'.format(bearer)
    }
    r = requests.get(url=url, headers=headers)
    print(json.dumps(r.json(), indent=4))

def search_artist(bearer, keyword):
    url = 'https://api.spotify.com/v1/search?type=artist&limit=10&q={}'.format(keyword)
    headers = {
        'Authorization': 'Bearer {}'.format(bearer)
    }
    r = requests.get(url=url, headers=headers)
    print(json.dumps(r.json(), indent=4))


def main():
    bearer = get_bearer()
    # album_id = '4aawyAB9vmqN3uQ7FjRGTy'
    # get_album(bearer, album_id)
    keyword='eminem'
    search_artist(bearer, keyword)


if __name__ == "__main__":
    main()