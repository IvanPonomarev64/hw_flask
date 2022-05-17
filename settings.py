import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from flask_mail import Mail
from flask import Flask
from flask_bcrypt import Bcrypt
from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


flask_app = Flask("app")
flask_app.config.from_object('config')
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:5001/0',
    CELERY_RESULT_BACKEND='redis://localhost:5001/1'
)
mail = Mail(flask_app)
created_by_celery = make_celery(flask_app)

bcrypt = Bcrypt(flask_app)

load_dotenv()
engine = create_engine(os.getenv("ENGINE"))
insp = inspect(engine)
Session = sessionmaker(bind=engine)
