from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#Models
from .clients import *
from .events import *
from .purchases import *