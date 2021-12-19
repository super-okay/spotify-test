import requests
import json
import base64
from creds import *

def get_bearer():
    ''' gets new bearer token from Spotify, returns string '''
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

def make_request(bearer):
    ''' makes main API request to Spotify, prints response '''
    url = 'https://api.spotify.com/v1/albums/4aawyAB9vmqN3uQ7FjRGTy'
    headers = {
        'Authorization': 'Bearer {}'.format(bearer)
    }
    r = requests.get(url=url, headers=headers)
    print(json.dumps(r.json(), indent=4))


def main():
    bearer = get_bearer()
    make_request(bearer)


if __name__ == "__main__":
    main()