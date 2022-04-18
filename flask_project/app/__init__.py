from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Instance APP
app = Flask(__name__)
app.config.from_object('config')

# Data Base Configuration
db = SQLAlchemy(app)

from app.models.create_db import Tasks

# Import default.py Module with our rotes
from app.controllers import default