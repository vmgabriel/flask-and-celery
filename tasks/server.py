
from __future__ import absolute_import

# Libraries
# from __future__ import absolute_import
from typing import Any
from celery import Celery
from flask import Flask


def make_celery(app: Any) -> Celery:
    """Build and return Celery App"""
    app_celery = Celery(
        app.import_name,
        backend=app.config.get('CELERY_RESULT_BACKEND'),
        broker=app.config.get('CELERY_BROCKER_URL')
    )

    app_celery.conf.update(app.config)


    class ContextTask(Celery.Task):
        """Class Context Task"""
        def __call__(self, *args, **kwargs):
            """Use In Server call"""
            with app.app_context():
                return self.run(*args, **kwargs)

    app_celery.Task = ContextTask

    return app_celery


flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(flask_app)


@celery.task()
def add_together(_a, _b):
    """a"""
    return _a + _b
