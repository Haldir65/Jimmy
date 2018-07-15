from models import Student

def serialize_student(student):
    return {"id":student.id,"name":student.studentname,"email":student.email}