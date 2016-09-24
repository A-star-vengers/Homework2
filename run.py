#!flask/bin/python
from app import app
from app.db import init_db
from sys import argv, exit

init_db()

app.run(debug=True)
