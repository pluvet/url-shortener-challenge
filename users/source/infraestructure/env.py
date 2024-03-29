import os

pg_user = os.getenv('PGDB_USER', default="postgres")

pg_password = os.getenv('PGDB_PASSWORD', default="123456")

secret = os.environ['SECRET']
