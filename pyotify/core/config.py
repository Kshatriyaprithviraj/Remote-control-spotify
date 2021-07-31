import os
import yaml
from collections import namedtuple

from ..auth import authMethod

# namedtuples are tuple-like objects with a name and with fields
# accessible by attribute lookup.
Config = namedtuple('Config', ['client_id',
                               'client_secret',
                               'access_token_url',
                               'auth_url',
                               'api_version',
                               'api_url', 'base_url',
                               'auth_method'])

# Returns the above tuple i.e., namedtuple - Config


def read_config():
    current_dir = os.path.abspath(os.curdir)
    file_path = os.path.join(current_dir, 'config.yaml')

    try:
        with open(file_path, mode='r', encoding='UTF-8') as file:
            config = yaml.load(file)

            config['base_url'] = f'{config["api_url"]}/{config["api_version"]}'
            auth_method = config['auth_method']
            config['auth_method'] = authMethod.__members__.get(auth_method)
            # returning an instance of namedtuple - Config.
            return Config(**config)
    except IOError:
        print("""Err: Could not find the configuration file `config.yaml` 'on your current directory.
            Default format is: ',
            client_id: 'your_client_id'
            client_secret: 'you_client_secret'
            access_token_url: 'https://accounts.spotify.com/api/token'
            auth_url: 'https://accounts.spotify.com/authorize'
            api_version: 'v1'
            api_url: 'http//api.spotify.com'
            auth_method: 'authentication method'
            
            * auth_method can be CLIENT_CREDENTIALS or
              AUTHORIZATION_CODE""")
        raise
