# CAPSTONE

## The Capstone Casting Agency

The Capstone Casting Agency is passionate about good movies. The agency's speciality is to create excellent movies and find the best actors for them.

The agency has and maintains a database of actors and movies, and an overview of which movies have which actors.

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

## Running the app

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
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpIWGZWZ3plREptV2xBeWNpcDRxdyJ9.eyJpc3MiOiJodHRwczovL2tyaWFrcmlhLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA1MzBkZjhlYzRhMzAwNmVlMzUxZjMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAvY2Fwc3RvbmUiLCJpYXQiOjE2MTEyMjI2MTMsImV4cCI6MTYxMTMwOTAxMywiYXpwIjoianpDTWJhc1YzVU9XS3d4OWtaY2hKSXpTOHFxZWlBaEQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMtbGlzdCIsImdldDptb3ZpZXMtbGlzdCJdfQ.THozfeDZxDj4erg8Bnx84bt2liTp_vp_hwM-gCSWrvTgYbJYwZbv_ET6bMewF79ddq5AKSJbIaXyAa_o5zMMDrrTxCxO5Ns5YUIfWqXsq0-WK4V15iAP4jRcbxKyPvUDIFHem6QEXNwdzrAn2dVs9_JxgxjkKz8imChWrNLJSJmfhuDioHsqTeRzwUKb-vjq5vp6PaFvTFuDi_BGf9bAB8Hd7BdlSTfYpKprySW_PTQCQnEaQ8WIfqQVCkkUZ4nVbc2Wq8EzeNTF7zWLpVE68M9gRfgcnpsYoN73PdcT0ByfPpBFXxQYZ9OQVGvLqT0n96_n0xzM96RzwcYjQuk6Mw
```

### Casting Director

User: casting_director@kristin.com

Password: TestUserCD1

Submitted token (which can be expired at the time of review):

```python
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpIWGZWZ3plREptV2xBeWNpcDRxdyJ9.eyJpc3MiOiJodHRwczovL2tyaWFrcmlhLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA1MzIwZjk4YjY4OTAwNzUxZGJhYTUiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAvY2Fwc3RvbmUiLCJpYXQiOjE2MTEyMjIyNTcsImV4cCI6MTYxMTMwODY1NywiYXpwIjoianpDTWJhc1YzVU9XS3d4OWtaY2hKSXpTOHFxZWlBaEQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzLWxpc3QiLCJnZXQ6bW92aWVzLWxpc3QiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.h1ia1lHU9gja2YWJ7TOzeTyNLLNyKXGgzisdsaVh7VbLwXcoeXS9g4sjNAuvlgvKrTD7M0f8tiLB-XI5e_lQOpmOiVpjXpUmAWn_7FpxkuQCBCPYh_dVGxFe0yCdQDt6ULIM9wD0y2PuQf-oX-vldnqlql0tR0Rd0Wt5IvBWG2ur8OgxLhJQKSkaQGzp9C-hsDruzXVBkFaRq7UkV6Ps3aPpnzaf3xpU2NLbBtseH6lERyvu5Ar-FJUrJpwhfU__fiQnAGMiUv7W3xCcoQ8GUHFP8golCQPhgoxb020gDZDwpddB3hVBJcovtgPBC4SqhleVAwozYAxHn2PDfnHXQg
```

### Executive Producer

User: executive_director@kristin.com

Password: TestUserED1

Submitted token (which can be expired at the time of review):

```python
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpIWGZWZ3plREptV2xBeWNpcDRxdyJ9.eyJpc3MiOiJodHRwczovL2tyaWFrcmlhLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA1MzI2MjAzN2FjMjAwNzRiNjJkMWYiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAvY2Fwc3RvbmUiLCJpYXQiOjE2MTEyMjI3ODQsImV4cCI6MTYxMTMwOTE4NCwiYXpwIjoianpDTWJhc1YzVU9XS3d4OWtaY2hKSXpTOHFxZWlBaEQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycy1saXN0IiwiZ2V0Om1vdmllcy1saXN0IiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.acgLBJf4GHGRrcvPf90YDhcFQTU2B-H-ntdWakI9CtEkCWt-PKpf3GQUmasGrFgqxY8rhB90KVYrukNfolyvcSKuXrRszfhCbJTedsVPUDOXP6TNN4ndPIY0jUXFZVAUCqMAl2nmH5QDwZq1fIaiTi3i8n5-_5YE6JyzLcGHelNCmOUGR9sUcfsFdehloKkBeg1cpcccEaSpcpbPK07DY6xee7A_bLAmsWUpKSswesbs3Ra4fajRW4dY0iKokVNvtTgrszFqiI8vfnAPUT_37lDrU44GN020KOli8lsCCB8ngoZihOeIjMTg-jGllymQ298Npojvzgsf9AWltg_akQ
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
