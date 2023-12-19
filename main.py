from fastapi import FastAPI

from models import Task

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


@app.get("/tasks/")
async def get_tasks() -> dict:
    return {}


@app.get("/tasks/{task_id}")
async def get_task(task_id: int) -> dict:
    return {"task_id": task_id}


@app.post("/create_task")
async def create_task(task: Task) -> dict:
    return {"task": task.title}
