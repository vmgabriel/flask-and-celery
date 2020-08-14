"""
Module of Celery Build
"""

# Libraries
# from __future__ import absolute_import
from typing import Any
from celery import Celery


def make_celery(app: Any) -> Celery:
    """Build and return Celery App"""
    app_celery = Celery(
        app.name,
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
