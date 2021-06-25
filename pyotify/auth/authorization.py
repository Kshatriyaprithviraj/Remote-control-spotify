from collections import namedtuple

# This is going to contain authentication model
# and it'll contain data as response for requesting
# an access token.
Authorization = namedtuple('Authorization', ['access_token',
                                             'token_type',
                                             'expires_in',
                                             'scope',
                                             'refresh_token'])

"""
    access_token: The token has to be sent together with every request to the web API.
    token_type: The type of token, which is usually Bearer.
    expires_in: The access_token expiration time is 3600 seconds.
    scope: The scope is basically the permissions that spotify's user granted to the application.
    refresh_token: The token that can be used to refresh the access token after expiration.
"""
