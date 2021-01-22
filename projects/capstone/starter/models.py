import os
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json
from dotenv import load_dotenv

db_name = 'capstone'


load_dotenv()  # loading the environment variables
# getting the token values:
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

# get database user and password from env file
# db_user = os.environ['DB_USER']
# db_password = os.environ['DB_PASSWORD']

# set the Heroku database path
db_path = "postgres://mswtwueikeynok:074a6ff712bd6dab3ec93118b31d70ac10b111f32d17c7e4c8afc1c0d18a23cb@ec2-3-216-181-219.compute-1.amazonaws.com:5432/dboednp2dv6b26"

# local db path
# db_path = "postgres://{}:{}@{}/{}".
# format(db_user, db_password, 'localhost:5432', db_name)

db = SQLAlchemy()


def setup_db(app, database_path=db_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Movie
'''


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(DateTime)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }

    '''def __repr__(self):
        return f'<Movie id {self.id}, Movie title {self.title}, \
            Movie release date {self.release_date}>'
    '''


'''
Actor
'''


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    '''def __repr__(self):
        return f'<Actor id {self.id}, Actor name {self.name}, \
            Actor age {self.age}, Actor gender {self.gender}>
    '''


'''
Cast
'''


class Cast(db.Model):
    __tablename__ = 'casts'

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    actor_id = Column(Integer, ForeignKey('actors.id'), nullable=False)

    def __init__(self, movie_id, actor_id):
        self.movie_id = movie_id
        self.actor_id = actor_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'move_id': self.movie_id,
            'actor_id': self.actor_id,
        }

    '''def __repr__(self):
        return f'<Cast id {self.id}, movie_id {self.movie_id}, \
            actor_id {self.actor_id}>'
    '''
