from typing import Union
from celery.result import AsyncResult
from fastapi import FastAPI
from fastapi import Body, FastAPI, Form, Request
from fastapi.responses import JSONResponse
from worker import create_task

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/tasks", status_code=201)
async def run_task():
    task = create_task.delay(
        'https://ipaudio.club/wp-content/uploads/HQ/ANTRA/Make%20Your%20Bed/02.mp3?_=2')
    return JSONResponse({"task_id": task.id})


@app.get("/tasks/{task_id}")
async def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)
