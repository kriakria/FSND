import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import setup_db, Movie, Actor, Cast, db
from auth.auth import AuthError, requires_auth, get_token_auth_header


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

    # Get the cast from the database

    def get_cast():
        casts = Cast.query.all()

        cast_data = []

        for cast in casts:
            cast_data.append({
                'id': cast.id,
                'movie_id': cast.movie_id,
                'actor_id': cast.actor_id
            })

        if len(cast_data) == 0:
            abort(404)

        return cast_data

    @app.route('/capstone')
    def capstone_info_page():
        return 'The Capstone Casting Agency info page'

    @app.route('/')
    def starter_page():
        return 'Welcome to the Capstone Casting Agency'

    '''
    ACTORS
    GET actors. This enpoint displays all the actors in the database.
    This route can be accessed by the roles Casting Assistant,
    Casting Director and Executive Producer.
    '''

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors-list')
    def list_actors(jwt):
        # def list_actors():

        if len(get_actors()) == 0:
            abort(401)

        try:
            return jsonify({
                'success': True,
                'actors': get_actors(),
                'total_actors': len(get_actors())
            }), 200

        except Exception as e:
            print(e)
            abort(404)

    # TEST

    @app.route('/actors-test', methods=['GET'])
    def test_list_actors():
        # def list_actors():

        if len(get_actors()) == 0:
            abort(401)

        try:
            return jsonify({
                'success': True,
                'actors': get_actors(),
                'total_actors': len(get_actors())
            }), 200

        except Exception as e:
            print(e)
            abort(404)

    # Display an actor with a selected actor ID.

    @app.route('/actors/<actor_id>', methods=['GET'])
    def get_one_actor(actor_id):
        actor = Actor.query.get(actor_id)

        actor_data = []

        actor_data.append({
            'id': actor.id,
            'name': actor.name,
            'age': actor.age,
            'gender': actor.gender
        })

        return jsonify({
            'success': True,
            'actor': actor_data
        })

    '''
    DELETE actors. Actors can be deleted from the database.
    This route can be accessed by the roles Casting Director
    and Executive Producer, with the permission 'delete:actors'.
    '''

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(jwt, actor_id):

        try:
            actor = Actor.query.get(actor_id)

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

        except Exception as e:
            print(e)
            abort(422)  # not able to process the request

    '''
    POST actors. Actors can be created in the database.
    This route can be accessed by the roles Casting Director
    and Executive Producer.
    '''

    @app.route('/actors/create', methods=['POST'])
    def create_actor():

        # print("in create_actor")
        # data = request.get_json()
        data = request.get_json()
        print(data)

        if data is None:
            # print("data is none")
            new_name = 'test name'
            new_age = 20
            new_gender = 'male'            

        else:
            new_name = data.get('name', None)
            new_age = data.get('age', None)
            new_gender = data.get('gender', None)

        try:
            actor = Actor(name=new_name, age=new_age, gender=new_gender)
            print(actor)
            actor.insert()

            return jsonify({
                'success': True,
                'actors': get_actors(),
                'total_actors': len(get_actors()),
                'name': new_name,
                'age': new_age,
                'gender': new_gender
            })

        except Exception as e:
            print(e)
            abort(422)  # not able to process the request

    # TEST
    @app.route('/actors/create-test', methods=['POST'])
    def test_create_actor():

        # print("in create_actor")
        # data = request.get_json()
        data = request.get_json()
        print(data)

        if data is None:
            # print("data is none")
            # new_name = 'test name'
            # new_age = 20
            # new_gender = 'male'
            print("data is none")

        else:
            new_name = data.get('name', None)
            new_age = data.get('age', None)
            new_gender = data.get('gender', None)

        try:
            actor = Actor(name=new_name, age=new_age, gender=new_gender)
            print(actor)
            actor.insert()

            return jsonify({
                'success': True,
                'actors': get_actors(),
                'total_actors': len(get_actors()),
                'name': new_name,
                'age': new_age,
                'gender': new_gender
            })

        except Exception as e:
            print(e)
            abort(422)  # not able to process the request

    # Edit actors

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    def actor(actor_id):

        actor_update = request.get_json(force=True)
        print(actor_update)
        new_name = actor_update.get('name', None)
        new_age = actor_update.get('age', None)

        try:
            actor = Actor.query.get(actor_id)
            print(actor)

            if actor is None:
                print("actor is none")
                abort(404)

            actor.update()

            return jsonify({
                'success': True,
                'updated': actor,
                'actors': get_actors(),
                'total_actors': len(get_actors())
            })

        except Exception as e:
            print(e)
            abort(422)  # not able to process the request

    '''
    MOVIES
    GET movies. This enpoint displays all the movies in the database.
    This route can be accessed by the roles Casting Assistant,
    Casting Director and Executive Producer.
    '''

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies-list')
    def list_movies(jwt):

        return jsonify({
            'success': True,
            'movies': get_movies(),
            'total_movies': len(get_movies())
        })

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(jwt, movie_id):

        try:
            movie = Movie.query.get(movie_id)

            if movie is None:
                abort(404)

            else:
                movie.delete()

            return jsonify({
                'success': True,
                'deleted': movie,
                'actors': get_movies(),
                'total_actors': len(get_movies())
            })

        except BaseException:
            abort(422)  # not able to process the request

    '''
    POST movies. Movies can be created in the database.
    This route can be accessed by the role Executive Producer.
    '''

    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(jwt):

        data = request.get_json()
        new_title = data.get('title', None)
        new_release_date = data.get('release_date', None)

        try:
            movie = Movie(title=new_title, release_date=new_release_date)
            movie.insert()

            return jsonify({
                'success': True,
                'movies': get_movies(),
                'total_movies': len(get_movies()),
                'title': new_title,
                'release_date': new_release_date,
            })

        except BaseException:
            abort(422)  # not able to process the request

    '''
    PATCH movies. Movies can be created in the database.
    This route can be accessed by the roles Casting Director
    and Executive Producer.
    '''

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def edit_movie(jwt, movie_id):

        movie_update = request.get_json()
        new_title = movie_update.get('title', None)
        new_release_date = movie_update.get('release_date', None)

        try:
            movie = Movie.query.get(movie_id)

            if movie is None:
                abort(404)

            movie.update()

            return jsonify({
                'success': True,
                'deleted': movie,
                'actors': get_movies(),
                'total_actors': len(get_movies())
            })

        except Exception as e:
            print(e)
            abort(422)  # not able to process the request

    '''
    CAST
    GET cast. This enpoint displays all the movies and associated
    actors.
    This route can be accessed by the roles Casting Assistant,
    Casting Director and Executive Producer.
    '''

    @app.route('/cast', methods=['GET'])
    @requires_auth('get:actors-list')
    def list_cast(jwt):

        return jsonify({
            'success': True,
            'cast': get_cast()
        })

    '''
    ERROR HANDLING
    The error handlers use the @app.errorhandler(error) decorator.
    Each error handler returns the error coda and the approprate message.
    '''

    @app.errorhandler(400)
    def bad_request(error):

        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):

        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not found'
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):

        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method not allowed'
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                        "success": False,
                        "error": 422,
                        "message": "unprocessable"
                        }), 422

    @app.errorhandler(500)
    def server_error(error):

        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal server error'
        }), 500

    '''
    The AuthError error handler returns the error and the error code.
    '''

    @app.errorhandler(AuthError)
    def autherror(e):
        return jsonify(e.error), e.status_code

    return app


APP = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=8080, debug=True)
    APP.run(host='localhost', port=5000, debug=True)
