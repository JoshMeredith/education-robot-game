# CodeBot

# Build:
1. Install node (version 8.x.x)
2. `npm install`
3. `npm run make`

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
5. To initialise the database, ensure virtualenv is activated then run:
```
cd <repo_dir>
./db_create.py
```

## To run Flask

1. Ensure virtualenv is activated.
2. In `web/` directory `FLASK_APP=__init__.py FLASK_DEBUG=1 flask run`
The debug flag is optional but is useful for testing / debugging.
3. Open server pages in browser!
