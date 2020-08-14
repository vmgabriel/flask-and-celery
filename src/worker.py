"""
Module of Celery Build
"""

# Libraries
from typing import Any
from celery import Celery

from src.app import create_worker_app


def make_worker(app: Any) -> Celery:
    """Build and return Celery App"""
    app_celery = Celery(
        app.import_name,
        broker='redis://localhost:6379'
    )

    app_celery.conf.update(app.config)

    TaskBase = app_celery.Task

    class ContextTask(TaskBase):
        """Class Context Task"""
        def __call__(self, *args, **kwargs):
            """Use In Server call"""
            with app.app_context():
                return self.run(*args, **kwargs)

    app_celery.Task = ContextTask
    return app_celery


flask_app = create_worker_app()
celery = make_worker(flask_app)
