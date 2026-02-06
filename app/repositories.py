from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session
from .models import Task, TaskCreate
from .models_orm import TaskORM 

class ITaskRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def create(self, task: TaskCreate) -> Task:
        pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def update(self, task: Task) -> Optional[Task]:
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> Optional[Task]:
        pass

class InMemoryTaskRepository(ITaskRepository):
    # ... (ส่วน InMemory ไม่ต้องแก้ เพราะไม่ได้ใช้ ORM) ...
    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def get_all(self) -> List[Task]:
        return self.tasks

    def create(self, task_in: TaskCreate) -> Task:
        task = Task(id=self.current_id, **task_in.dict())
        self.tasks.append(task)
        self.current_id += 1
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update(self, task: Task) -> Optional[Task]:
        for i, t in enumerate(self.tasks):
            if t.id == task.id:
                self.tasks[i] = task
                return task
        return None
    
    def get_by_title(self, title: str) -> Optional[Task]:
        for task in self.tasks:
            if task.title == title:
                return task
        return None

# --- ส่วนที่แก้ไขคือ Class นี้ ---
class SqlTaskRepository(ITaskRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Task]:
        tasks = self.session.query(TaskORM).all()
        # แก้จุดที่ 1: ใช้ model_validate
        return [Task.model_validate(t) for t in tasks]

    def create(self, task_in: TaskCreate) -> Task:
        task = TaskORM(**task_in.dict())
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return Task.model_validate(task)

    def get_by_id(self, task_id: int) -> Optional[Task]:
        task = self.session.query(TaskORM).filter(TaskORM.id == task_id).first()
        return Task.model_validate(task) if task else None

    def update(self, task: Task) -> Optional[Task]:
        db_task = self.session.query(TaskORM).filter(TaskORM.id == task.id).first()
        if not db_task:
            return None
        
        db_task.title = task.title
        db_task.description = task.description
        db_task.completed = task.completed
        
        self.session.commit()
        self.session.refresh(db_task)
        return Task.model_validate(db_task)

    def get_by_title(self, title: str) -> Optional[Task]:
        task = self.session.query(TaskORM).filter(TaskORM.title == title).first()
        return Task.model_validate(task) if task else None