from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Data model  --> CRUD OPERATIONS
class Student(BaseModel):
    name: str
    marks: int

# Temporary database
students = []

# Home API
@app.get("/")
def home():
    return {"message": "Student CRUD API"}

# CREATE student
@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {"message": "Student added", "student": student}

# READ all students
@app.get("/students")
def get_students():
    return students

# READ single student
@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")

    return students[student_id]

# UPDATE student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    if student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")

    students[student_id] = student

    return {"message": "Student updated", "student": student}

# DELETE student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")

    deleted_student = students.pop(student_id)

    return {"message": "Student deleted", "student": deleted_student}