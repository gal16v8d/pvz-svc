# pvz-svc

<p align="center">
  <img width="200" src="fast-api-logo.png" alt="FastApi logo">
  <p align="center">
    FastApi + Mongo REST API wiki about Plants Vs Zombies videogame
  </p>
</p>

# Get started

## Unix

Install poetry:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Init repo:

```bash
poetry new pvz-svc
```

Create the virtual env folder:

```bash
mkdir .venv
```

Install all the dependencies in the project (clean-state):

```bash
poetry install
```

Install any dependency you need:

```bash
poetry add lib_here
```

Remove a dependency you don't need:

```bash
poetry remove lib_here
```

Update all (updatable) libs

```bash
poetry update
```

# Set up

# env

Activate using the command:

```bash
source .venv/bin/activate
```

Exit virtual env:

```bash
exit
```

or

```bash
deactivate
```

# Advanced use cases

If multiple python versions are found in the operative system, then

- use pyenv to handle the versions
- if needed set the local python for this project, like

```bash
pyenv local 3.12.1
```

- you can confirm all good by checking

```bash
pyenv which python
```

- set the specific python version like

```bash
poetry env use $USER_HOME/.pyenv/versions/3.12.1/bin/python
```

- then install using commands like the ones in the previous section

# Formatter

Using `black` as code formatter
Can be used this way:

```bash
poetry run black .
```

# Type checking

Using `mypy` for type checking
Can be used this way:

```bash
poetry run mypy app tests
```

# docs

Open {base_url}/docs while running to access swagger instance
Open {base_url}/redoc while running to access redoc instance

# launch

You might need to create a DB in Atlas Mongo, then please reference `.env.sample`, to create your own `.env`
file with the relevant database info. Once ready you can do the following to launch:

```bash
uvicorn app:app --reload
```

# test

```bash
pytest
```

# Web deployment

This app can be hosted in [Railway](https://railway.app), folder that helps with it is `.ci` folder.

## List of cool technologies in use here

- [FastApi](https://fastapi.tiangolo.com)
- [poetry](https://python-poetry.org/)
- [pymongo](https://pymongo.readthedocs.io/en/stable/)

## License

[MIT licensed](LICENSE).

## Stay in touch

- Author - [gal16v8d](https://github.com/gal16v8d)
