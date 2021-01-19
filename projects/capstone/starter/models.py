import os
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json

db_name = 'capstone'

# get database user and password from env file
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']

# set the database path
db_path = "postgres://{}:{}@{}/{}". \
    format(db_user, db_password, 'localhost:5432', db_name)

db = SQLAlchemy()


def setup_db(app, database_path=db_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    # db.create_all()


'''
Movie
'''


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(DateTime)

    def __repr__(self):
        return f'<Movie id {self.id}, Movie title {self.title}, \
            Movie release date {self.release_date}>'


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
        db.session.delete()
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

    def __repr__(self):
        return f'<Cast id {self.id}, movie_id {self.movie_id}, \
            actor_id {self.actor_id}>'
