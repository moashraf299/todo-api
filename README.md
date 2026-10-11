# Todo API

A simple REST API built with FastAPI to manage a list of tasks.
Tasks are stored in a JSON file.

## Endpoints
- `GET /tasks` - list all tasks
- `POST /tasks` - add a task (body: `{"title": "..."}`)
- `DELETE /tasks/{task_id}` - delete a task by its number

## Run
```
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs
