import flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)
DSN = 'postgresql+psycopg2://admin:1234@127.0.0.1:5432/advertising_site_db'
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=DSN)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Advertising(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    description = db.Column(db.String(128))
    date_of_creation = db.Column(db.Date())
    owner = db.Column(db.String(64), index=True)


@app.route('/advertisings/<int:advertising_id>', methods=['GET'])
def get(advertising_id):
    advertising = Advertising.query.get(advertising_id)
    if advertising is None:
        raise NotFound
    return flask.jsonify({
        'id': advertising.id,
        'title': advertising.title,
        'description': advertising.description,
        'date_of_creation': advertising.date_of_creation,
        'owner': advertising.owner
    })


@app.route('/advertisings/', methods=['POST'])
def post():
    advertising_data = request.json
    advertising = Advertising(**advertising_data)
    db.session.add(advertising)
    db.session.commit()
    return flask.jsonify({'id': advertising.id})


@app.route('/advertisings/<int:advertising_id>', methods=['DELETE'])
def delete_ad(advertising_id):
    advertising = Advertising.query.get(advertising_id)
    if advertising is None:
        raise NotFound
    db.session.delete(advertising)
    db.session.commit()
    return flask.jsonify({'result': True})


class NotFound(Exception):
    message = 'Not Found'
    status_code = 404


@app.errorhandler(NotFound)
def error_handler(error):
    response = flask.jsonify({'error': error.message})
    response.status_code = error.status_code
    return response


app.run(host='127.0.0.1', port=5000)