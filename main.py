from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

class Task(BaseModel):
    title: str

filename = "tasks.json"

def load_tasks():
    if os.path.exists(filename):
        with open(filename) as file:
            return json.load(file)
    else:    
        return []
        
tasks = load_tasks()
        
        
def save_tasks(tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)
            

@app.get("/")
def home():
    return {"message":"Hello API"}

@app.get("/about")
def about():
    return {"title":"My first API","author":"Mohamed"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task:Task):
    tasks.append(task.title)
    save_tasks(tasks)
    return{"message":"Task Added.", "tasks":tasks}

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    if 1 <= task_id <= len(tasks):
        tasks.pop(task_id - 1)
        save_tasks(tasks)
        return{"message":"Task Deleted.", "tasks":tasks}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

