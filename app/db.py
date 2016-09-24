from flask_sqlalchemy import SQLAlchemy
from app import app
from app.util import getsalt, createhash

db = SQLAlchemy(app)

def init_db():
    from app.dbmodels import User

    db.create_all()
