import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://xqvxrucqzljesm:d0dae0349270bb2b9055d04198921b932a987c9c604a33211a56f970da36b9ca@ec2-54-83-55-125.compute-1.amazonaws.com:5432/df5bsnd4t9si5c'
