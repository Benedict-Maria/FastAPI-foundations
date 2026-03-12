from database import engine, SessionLocal
from models import Student
from database import Base

Base.metadata.create_all(bind=engine)

session = SessionLocal()


student1 = Student(name="Rahul", age=21, course="Python")
student2 = Student(name="Anu", age=22, course="Java")
session.add(student1)
session.add(student2)
session.commit()
print("Students inserted")


print("\nAll Students:")
students = session.query(Student).all()
for student in students:
    print(student.id, student.name, student.age, student.course)


print("\nFilter Student (name = Rahul):")
student = session.query(Student).filter(Student.name == "Rahul").first()
if student:
    print(student.id, student.name, student.age, student.course)


print("\nUpdating Rahul's course...")
student = session.query(Student).filter(Student.name == "Rahul").first()
if student:
    student.course = "FastAPI"
    session.commit()
print("Student updated")


print("\nDeleting student Anu...")
student = session.query(Student).filter(Student.name == "Anu").first()
if student:
    session.delete(student)
    session.commit()
print("Student deleted")


print("\nFinal Students List:")
students = session.query(Student).all()
for student in students:
    print(student.id, student.name, student.age, student.course)
session.close()