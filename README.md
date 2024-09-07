# ToDo List API with FastAPI

This is a simple yet powerful ToDo List API built using **FastAPI**, allowing users to manage their tasks efficiently. The API supports user registration, authentication via JWT tokens, and CRUD operations (Create, Read, Update, Delete) for tasks. The project is designed with scalability in mind, making it easy to integrate with other services or extend functionality.

## Features

- **User Registration & Authentication**: Secure user registration and login with password hashing and JWT-based authentication.
- **Task Management (CRUD)**: Allows users to create, update, retrieve, and delete tasks (todos).
- **Authorization**: Protects task management routes, ensuring that only authenticated users can create, modify, or delete their tasks.
- **Pagination**: Support for paginated retrieval of tasks, making it easy to manage large datasets.
- **SQLite Database**: Simple database setup with SQLite for local development (can be easily switched to PostgreSQL or MySQL for production).

## Endpoints

### User Authentication
- `POST /register`: Register a new user.
- `POST /login`: Login to obtain JWT token.

### ToDo Management
- `POST /todos`: Create a new task (requires JWT token).
- `GET /todos`: Retrieve all tasks (with pagination).
- `GET /todos/{id}`: Get details of a specific task.
- `PUT /todos/{id}`: Update an existing task (requires JWT token).
- `DELETE /todos/{id}`: Delete a task (requires JWT token).

## Getting Started

### Prerequisites
- Python 3.8+
- FastAPI
- Uvicorn (for running the server)
- SQLite (or any other database)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/todo-list-api.git
   cd todo-list-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`.

### Documentation

After running the server, you can explore the API documentation via the interactive Swagger UI at `http://127.0.0.1:8000/docs`.

---

https://roadmap.sh/projects/todo-list-api
