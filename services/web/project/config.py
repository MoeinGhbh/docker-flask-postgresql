import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Get enviroment variable from .env.dev
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False