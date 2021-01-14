import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import setup_db, Movie, Actor, Cast

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app)

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

  @app.route('/')
  def starter_page():
    return 'hello'

  return app

APP = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=8080, debug=True)
    APP.run(host='localhost', port=5000, debug=True)