from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Employee(BaseModel):
    Employee_id : int
    Employee_name : str
    Designation : str
    login_time : datetime
    logout_time : datetime

# GET request
@app.get("/")   
def read_root():
    return {"message": " Welcome to REST API "}

# POST req
@app.post("/employee/")
def create_employee(emp: Employee):
    emp.login_time = datetime.utcnow()
    return emp
