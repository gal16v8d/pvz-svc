# pvz-svc

<p align="center">
  <img width="200" src="fast-api-logo.png" alt="FastApi logo">
  <p align="center">
    FastApi + Mongo REST API wiki about Plants Vs Zombies videogame
  </p>
</p>

# Get started

## Unix

Install pipenv:

```bash
sudo apt install python3-venv
pip3 install pipenv
```

Then create the folder for allocate the virtual environment:

```bash
mkdir .venv
```

Launch pipenv:

```bash
pipenv install
```

Then activate the virtual env:

```bash
pipenv shell
```

Run command inside virtualenv:

```bash
pipenv run
```

Exit virtual env:

```bash
exit
```

or

```bash
deactivate
```

## Windows

Update pip:

```bash
py -m pip install --upgrade pip
```

Install python3-venv:

```bash
py -m pip install virtualenv
```

Then create the folder for allocate the virtual environment:

```bash
py -m virtualenv env
```

Optional (run if UnauthorizedAccess in powershell console):

```bash
Set-ExecutionPolicy Unrestricted -Scope Process
```

Then activate the virtual env:

```bash
.\venv\Scripts\activate.ps1
```

Now you can install python libs as you need it

# set up

Configure all your dependencies in Pipfile.
See: [Pypi](https://pypi.org/)

# dependencies

For generate requirements.txt file please execute:

```bash
pip3 freeze > requirements.txt
```

# docs

Open {base_url}/docs while running to access swagger instance
Open {base_url}/redoc while running to access redoc instance

# launch

You might need to create a DB in Atlas Mongo, then please reference `.env.sample`, to create your own `.env`
file with the relevant database info. Once ready you can do the following to launch:

```bash
cd src
uvicorn main:app --reload
```

# test

```bash
cd src
pytest
```
