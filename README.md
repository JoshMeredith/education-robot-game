# CodeBot

# Build:
1. Install node
2. `npm install -g purescript typescript pulp bower uglify-es`
3. `make`

# Running Flask (with virtualenv)

We use Python3.

## Setup (once)

1. Install virtualenv
2. Create a virtualenv (outside the project directory)
```
cd ~
mkdir envs
cd envs
virtualenv codegame
```
3. Activate virtualenv `source ~/envs/codegame/bin/activate`. To deactivate,
   simply `deactivate`.
4. Install packages inside virtualenv.
```
cd <repo_dir>/web
pip3 install -r requirements.txt
```

## To run Flask

1. Ensure virtualenv is activated.
2. In `web/` directory `FLASK_APP=app.py FLASK_DEBUG=1 flask run`
The debug flag is optional but is useful for testing / debugging.
3. Open server pages in browser!
