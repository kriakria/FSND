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

        context = self.app.test_client
        context.push()

        from models import db
        self.db = db
        self.db.init_app(self.db)
        with self.app.app_context():
            self.db.create_all()

        self.assistent_token = os.getenv('ASSISTENT')
        self.exec_prod_token = os.getenv('EXEC_PROD')

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

    def test_list_actors(self):
        res = self.client().get('/actors-test')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['total_actors'])

    def test_401_list_actors_no_auth(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    def test_delete_actors(self):
        res = self.client().get('/actors/11')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # self.assertTrue(data['actors'])
        # self.assertTrue(data['total_actors'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
