from typing import List

from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class TodoCreate(BaseModel):
    title: str
    description: str

class TodoUpdate(BaseModel):
    title: str
    description: str

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str

class PaginatedTodos(BaseModel):
    data: List[TodoResponse]
    page: int
    limit: int
    total: int