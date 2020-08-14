"""
Index Route of Server
"""

# Libraries
from datetime import datetime, timedelta
from flask import Blueprint, jsonify, url_for
from celery.result import AsyncResult

# Tasks
from src.tasks.calculator import long_process, long_task

# Configure the Route
mod = Blueprint('', __name__)


@mod.route('/')
def base():
    """Route Base"""
    return jsonify({
        'code': 200,
        'message': 'Flask Celery'
    }), 200


@mod.route('/about')
def about():
    """Route for knowledge of creators"""
    return jsonify({
        'code': 200,
        'message': 'About Data - Created By Gabriel Vargas'
    }), 200


@mod.route('/task')
def task():
    """Route task"""
    task_res = long_process.delay()
    print('task - ', task_res)
    return jsonify({
        'code': 200,
        'task': task_res.id,
        'message': 'About Data - Created By Gabriel Vargas'
    }), 200


@mod.route("/extend")
def index():
    """Add a new task and start running it after 10 seconds."""
    eta = datetime.utcnow() + timedelta(seconds=10)
    tsk = long_task.apply_async(eta=eta)
    return (
        jsonify(
            {"_links": {
                "task": url_for(
                    ".get_data",
                    task_id=tsk.id,
                    _external=True
                )
            }}
        ),
        202,
    )


@mod.route("/extend/<task_id>/", methods=["GET"])
def get_data(task_id):
    """Get Data"""
    tsk = AsyncResult(task_id)
    if tsk.state == "PENDING":
        # job did not start yet
        response = {"state": tsk.state, "status": "Pending..."}
    elif tsk.state != "FAILURE":
        response = {
            "state": tsk.state,
            "current": tsk.info.get("current", 0),
            "total": tsk.info.get("total", 1),
            "status": tsk.info.get("status", ""),
        }
        if "result" in tsk.info:
            response["result"] = tsk.info["result"]
    else:
        # something went wrong in the background job
        response = {
            "state": tsk.state,
            "current": 1,
            "total": 1,
            "status": str(tsk.info),  # this is the exception raised
        }
    return jsonify(response)
