import os, click

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


""" SQLAlchemy ->  Conexao com o banco """
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

"""  """

""" Registrando o nome do commando ->  Conexão com o banco """
@click.command('init-db')
def init_db_command():
    global db
    with current_app.app_context():
        db.create_all()
    click.echo('Initialized the database.')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///diobank.sqlite',
        
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Rota 
    


##Registro de comandado  / inicialização do banco - Conexão com o banco
    app.cli.add_command(init_db_command)
    db.init_app(app)

    return app