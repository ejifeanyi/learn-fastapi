from fastapi import APIRouter, HTTPException
from app.schemas import TodoCreate, Todo

router = APIRouter()


todos = [
    Todo(id=1, title="Buy groceries", description="Milk, Eggs, Bread", completed=False),
    Todo(
        id=2, title="Learn FastAPI", description="Build a small project", completed=True
    ),
]


@router.get("/todos", response_model=list[Todo])
def get_todos():
    # return all todos
    return todos


@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    # loop through the todos list
    # if the todo id matches the todo_id passed in
    # return the todo

    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}


@router.post("/todo", response_model=Todo)
def add_todo(todo: TodoCreate):
    # create a new todo
    # add the todo to the list
    # return

    new_id = len(todos) + 1
    new_todo = Todo(id=new_id, **todo.dict())
    todos.append(new_todo)
    return new_todo


@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_data: TodoCreate):
    # loop through the todos list
    # if the todo id matches the todo_id passed in
    # update the todo with the new data
    # return the updated todo

    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            updated_todo = Todo(
                id=todo_id,
                title=todo_data.title,
                description=todo_data.description,
                completed=todo_data.completed,
            )
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")


@router.delete("/todos/{todo_id}", response_model=list[Todo])
def delete_todo(todo_id: int, todo_data: TodoCreate):
    # loop through the todos list
    # if the todo id matches the todo_id passed in
    # remove the todo from the list

    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return todos
    raise HTTPException(status_code=404, detail="Todo not found")
