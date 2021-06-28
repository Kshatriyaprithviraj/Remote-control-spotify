# Remote-control-spotify ​🔉​🎶​

A terminal application for spotify.🔫

# Features 🎊

You can search 🔍 for
- artists
- albums
- play the searched content.

# Toolset 🛠

- [flask](https://flask.palletsprojects.com/en/2.0.x/)
- [requests](https://pypi.org/project/requests/)
- [pyyaml](https://pypi.org/project/PyYAML/)

# Directory structure 🛡

```shell
./
├── app.py
├── client
│   ├── alignment.py
│   ├── data_manager.py
│   ├── empty_results_error.py
│   ├── menu_item.py
│   ├── menu.py
│   └── panel.py
├── config.yaml
├── Pipfile
├── Pipfile.lock
├── pyotify
│   ├── auth
│   │   ├── auth_method.py
│   │   ├── authorization.py
│   │   ├── auth.py
│   │   └── __init__.py
│   └── core
│       ├── album.py
│       ├── artist.py
│       ├── config.py
│       ├── exceptions.py
│       ├── __init__.py
│       ├── parameter.py
│       ├── player.py
│       ├── request.py
│       ├── request_type.py
│       ├── search.py
│       └── search_type.py
├── README.md
├── spotify_auth.py
└── templates
    └── index.html
```

# To run 🏃🏻‍♂️

> `git clone https://github.com/Kshatriyaprithviraj/Remote-control-spotify.git` <br>
> `cd ./remote*` <br>
> `pipenv shell` <br>
> `pipenv install` <br>
> `python app.py` <br>

Cheers! 🥂
