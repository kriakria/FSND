import os

db_user = os.dotenv('db_user')
db_password = os.dotenv('db_password')

export DATABASE_URL = "postgres://db_user:db_password@localhost:5432/heroko_test"

