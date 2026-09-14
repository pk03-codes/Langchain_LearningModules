from pydantic import BaseModel,EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = 'Nitish'
    age:Optional[int]=None
    email:EmailStr

new_student={"name":"John","age":'32',"email":"jsd@example.com"}

student=Student(**new_student) #unpack the dicitonary into keyword arguments using ** operator and pass it to the Student class constructor

student_dict=dict(student)
print(student_dict)
student_json=student.model_dump_json()
print(student_json)