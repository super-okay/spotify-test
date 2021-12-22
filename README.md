# Testing Spotify API

## Auth
I'm using the [Client Credentials](https://developer.spotify.com/documentation/general/guides/authorization/client-credentials/) auth flow. This requires making a post request to Spotify's token endpoint using the client ID and client secret key to get a bearer token.
This process is outlined in the `get_bearer()` method in `run.py`.

## Main Request
Once the bearer token has been received, a request can now be made to Spotify's Web API using the bearer token.
I am testing the [Get Album](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-album) and [Search](https://developer.spotify.com/documentation/web-api/reference/#/operations/search) endpoints as shown in Spotify's documentation. <br>
