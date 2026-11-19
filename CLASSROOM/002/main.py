# TABLE CREATION

from db.db_config import engine, Base
from model.employee import Employee
from db.db_config import sessionlocal

Base.metadata.create_all(engine)
print("table will be created agar sab kuch sahi raha")



# Engine created successfully
# session factor created
# table will be created agar sab kuch sahi raha









# INSERT DATA INTO TABLE

from model.employee import Employee
from db.db_config import sessionlocal
emp = Employee(name = "rashmika", email = "rashmi@gmail.com", salary= 600000)
session = sessionlocal()
session.add(emp)
session.commit()
print('Employee will be inserted')



# Engine created successfully
# session factor created
# Employee will be inserted










# INSERT MULTIPLE DATA INTO TABLE

from model.employee import Employee
from db.db_config import sessionlocal

emp1 = Employee(
    name="Deepika",
    email="deepu@gmail.com",
    salary=900000
)

emp2 = Employee(
    name="Rahul",
    email="rahul@gmail.com",
    salary=500000
)

emp3 = Employee(
    name="Amit",
    email="amit@gmail.com",
    salary=450000
)

session = sessionlocal()

session.add_all([emp1, emp2, emp3])
session.commit()
print('ALL Employees will be inserted')



# Engine created successfully
# session factor created
# ALL Employees will be inserted





 





from model.employee import Employee
from db.db_config import sessionlocal
session = sessionlocal()
employees = session.query(Employee).all()
for emp in employees:
    print(emp.id, emp.name, emp.salary)
session.close()
print("all employees are printed")    



# Engine created successfully
# session factor created
# 1 rashmika 600000.00
# 3 Deepika 900000.00
# 4 Rahul 500000.00
# 5 Amit 450000.00
# all employees are printed










from model.employee import Employee
from db.db_config import sessionlocal
session = sessionlocal()
employee = session.query(Employee).filter(Employee.id == 1).first()
if employee:
    print(employee.id, employee.name, employee.salary)
else:
    print("Employee not found")    
session.close()
print("employee are printed")  



# Engine created successfully
# session factor created
# 1 rashmika 600000.00
# employee are printed









from model.employee import Employee
from db.db_config import sessionlocal
session = sessionlocal()
employee = session.query(Employee).filter(Employee.email == "deepu@gmail.com").first()
if employee:
    print(employee.id, employee.name, employee.salary)
else:
    print("Employee not found")    
session.close()
print("employee are printed")  



# Engine created successfully
# session factor created
# 3 Deepika 900000.00
# employee are printed










# write a program to update salary of deepika padukone to 100000


from model.employee import Employee
from db.db_config import sessionlocal
session = sessionlocal()
employee = session.query(Employee).filter(Employee.id == 3).first()
if employee:
    employee.salary = 100000
    session.commit()
    print("employee salary updated successfully")
else:
    print("no employee with given id")



# Engine created successfully
# session factor created
# employee salary updated successfully











from model.employee import Employee
from db.db_config import sessionlocal
from sqlalchemy import select

session = sessionlocal()
stmt = select(Employee)
employees  = session.scalars(stmt).all()
for emp in employees:
    print(emp.id, emp.name, emp.salary)
print("Employees........")    



# Engine created successfully
# session factor created
# 1 rashmika 600000.00
# 3 Deepika 100000.00
# 4 Rahul 500000.00
# 5 Amit 450000.00
# Employees........










from model.employee import Employee
from db.db_config import sessionlocal
from sqlalchemy import select
session = sessionlocal()
stmt = select(Employee).where(Employee.id ==1)
employee = session.scalars(stmt).first()
if employee:
    print(employee.id, employee.name, employee.salary)
    print("Employee........founded")
else:
    print("Employee not found")    



# Engine created successfully
# session factor created
# 1 rashmika 600000.00
# Employee........founded    










# write a program to find employees whose salary > 80000 and id is > 1

from model.employee import Employee
from db.db_config import sessionlocal
from sqlalchemy import select
session = sessionlocal()
stmt = select(Employee).where(Employee.id >1 , Employee.salary > 80000)
employees  = session.scalars(stmt).all()
for emp in employees:
    print(emp.id, emp.name, emp.salary)
print("Employees........")  



# Engine created successfully
# session factor created
# 3 Deepika 100000.00
# 4 Rahul 500000.00
# 5 Amit 450000.00
# Employees........









from model.employee import Employee
from db.db_config import sessionlocal
from sqlalchemy import select
session = sessionlocal()
stmt = select(Employee).where(Employee.id ==1)
employee  = session.scalars(stmt).first()
employee.salary = 1900000
session.commit()
print("byyy")



# Engine created successfully
# session factor created
# byyy










# FIND EMPLOYEES WHOSE NAME STARTS WITH "A"

from model.employee import Employee
from db.db_config import sessionlocal
from sqlalchemy import select
session = sessionlocal()
stmt = select(Employee).where(Employee.name.like("A%"))
employees = session.scalars(stmt).all()
for emp in employees:
    print(emp.id, emp.name, emp.salary)
session.close()
print("Employees........")


# Engine created successfully
# session factor created
# 5 Amit 450000.00
# Employees........










# FIND EMPLOYEES WHOSE NAME CONTAINS "it"

from model.employee import Employee
from db.db_config import sessionlocal
from sqlalchemy import select
session = sessionlocal()
stmt = select(Employee).where(Employee.name.like("%it%"))
employees = session.scalars(stmt).all()
for emp in employees:
    print(emp.id, emp.name, emp.salary)
session.close()
print("Employees........")

# Engine created successfully
# session factor created
# 5 Amit 450000.00
# Employees........









# GROUP EMPLOYEES BY SALARY

from model.employee import Employee
from db.db_config import sessionlocal
from sqlalchemy import select, func
session = sessionlocal()
stmt = select(
    Employee.salary,
    func.count(Employee.id)
).group_by(Employee.salary)
results = session.execute(stmt).all()
for salary, count in results:
    print(salary, count)
session.close()
print("Salary groups........")



# Engine created successfully
# session factor created
# 1900000.00 1
# 100000.00 1
# 500000.00 1
# 450000.00 1
# Salary groups........










# FIND SALARY GROUPS HAVING MORE THAN 1 EMPLOYEE

from model.employee import Employee
from db.db_config import sessionlocal
from sqlalchemy import select, func
session = sessionlocal()
stmt = select(
    Employee.salary,
    func.count(Employee.id)
).group_by(
    Employee.salary
).having(
    func.count(Employee.id) > 1
)
results = session.execute(stmt).all()
for salary, count in results:
    print(salary, count)
session.close()
print("Salary groups........")



# Engine created successfully
# session factor created
# Salary groups........
