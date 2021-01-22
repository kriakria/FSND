#!/bin/bash

import os

db_user = os.dotenv('db_user')
db_password = os.dotenv('db_password')
db_name = 'capstone'

export db_path = "postgres://mswtwueikeynok:074a6ff712bd6dab3ec93118b31d70ac10b111f32d17c7e4c8afc1c0d18a23cb@ec2-3-216-181-219.compute-1.amazonaws.com:5432/dboednp2dv6b26"

# Auth0 complete before sumbitting
export AUTH0_DOMAIN = 'kriakria.eu.auth0.com'
export ALGORITHMS = ['RS256']
export API_AUDIENCE = 'http://localhost:5000/capstone'
export AUTH_CLIENT_ID = 'jzCMbasV3UOWKwx9kZchJIzS8qqeiAhD'

# Tokens

export ASSISTANT='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpIWGZWZ3plREptV2xBeWNpcDRxdyJ9.eyJpc3MiOiJodHRwczovL2tyaWFrcmlhLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA1MzBkZjhlYzRhMzAwNmVlMzUxZjMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAvY2Fwc3RvbmUiLCJpYXQiOjE2MTEzMTY3MTksImV4cCI6MTYxMTQwMzExOSwiYXpwIjoianpDTWJhc1YzVU9XS3d4OWtaY2hKSXpTOHFxZWlBaEQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMtbGlzdCIsImdldDptb3ZpZXMtbGlzdCJdfQ.ow8FkxWBbRwt6V-FWeqn85bhFVFNLMzXEOEbZE1Bfy8L2_v9E-btsZ2tGS2YcKyPYo8EZfioAfMR1sXf9egK0KuidN93jjXF3q_r_WIHIAJOpx-YOSV7SI5B9MoNj8uzypbslMQd7nGIa_vMg9KLGx95bHrZg9U12569kr_zGGKp_jr_8kzuXP19hhmGtDPrLRQ_REthF5z88QDJjih2w0U6Q75c5B30Ur6saWJ5yJGmXsMHnM1J6V3BhIZlB9vSWeA7If2nPTlae-p1SiRzyCgomxvE4TWB5pNh6wxfK0v51jB3UoYVxzrp2ilEyWFwOAvPpq0jkWuLsuGMozOR3Q'
export DIRECTOR='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpIWGZWZ3plREptV2xBeWNpcDRxdyJ9.eyJpc3MiOiJodHRwczovL2tyaWFrcmlhLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA1MzIwZjk4YjY4OTAwNzUxZGJhYTUiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAvY2Fwc3RvbmUiLCJpYXQiOjE2MTEzMTkwNTMsImV4cCI6MTYxMTQwNTQ1MywiYXpwIjoianpDTWJhc1YzVU9XS3d4OWtaY2hKSXpTOHFxZWlBaEQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzLWxpc3QiLCJnZXQ6bW92aWVzLWxpc3QiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.iilsIprpL79NPZR1irs8MQeRtU9OjLAxoA9zmyUlI7a06gz5TDTlnLmvfOn8n_Bu27Bjw0Smz5hz4vkM9ufbwVFLDWa6iWs_Z-TjaRiIAL5T5ihJqNIwTOxYSWWtnyAlN0LR_44gXaKSSF2nFoyO_KeXJKSnhMwG9XuVvS3X9kSoAs_q313s7ZsRnZjtETBzs2HtUgcP9hLSa6XEOWNd6w0j7AAnEoB0OQbuEgO3Twa-nuDmzYcyhR5BgLf2HSunvICLne6iR3NlZ_5dNqwtvcnkGxeHoP0v-bzH-lqlQNXfdU4EyT9sGzDTZ8sIJDSvydwvGmF1aqpoyaZdW1rJRA'
export PRODUCER='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpIWGZWZ3plREptV2xBeWNpcDRxdyJ9.eyJpc3MiOiJodHRwczovL2tyaWFrcmlhLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA1MzI2MjAzN2FjMjAwNzRiNjJkMWYiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAvY2Fwc3RvbmUiLCJpYXQiOjE2MTEzMTg4MDIsImV4cCI6MTYxMTQwNTIwMiwiYXpwIjoianpDTWJhc1YzVU9XS3d4OWtaY2hKSXpTOHFxZWlBaEQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycy1saXN0IiwiZ2V0Om1vdmllcy1saXN0IiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.aSC_CIVMfKzk85HqPZ4f3WIw6zmETdk4HK78p4Bko6ienPTp790EIXIMjxQkatljC3P4Bwo3Cng9ym1PjqDN3pux8WjlOG0XF7F8n2LNpQ9q1m4VjV202XBfs4kzaCah4_yIJoK5MPZPo4vvQo3myZa-LhoJ2Osi0olHir4rfNPKIgs-vk7iTm_xcTkcU44ZefvraHwOIOWvzKZ1AmloON4vq9b3rMluQIykGdDPX4Nejp4bubQrCzvRPYjyKQOKCeR23saoxz0CxJPSIYh-E5HQl5-wPTBdw9-v2iTv2OSsboxjbJDAVkgTYzI6LEp47nqigyeC373zF1h1TrnGHw'
