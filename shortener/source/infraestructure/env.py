import os

mongo_url = os.getenv('MONGODB_URL', default='mongodb://admin:123456@mongodb:27017')

short_url = os.getenv('SHORT_URL', default='localhost')

jwt_secret = os.environ['SECRET']