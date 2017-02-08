# Secret key resides in an .env file.
# KEEP IT SAFE!!!
from decouple import config


SECRET_KEY = config('SECRET_KEY')
