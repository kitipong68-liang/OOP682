# app/services.py
from fastapi import HTTPException
from typing import Optional
from .repositories import ITaskRepository
from .models import Task, TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        # Validation: ห้ามชื่อซ้ำ
        existing = self.repo.get_by_title(task_in.title)
        if existing:
            # Clean Code: Logic อยู่ที่นี่ ถูกต้องครับ!
            raise HTTPException(status_code=400, detail="Task with this title already exists")
        return self.repo.create(task_in)

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        return self.repo.get_by_id(task_id)

    def mark_task_complete(self, task_id: int) -> Optional[Task]:
        task = self.repo.get_by_id(task_id)
        if not task:
            return None
        task.completed = True
        return self.repo.update(task)