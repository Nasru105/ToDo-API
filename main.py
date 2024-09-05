from fastapi import FastAPI, HTTPException, Depends
from flask_sqlalchemy.session import Session
from typing import Optional

from Dependencies import get_db
from Utilities import get_password_hash, create_access_token, verify_password, get_current_user
from models import User, Todo
from schemes import UserCreate, UserLogin, TodoResponse, TodoCreate, TodoUpdate, PaginatedTodos

# Инициализация
app = FastAPI()


# Роуты
@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, name=user.name, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    token = create_access_token({"sub": user.email})
    return {"token": token}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email})
    return {"token": token}

@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_todo = Todo(title=todo.title, description=todo.description, owner_email=current_user.email)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    if db_todo.owner_email != current_user.email:
        raise HTTPException(status_code=403, detail="Forbidden")
    db_todo.title = todo.title
    db_todo.description = todo.description
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    if db_todo.owner_email != current_user.email:
        raise HTTPException(status_code=403, detail="Forbidden")
    db.delete(db_todo)
    db.commit()
    return

@app.get("/todos", response_model=PaginatedTodos)
def get_todos(page: int = 1, limit: int = 10, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    offset = (page - 1) * limit
    todos_query = db.query(Todo).filter(Todo.owner_email == current_user.email)
    total = todos_query.count()
    todos = todos_query.offset(offset).limit(limit).all()
    return {
        "data": todos,
        "page": page,
        "limit": limit,
        "total": total
    }