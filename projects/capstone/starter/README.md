# CAPSTONE

## The Capstone Casting Agency

The Capstone Casting Agency is passionate about good movies. The agency's speciality is to create excellent movies and find the best actors for them.

The agency has and maintains a database of actors and movies, and an overview of which movies have which actors.

## Run the app on Heroku

The application is live at this URL:
<https://capstone-casting-agency-kigi.herokuapp.com/>

## Testing endpoints

The endpoints can be tested with curl, e.g.:

```python
curl <https://capstone-casting-agency-kigi.herokuapp.com/actors> -X GET -H 'Authorization: Bearer <token>'

```

## Code style

The code style adheres to the PEP 8 style guide: <https://www.python.org/dev/peps/pep-0008/>.

## About the stack

The backend is ready, but the frontend is yet to be built.

### Backend

The main code is in app.py where the endpoints are defined and models.py is referenced for DB and SQLAlchemy setup.

Main libraries used:

- Flask-SQLAlchemy, adds support for SQLAlchemy ORM
- Flask-Migrate, for handling all database migrations
- Flask-CORS

Project structure:

- README.md
- app.py
- models.py
- migrations
  - versions
  - alembic.ini
- .env
- auth
  - auth.py
  - .env
- .gitignore
- test_app.py
- requirements.txt

### Frontend

Frontend is not yet built.

## Running the app locally

1. Clone repository.
2. pip install requirements.txt
3. Run following commands:
    1. flask db init
    2. flask db migrate
    3. flask db upgrade
4. Start server by running:
    1. export FLASK_APP=app.py (on Windows: set FLASK_APP=app.py)
    2. flask run --reload

## Endpoints

**The landing page for the agency**
<http://localhost:5000/>

> Welcome to the Capstone Casting Agency

**The Capstone information page**
<http://localhost:5000/capstone>

> The Capstone Casting Agency info page.

**Show all actors**
GET <http://localhost:5000/actors>

Response:

```python
    {
        "actors": [
            {
                "age": 25,
                "gender": "female",
                "id": 1,
                "name": "cindy"
            }
        ],
        "success": true,
        "total_actors": 1
    }
```

**Delete actors**
DELETE <http://localhost:5000/actors/1>

Response:

```python
    {
        "actors": [
            {
                "age": 47,
                "gender": "male",
                "id": 3,
                "name": "John Smith"
            },
            {
                "age": 23,
                "gender": "female",
                "id": 4,
                "name": "Mary James"
            }
        ],
        "deleted":{
            "age": 25,
            "gender": "female",
            "id": 1,
            "name": "cindy"}
        "success": true,
        "total_actors": 10,        
    }
```

**Create actors**
POST <http://localhost:5000/actors/create>

Request:

```python
{
    "name": "Cameron Diaz",
    "age": 45,
    "gender": "female"
}
```

Response:

```python
    {
        "actors": [
            {
                "age": 25,
                "gender": "female",
                "id": 1,
                "name": "cindy"
            },
            {
                "age": 45,
                "gender": "female",
                "id": 6,
                "name": "Cameron Diaz"
            }
        ],
        "success": true,
        "total_actors": 5,
        "name": "Cameron Diaz",
        "age": 45,
        "gender": "female"
    }
```

**Edidt actors**
POST <http://localhost:5000/actors/6>

Request:

```python
{
    "name": "Michael John",
    "age": 41,
    "gender": "male"
}
```

Response:

```python
    {
        "actors": [
            {
                "age": 25,
                "gender": "female",
                "id": 1,
                "name": "cindy"
            },
            {
                "age": 41,
                "gender": "male",
                "id": 6,
                "name": "Michael John"
            }
        ],
        "success": true,
        "total_actors": 2,
        "updated": {
                "age": 41,
                "gender": "male",
                "id": 6,
                "name": "Michael John"
            }
    }
```

The same structure and concept applies to Movies.

## Auth0 account

Roles and Users are defined in Auth0.
The Auth0 account details are set as environment variables in auth/.env.

### Casting Assistant

User: casting_assistant@kristin.com

Password: TestUserCA1

Submitted token (which can be expired at the time of review):

```python
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpIWGZWZ3plREptV2xBeWNpcDRxdyJ9.eyJpc3MiOiJodHRwczovL2tyaWFrcmlhLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA1MzBkZjhlYzRhMzAwNmVlMzUxZjMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAvY2Fwc3RvbmUiLCJpYXQiOjE2MTEzMTY3MTksImV4cCI6MTYxMTQwMzExOSwiYXpwIjoianpDTWJhc1YzVU9XS3d4OWtaY2hKSXpTOHFxZWlBaEQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMtbGlzdCIsImdldDptb3ZpZXMtbGlzdCJdfQ.ow8FkxWBbRwt6V-FWeqn85bhFVFNLMzXEOEbZE1Bfy8L2_v9E-btsZ2tGS2YcKyPYo8EZfioAfMR1sXf9egK0KuidN93jjXF3q_r_WIHIAJOpx-YOSV7SI5B9MoNj8uzypbslMQd7nGIa_vMg9KLGx95bHrZg9U12569kr_zGGKp_jr_8kzuXP19hhmGtDPrLRQ_REthF5z88QDJjih2w0U6Q75c5B30Ur6saWJ5yJGmXsMHnM1J6V3BhIZlB9vSWeA7If2nPTlae-p1SiRzyCgomxvE4TWB5pNh6wxfK0v51jB3UoYVxzrp2ilEyWFwOAvPpq0jkWuLsuGMozOR3Q
```

### Casting Director

User: casting_director@kristin.com

Password: TestUserCD1

Submitted token (which can be expired at the time of review):

```python
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpIWGZWZ3plREptV2xBeWNpcDRxdyJ9.eyJpc3MiOiJodHRwczovL2tyaWFrcmlhLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA1MzIwZjk4YjY4OTAwNzUxZGJhYTUiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAvY2Fwc3RvbmUiLCJpYXQiOjE2MTEzMTkwNTMsImV4cCI6MTYxMTQwNTQ1MywiYXpwIjoianpDTWJhc1YzVU9XS3d4OWtaY2hKSXpTOHFxZWlBaEQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzLWxpc3QiLCJnZXQ6bW92aWVzLWxpc3QiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.iilsIprpL79NPZR1irs8MQeRtU9OjLAxoA9zmyUlI7a06gz5TDTlnLmvfOn8n_Bu27Bjw0Smz5hz4vkM9ufbwVFLDWa6iWs_Z-TjaRiIAL5T5ihJqNIwTOxYSWWtnyAlN0LR_44gXaKSSF2nFoyO_KeXJKSnhMwG9XuVvS3X9kSoAs_q313s7ZsRnZjtETBzs2HtUgcP9hLSa6XEOWNd6w0j7AAnEoB0OQbuEgO3Twa-nuDmzYcyhR5BgLf2HSunvICLne6iR3NlZ_5dNqwtvcnkGxeHoP0v-bzH-lqlQNXfdU4EyT9sGzDTZ8sIJDSvydwvGmF1aqpoyaZdW1rJRA
```

### Executive Producer

User: executive_director@kristin.com

Password: TestUserED1

Submitted token (which can be expired at the time of review):

```python
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpIWGZWZ3plREptV2xBeWNpcDRxdyJ9.eyJpc3MiOiJodHRwczovL2tyaWFrcmlhLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA1MzI2MjAzN2FjMjAwNzRiNjJkMWYiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAvY2Fwc3RvbmUiLCJpYXQiOjE2MTEzMTg4MDIsImV4cCI6MTYxMTQwNTIwMiwiYXpwIjoianpDTWJhc1YzVU9XS3d4OWtaY2hKSXpTOHFxZWlBaEQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycy1saXN0IiwiZ2V0Om1vdmllcy1saXN0IiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.aSC_CIVMfKzk85HqPZ4f3WIw6zmETdk4HK78p4Bko6ienPTp790EIXIMjxQkatljC3P4Bwo3Cng9ym1PjqDN3pux8WjlOG0XF7F8n2LNpQ9q1m4VjV202XBfs4kzaCah4_yIJoK5MPZPo4vvQo3myZa-LhoJ2Osi0olHir4rfNPKIgs-vk7iTm_xcTkcU44ZefvraHwOIOWvzKZ1AmloON4vq9b3rMluQIykGdDPX4Nejp4bubQrCzvRPYjyKQOKCeR23saoxz0CxJPSIYh-E5HQl5-wPTBdw9-v2iTv2OSsboxjbJDAVkgTYzI6LEp47nqigyeC373zF1h1TrnGHw
```

## Testing

### test_app.py

Two test cases are written for each endpoint, one that should pass and one fail.
Before running the test cases, make sure that the movie_ids and actor_ids that are to be deleted or patched exist in the database.

How to run the tests:

```python
python test_app.py
```

### Postman

- Exported collection with configured tokens can be found at: Capstone.postman_collection.json
- Test results containing 27 successful cases: Capstone.postman_test_run.json
