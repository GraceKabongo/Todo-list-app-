from typing import List
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from .models import TaskModel
from .schema import GetTaskSchema, PostTaskSchema

api = NinjaAPI()


@api.post("/create-task")
def create_task(request, data: PostTaskSchema):
    task = TaskModel.objects.create(
        title=data.title,
        description=data.description,
        user=request.user
    )

    return {"id": task.id}

@api.get("/get-task/{task_id}", response=GetTaskSchema)
def get_task(request, task_id: str):
    task = get_object_or_404(TaskModel, id=task_id)

    return {
        "title": task.title,
        "description": task.description,
        "is_done": task.is_done,
        "user": task.user.id  # Return user ID instead of full user object
    }


@api.get("/get-tasks", response=List[GetTaskSchema])
def get_tasks(request):
    all_tasks = TaskModel.objects.filter(user=request.user).all()

    tasks = [
        GetTaskSchema(
            title=task.title,
            description=task.description,
            is_done=task.is_done,
            user=task.user.id
        ) 
        for task in all_tasks
    ]

    return tasks