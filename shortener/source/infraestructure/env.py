import os

user = os.getenv("mongodb_user")

password = os.getenv("mongodb_password")

host = os.getenv("mongodb_host")

pg_user = os.getenv('pgdb_user', default="postgres")

pg_password = os.getenv('pgdb_password', default="123456")

short_url = os.getenv('SHORT_URL', default='localhost')