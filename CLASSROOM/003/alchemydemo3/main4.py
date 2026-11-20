from db.db_config import engine, Base, sessionlocal
from model.employee import Employee
from model.department import Department
Base.metadata.create_all(engine)
print("agar sab shi rha to dono table ban jaegiii")



# Engine created successfully
# session factor created
# 2026-11-20 20:05:10,820 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2026-11-20 20:05:10,822 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:05:10,826 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2026-11-20 20:05:10,827 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:05:10,829 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2026-11-20 20:05:10,833 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:05:10,836 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-20 20:05:10,837 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`employee10`
# 2026-11-20 20:05:10,837 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:05:10,843 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`department10`
# 2026-11-20 20:05:10,847 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:05:10,850 INFO sqlalchemy.engine.Engine 
# CREATE TABLE department10 (
#         dept_id INTEGER NOT NULL AUTO_INCREMENT, 
#         dept_name VARCHAR(100) NOT NULL, 
#         PRIMARY KEY (dept_id)
# )


# 2026-11-20 20:05:10,851 INFO sqlalchemy.engine.Engine [no key 0.00087s] {}
# 2026-11-20 20:05:10,960 INFO sqlalchemy.engine.Engine 
# CREATE TABLE employee10 (
#         id INTEGER NOT NULL AUTO_INCREMENT, 
#         name VARCHAR(100) NOT NULL, 
#         email VARCHAR(100) NOT NULL, 
#         salary INTEGER NOT NULL, 
#         dept_id INTEGER NOT NULL, 
#         PRIMARY KEY (id), 
#         UNIQUE (email), 
#         FOREIGN KEY(dept_id) REFERENCES department10 (dept_id)
# )


# 2026-11-20 20:05:10,962 INFO sqlalchemy.engine.Engine [no key 0.00142s] {}
# 2026-11-20 20:05:11,032 INFO sqlalchemy.engine.Engine COMMIT
# agar sab shi rha to dono table ban jaegiii












from db.db_config import engine, Base, sessionlocal
from model.employee import Employee
from model.department import Department
def cetedepartment():
    session = sessionlocal()
    dept = Department(dept_name = "IT")
    session.add(dept)
    session.commit()
    print("department will be added")
    session.close()
cetedepartment()    



# Engine created successfully
# session factor created
# 2026-11-20 20:08:05,351 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2026-11-20 20:08:05,351 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:08:05,353 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2026-11-20 20:08:05,353 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:08:05,354 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2026-11-20 20:08:05,354 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:08:05,355 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-20 20:08:05,357 INFO sqlalchemy.engine.Engine INSERT INTO department10 (dept_name) VALUES (%(dept_name)s)
# 2026-11-20 20:08:05,357 INFO sqlalchemy.engine.Engine [generated in 0.00025s] {'dept_name': 'IT'}
# 2026-11-20 20:08:05,365 INFO sqlalchemy.engine.Engine COMMIT
# department will be added















from db.db_config import engine, Base, sessionlocal
from model.employee import Employee
from model.department import Department
def createemployee():
    session = sessionlocal()
    emp = Employee(name = "deepika", email = "dipu@gmail.com", salary = 9000)
    dept = session.get(Department,1)
    dept.employees.append(emp)
    session.commit()
    print("agar sab shi rha.... employee will created")
    session.close()
createemployee()   



# Engine created successfully
# session factor created
# 2026-11-20 20:09:33,828 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2026-11-20 20:09:33,828 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:09:33,831 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2026-11-20 20:09:33,831 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:09:33,832 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2026-11-20 20:09:33,832 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:09:33,834 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-20 20:09:33,837 INFO sqlalchemy.engine.Engine SELECT department10.dept_id, department10.dept_name 
# FROM department10 
# WHERE department10.dept_id = %(pk_1)s
# 2026-11-20 20:09:33,838 INFO sqlalchemy.engine.Engine [generated in 0.00033s] {'pk_1': 1}
# 2026-11-20 20:09:33,845 INFO sqlalchemy.engine.Engine SELECT employee10.id, employee10.name, employee10.email, employee10.salary, employee10.dept_id 
# FROM employee10 
# WHERE %(param_1)s = employee10.dept_id
# 2026-11-20 20:09:33,850 INFO sqlalchemy.engine.Engine [generated in 0.00532s] {'param_1': 1}
# 2026-11-20 20:09:33,860 INFO sqlalchemy.engine.Engine INSERT INTO employee10 (name, email, salary, dept_id) VALUES (%(name)s, %(email)s, %(salary)s, %(dept_id)s)
# 2026-11-20 20:09:33,862 INFO sqlalchemy.engine.Engine [generated in 0.00194s] {'name': 'deepika', 'email': 'dipu@gmail.com', 'salary': 9000, 'dept_id': 1}
# 2026-11-20 20:09:33,870 INFO sqlalchemy.engine.Engine COMMIT
# agar sab shi rha.... employee will created











from sqlalchemy import select
from db.db_config import engine, Base, sessionlocal
from model.employee import Employee
from model.department import Department
def getAllemployees():
    session = sessionlocal()
    stmt = select(Employee)
    result = session.execute(stmt)
    employees = result.scalars().all()
    for emp in employees:
        print("ID", emp.id)
        print("Name", emp.name)
        print("Email", emp.email)
        print("DID", emp.dept_id)
        print("Dname", emp.department.dept_name)
    session.close()
getAllemployees()       

# KAL WALA LAYERED
#HW ONE TO ONE RELATION SHIP USER PROFILE

# Engine created successfully
# session factor created
# 2026-11-20 20:11:49,413 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2026-11-20 20:11:49,414 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:11:49,415 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2026-11-20 20:11:49,415 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:11:49,416 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2026-11-20 20:11:49,417 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-20 20:11:49,418 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-20 20:11:49,430 INFO sqlalchemy.engine.Engine SELECT employee10.id, employee10.name, employee10.email, employee10.salary, employee10.dept_id 
# FROM employee10
# 2026-11-20 20:11:49,443 INFO sqlalchemy.engine.Engine [generated in 0.01302s] {}
# ID 1
# Name deepika
# Email dipu@gmail.com
# DID 1
# 2026-11-20 20:11:49,455 INFO sqlalchemy.engine.Engine SELECT department10.dept_id, department10.dept_name 
# FROM department10 
# WHERE department10.dept_id = %(pk_1)s
# 2026-11-20 20:11:49,456 INFO sqlalchemy.engine.Engine [generated in 0.00145s] {'pk_1': 1}
# Dname IT
# 2026-11-20 20:11:49,463 INFO sqlalchemy.engine.Engine ROLLBACK