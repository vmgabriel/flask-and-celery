"""
module of Calculator
"""
# Modules
import random
import time
from typing import Any

from src.extensions import celery


@celery.task()
def add(_x: Any, _y: Any) -> Any:
    """add value"""
    return _x + _y


@celery.task()
def long_process() -> str:
    """Long Process"""
    time.sleep(15)
    return "Hello World"


@celery.task(bind=True)
def long_task(self):
    """Background task that runs a long function with progress reports."""

    verb = ["Starting up", "Booting", "Repairing", "Loading", "Checking"]
    adjective = ["master", "radiant", "silent", "harmonic", "fast"]
    noun = ["solar array", "particle reshaper", "cosmic ray", "orbiter", "bit"]
    message = ""
    total = random.randint(10, 50)

    for i in range(total):
        if not message or random.random() < 0.25:
            message = "{0} {1} {2}...".format(
                random.choice(verb),
                random.choice(adjective),
                random.choice(
                    noun
                )
            )
        self.update_state(
            state="PROGRESS", meta={
                "current": i,
                "total": total,
                "status": message
            }
        )
        time.sleep(1)

    return {
        "current": 100,
        "total": 100,
        "status":
        "Task completed!",
        "result": 42
    }
