import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from app import create_app
from models import setup_db, Actor, Movie, Cast
from auth.auth import AuthError, requires_auth, verify_decode_jwt


load_dotenv()  # loading the environment variables

# db_user = os.getenv('DB_USER')
# db_password = os.getenv('DB_PASSWORD')

# get database user and password from env file
# db_user = os.environ['DB_USER']
# db_password = os.environ['DB_PASSWORD']


# This class represents the Capstone test case
class CapstoneTestCase(unittest.TestCase):
    # Define test variables and initialize app.
    def setUp(self):
        self.app = create_app(test_config=True)
        self.client = self.app.test_client

        # context = self.app.test_client
        # context.push()

        # from models import db
        # self.db = db
        # self.db.init_app(self.db)
        # with self.app.app_context():
        # self.db.create_all()

        self.assistent = os.getenv('ASSISTENT')
        self.exec_producer = os.getenv('EXEC_PROD')

        self.db_name = "capstone_test"
        self.db_user = os.environ['DB_USER']
        self.db_pw = os.environ['DB_PASSWORD']
        self.database_path = "postgres://{}:{}@{}/{}". \
            format(self.db_user, self.db_pw, 'localhost:5432', self.db_name)

        setup_db(self.app, self.database_path)

        self.new_movie = {
            'title': 'Jurassic Park',
            'release_date': '09-06-1993'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    # Executed after each test
    def tearDown(self):
        pass

# -------------------------------------------ACTORS----------------------------
# ------------------------------------Testing list actors----------------------

# This test should pass, with a token from a casting assistent
    def test_list_actors(self):
        res = self.client(). \
            get('/actors',
                headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['total_actors'])

# This test should fail, without a token from a casting assistent
    def test_401_list_actors_no_auth(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

# ------------------------------------Testing creating actors-----------------
# This test should pass, with a token from an executive producer
    def test_create_actors(self):
        res = self.client(). \
            post('/actors/create',
                 headers={'Authorization': 'Bearer ' + self.exec_producer},
                 json={'name': 'Johnny'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_actor'])
        self.assertTrue(data['actors'])
        self.assertTrue(data['total_actors'])

# This test should fail, without including a name of the actor
    def test_400_create_actors(self):
        res = self.client(). \
            post('/actors/create',
                 headers={'Authorization': 'Bearer ' + self.exec_producer},
                 json={'age': 4})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

# ------------------------------------Testing editing actors-------------------

    # This test should pass, with a token from an executive producer
    def test_patch_actors(self):
        res = self.client(). \
            patch('/actors/7',
                  headers={'Authorization': 'Bearer ' + self.exec_producer},
                  json={'name': 'Johnny'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated']['id'], 7)
        self.assertTrue(data['updated'])
        self.assertTrue(data['actors'])
        self.assertTrue(data['total_actors'])

# This test should fail, without including a name of the actor
    def test_400_patch_actors(self):
        res = self.client(). \
            patch('/actors/7',
                  headers={'Authorization': 'Bearer ' + self.exec_producer},
                  json={'age': 4})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

# ------------------------------------Testing delete actors--------------------
    # This test should pass, with a token from an executive producer
    def test_delete_actors(self):
        res = self.client(). \
            delete('/actors/43',
                   headers={'Authorization': 'Bearer ' + self.exec_producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        self.assertTrue(data['actors'])
        self.assertTrue(data['total_actors'])

    # This test should fail, with a token from an assistent
    def test_401_delete_actors(self):
        res = self.client(). \
            delete('/actors/7',
                   headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

# ------------------------------------------MOVIES-----------------------------
# ------------------------------------Testing list movies----------------------

    # This test should pass, with a token from a casting assistent
    def test_list_movies(self):
        res = self.client(). \
            get('/movies',
                headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(data['total_movies'])

    # This test should fail, without a token from a casting assistent
    def test_401_list_movies_no_auth(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

# ------------------------------------Testing creating movies-----------------
    # This test should pass, with a token from an executive producer
    def test_create_movies(self):
        res = self.client(). \
            post('/movies/create',
                 headers={'Authorization': 'Bearer ' + self.exec_producer},
                 json={'title': 'Reality bites'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_movie'])
        self.assertTrue(data['movies'])
        self.assertTrue(data['total_movies'])

    # This test should fail, without including a name of the actor
    def test_400_create_movies(self):
        res = self.client(). \
            post('/movies/create',
                 headers={'Authorization': 'Bearer ' + self.exec_producer},
                 json={'release_date': '01-01-2021'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

# ------------------------------------Testing editing movies-------------------

    # This test should pass, with a token from an executive producer
    def test_patch_movies(self):
        res = self.client(). \
            patch('/movies/7',
                  headers={'Authorization': 'Bearer ' + self.exec_producer},
                  json={'title': 'Batman', 'release_date': '01-02-2023'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated']['id'], 7)
        self.assertTrue(data['updated'])
        self.assertTrue(data['movies'])
        self.assertTrue(data['total_movies'])

# This test should fail, without including a name of the actor
    def test_400_patch_movies(self):
        res = self.client(). \
            patch('/movies/7',
                  headers={'Authorization': 'Bearer ' + self.exec_producer},
                  json={'release_date': '01-01-8008'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

# ------------------------------------Testing delete movies--------------------

    # This test should pass, with a token from an executive producer
    def test_delete_movies(self):
        res = self.client(). \
            delete('/movies/12',
                   headers={'Authorization': 'Bearer ' + self.exec_producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        self.assertTrue(data['movies'])
        self.assertTrue(data['total_movies'])

    # This test should fail, with a token from an assistent
    def test_404_delete_movies(self):
        res = self.client(). \
            delete('/movies/8',
                   headers={'Authorization': 'Bearer ' + self.assistent})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
