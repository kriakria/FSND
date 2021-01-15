import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import setup_db, Movie, Actor, Cast, db

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app)

  migrate = Migrate(app, db)

  # CORS Headers
  @app.after_request
  def after_request(response):
    response.headers.add(
      'Access-Control-Allow-Headers',
      'Content-Type, Authorization, true')
    response.headers.add(
      'Access-Control-Allow-Headers',
      'GET, PATCH, POST, DELETE, OPTIONS')

    return response

# Get the actors from the database

  def get_actors():
    actors = Actor.query.all()

    actors_data = []

    for actor in actors:
      actors_data.append({
        'id': actor.id,
        'name': actor.name,
        'age': actor.age,
        'gender': actor.gender
      })

    if len(actors) == 0:
      abort(404)      

    return actors_data

# Get the movies from the database

  def get_movies():
    movies = Movie.query.all()

    movie_data = []

    for movie in movies:
      movie_data.append({
        'id': movie.id,
        'title': movie.title,
        'release_date': movie.release_date
      })

    if len(movie_data) == 0:
      abort(404)

    return movie_data
  
  @app.route('/')
  def starter_page():
    return 'hello'

# Actors

# GET actors. This enpoint displays all the actors in the database

  @app.route('/actors', methods=['GET'])
  def list_actors():

    return jsonify({
      'success': True,      
      'actors': get_actors(),
      'total_actors': len(get_actors())
    })

  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  def delete_actors(actor_id):

    try:
      actor = Actor.query.get(actor_id).one_or_none()

      if actor is None:
        abort(404)

      else:
        actor.delete()

        return jsonify({
          'success': True,
          'deleted': actor,
          'actors': get_actors(),
          'total_actors': len(get_actors())
        })
    
    except BaseException:
      abort(422) # not able to process the request


# Movies

# GET movies. This enpoint displays all the movies in the database.

  @app.route('/movies', methods=['GET'])
  def list_moview():

    return jsonify({
      'success': True,
      'movies': get_movies(),
      'total_movies': len(get_movies())
    })

  return app

APP = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=8080, debug=True)
    APP.run(host='localhost', port=5000, debug=True)