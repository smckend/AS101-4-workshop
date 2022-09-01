import os


SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', False)
DB_NAME = os.environ.get('DB_NAME', "postgres")
DB_USER = os.environ.get('DB_USER', "postgres")
DB_PASS = os.environ.get('DB_PASS')
DB_SERVICE = "postgres"
DB_PORT = "5432"
SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
)
