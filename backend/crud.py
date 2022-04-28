from sqlalchemy.orm import Session

from models import Todo
from schemas import TodoCreate, TodoDelete


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(text=todo.text)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int):
    db.query(Todo).filter_by(id=todo_id).delete()
    db.commit()
    return {"ok": True}