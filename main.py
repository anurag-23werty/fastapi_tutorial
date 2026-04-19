from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "sam"}
@app.get("/greet")
def greet():
    return {"message": f"Hello, anurag!"}
@app.get("/greet/{name}")
def greet_name(name: str,age:int):
    return {"message": f"Hello, {name}!,my age is{age}"}
@app.post("/create_student")
class Student(BaseModel):
    name: str
    age: int
    grade: str
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "grade": student.grade
    }