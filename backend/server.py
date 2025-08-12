from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI()

class Employees(BaseModel):
    Employee_id : int
    Employee_name : str
    Designation : str
    login_time : datetime
    logout_time : datetime


class EmployeeUpdate(BaseModel):
    Employee_name: Optional[str] = None
    Designation: Optional[str] = None
    login_time: Optional[datetime] = None
    logout_time: Optional[datetime] = None

# # GET request
# @app.get("/")   
# def read_root():
#     return {"message": " Welcome to REST API "}

# # POST req
# @app.post("/employee/")
# def create_employee(emp: Employee):
#     emp.login_time = datetime.utcnow()
#     return emp


employee = {}


@app.get("/")
def read_root():
    return {"message": "Welcome to REST API"}

# CREATE
@app.post("/employee/")
def create_employee(emp: Employees):
    if emp.Employee_id in employee:
        raise HTTPException(status_code=400, detail="Employee already exists")
    employee[emp.Employee_id] = emp
    return {"message": "Employee created successfully", "employee": emp}

# READ
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    if emp_id not in employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee[emp_id]

# UPDATE (Replace All)
@app.put("/employee/{emp_id}")
def update_employee(emp_id: int, emp: Employees):
    if emp_id not in employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    employee[emp_id] = emp
    return {"message": "Employee updated successfully", "employee": emp}

# UPDATE (Partial - PATCH)
@app.patch("/employee/{emp_id}")
def patch_employee(emp_id: int, emp_update: EmployeeUpdate):
    if emp_id not in employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    stored_emp = employee[emp_id]
    update_data = emp_update.dict(exclude_unset=True)
    updated_emp = stored_emp.copy(update=update_data)
    employee[emp_id] = updated_emp
    return {"message": "Employee partially updated", "employee": updated_emp}

# DELETE
@app.delete("/employee/{emp_id}")
def delete_employee(emp_id: int):
    if emp_id not in employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    del employee[emp_id]
    return {"message": "Employee deleted successfully"}
