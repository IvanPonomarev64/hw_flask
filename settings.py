import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask("app")
bcrypt = Bcrypt(app)

load_dotenv()
engine = create_engine(os.getenv("ENGINE"))
insp = inspect(engine)
Session = sessionmaker(bind=engine)
