#!/bin/bash

import os

db_user = os.dotenv('db_user')
db_password = os.dotenv('db_password')
db_name = 'capstone'

export = "postgres://mswtwueikeynok: \
         074a6ff712bd6dab3ec93118b31d70ac10b111f32d17c7e4c8afc1c0d18a23cb@ \
         ec2-3-216-181-219.compute-1.amazonaws.com:5432/dboednp2dv6b26"

# Auth0
export AUTH0_DOMAIN = 'kriakria.eu.auth0.com'
export ALGORITHMS = ['RS256']
export API_AUDIENCE = 'http://localhost:5000/capstone'
export AUTH_CLIENT_ID = 'jzCMbasV3UOWKwx9kZchJIzS8qqeiAhD'

# Tokens

export ASSISTANT='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpIWGZWZ3plREptV2xBeWNpcDRxdyJ9.eyJpc3MiOiJodHRwczovL2tyaWFrcmlhLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA1MzBkZjhlYzRhMzAwNmVlMzUxZjMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAvY2Fwc3RvbmUiLCJpYXQiOjE2MTEyMjI2MTMsImV4cCI6MTYxMTMwOTAxMywiYXpwIjoianpDTWJhc1YzVU9XS3d4OWtaY2hKSXpTOHFxZWlBaEQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMtbGlzdCIsImdldDptb3ZpZXMtbGlzdCJdfQ.THozfeDZxDj4erg8Bnx84bt2liTp_vp_hwM-gCSWrvTgYbJYwZbv_ET6bMewF79ddq5AKSJbIaXyAa_o5zMMDrrTxCxO5Ns5YUIfWqXsq0-WK4V15iAP4jRcbxKyPvUDIFHem6QEXNwdzrAn2dVs9_JxgxjkKz8imChWrNLJSJmfhuDioHsqTeRzwUKb-vjq5vp6PaFvTFuDi_BGf9bAB8Hd7BdlSTfYpKprySW_PTQCQnEaQ8WIfqQVCkkUZ4nVbc2Wq8EzeNTF7zWLpVE68M9gRfgcnpsYoN73PdcT0ByfPpBFXxQYZ9OQVGvLqT0n96_n0xzM96RzwcYjQuk6Mw'
export DIRECTOR='token_value_2'
export PRODUCER='token_value_3'
