#!/bin/bash

import os

db_user = os.dotenv('db_user')
db_password = os.dotenv('db_password')
db_name = 'capstone'

export DATABASE_URL = "postgres://{}:{}@{}/{}". \
    format(db_user, db_password, 'localhost:5432', db_name)

# Auth0
export AUTH0_DOMAIN = 'kriakria.eu.auth0.com'
export ALGORITHMS = ['RS256']
export API_AUDIENCE = 'http://localhost:5000/capstone'
export AUTH_CLIENT_ID = 'jzCMbasV3UOWKwx9kZchJIzS8qqeiAhD'

# Tokens

export ASSISTANT='token_value_1'
export DIRECTOR='token_value_2'
export PRODUCER='token_value_3'
