from fastapi import APIRouter,HTTPException
from models.emp import Employee
from pymongo import MongoClient

#create employee router
router=APIRouter(prefix='/emp')

#establish the db connection
client=MongoClient('mongodb://localhost:27017/')
db=client['dbtwo']
emp_col=db['employees']



'''
usage:Create new Employee
Rest API URL: http://127.0.0.1:8000/emp/create
Method Type:POST
Request Fields:eid,ename,esal,gender 
Access Type:Public
'''

@router.post("/create")
def create_emp(emp:Employee):
    emp_col.insert_one(emp.dict())
    return {'msg':'New Employee Created succesfully'}

'''
usage:fetch all employees
Rest API URL: http://127.0.0.1:8000/emp/read
Method Type:GET
Request Fields:None
Access Type:Public
'''
@router.get("/read")
def get_employees():
    employees=list(emp_col.find({},{'_id':0}))
    return employees


'''
usage:read employee by id
Rest API URL: http://127.0.0.1:8000/emp/read/101
Method Type:GET
Request Fields:None
Access Type:Public
'''
@router.get("/read/{eid}")
def get_employee(eid:int):
    employee = emp_col.find_one({'eid':eid},{'_id':0})

    if not employee:
        return HTTPException(status_code=404,detail="Employee Not found")
    return employee 



'''
usage:update employee by id
Rest API URL: http://127.0.0.1:8000/emp/update/101
Method Type:PUT
Request Fields:eid,ename,esal,gender
Access Type:Public
'''

@router.put("/update/{eid}")
def update_emp(eid:int,emp:Employee):
    #verify employee exists or not using eid
    employee=emp_col.find_one({'eid':eid}) 

    if not employee:
        return HTTPException(status_code=404,detail="Employee Not Exits")

    emp_col.update_one({'eid':eid},{'$set':emp.dict()})
    return {'msg':"Employee Updated Successfully"}


'''
usage:delete employee by id
Rest API URL: http://127.0.0.1:8000/emp/delete/101
Method Type:DELETE
Request Fields:None
Access Type:Public
'''

@router.delete('/delete/{eid}')
def delete_employee(eid:int):
    #verify emploeye exists or not 
    employee=emp_col.find_one({'eid':eid})

    if not employee:
        return HTTPException(status_code=404,detail="Employee Not Exits")
    emp_col.delete_one({'eid':eid})
    return {'msg':'Employee Deleted successfully'}