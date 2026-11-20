from sqlalchemy import select

from db.db_config import engine, Base, sessionlocal
from model.employee2 import Employee2
from model.empcard2 import EmpCard2


Base.metadata.create_all(engine)
print("agar sab shi rha to dono table ban jaegiii")




# Engine created successfully
# session factor created
# 2026-11-21 00:21:57,717 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2026-11-21 00:21:57,731 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:21:57,734 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2026-11-21 00:21:57,735 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:21:57,736 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2026-11-21 00:21:57,737 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:21:57,742 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-21 00:21:57,761 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`employee2`
# 2026-11-21 00:21:57,764 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:21:57,779 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`empcard2`
# 2026-11-21 00:21:57,786 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:21:57,792 INFO sqlalchemy.engine.Engine 
# CREATE TABLE employee2 (
#         id INTEGER NOT NULL AUTO_INCREMENT, 
#         name VARCHAR(100) NOT NULL, 
#         email VARCHAR(100) NOT NULL, 
#         salary INTEGER NOT NULL, 
#         PRIMARY KEY (id), 
#         UNIQUE (email)
# )


# 2026-11-21 00:21:57,796 INFO sqlalchemy.engine.Engine [no key 0.00423s] {}
# 2026-11-21 00:21:58,038 INFO sqlalchemy.engine.Engine 
# CREATE TABLE empcard2 (
#         card_id INTEGER NOT NULL AUTO_INCREMENT, 
#         card_number VARCHAR(50) NOT NULL, 
#         employee_id INTEGER NOT NULL, 
#         PRIMARY KEY (card_id), 
#         UNIQUE (card_number), 
#         UNIQUE (employee_id), 
#         FOREIGN KEY(employee_id) REFERENCES employee2 (id)
# )


# 2026-11-21 00:21:58,049 INFO sqlalchemy.engine.Engine [no key 0.01132s] {}
# 2026-11-21 00:21:58,120 INFO sqlalchemy.engine.Engine COMMIT
# agar sab shi rha to dono table ban jaegiii










# CREATE EMPLOYEE
def createemployee2():
    session = sessionlocal()

    emp = Employee2(
        name="deepika",
        email="dipu2@gmail.com",
        salary=9000
    )

    session.add(emp)
    session.commit()

    print("Employee2 will be added")
    print("Employee2 ID:", emp.id)

    session.close()


# Engine created successfully
# session factor created
# 2026-11-21 00:23:25,882 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2026-11-21 00:23:25,882 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:23:25,884 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2026-11-21 00:23:25,884 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:23:25,885 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2026-11-21 00:23:25,885 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:23:25,887 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-21 00:23:25,887 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`employee2`
# 2026-11-21 00:23:25,891 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:23:25,896 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`empcard2`
# 2026-11-21 00:23:25,906 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:23:25,914 INFO sqlalchemy.engine.Engine COMMIT
# agar sab shi rha to dono table ban jaegiii
# 2026-11-21 00:23:25,927 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-21 00:23:25,933 INFO sqlalchemy.engine.Engine INSERT INTO employee2 (name, email, salary) VALUES (%(name)s, %(email)s, %(salary)s)
# 2026-11-21 00:23:25,933 INFO sqlalchemy.engine.Engine [generated in 0.00034s] {'name': 'deepika', 'email': 'dipu2@gmail.com', 'salary': 9000}
# 2026-11-21 00:23:25,942 INFO sqlalchemy.engine.Engine COMMIT
# Employee2 will be added
# 2026-11-21 00:23:25,951 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-21 00:23:25,954 INFO sqlalchemy.engine.Engine SELECT employee2.id, employee2.name, employee2.email, employee2.salary 
# FROM employee2 
# WHERE employee2.id = %(pk_1)s
# 2026-11-21 00:23:25,958 INFO sqlalchemy.engine.Engine [generated in 0.00380s] {'pk_1': 1}
# Employee2 ID: 1
# 2026-11-21 00:23:25,965 INFO sqlalchemy.engine.Engine ROLLBACK












# CREATE EMP CARD FOR EMPLOYEE
def createempcard2():
    session = sessionlocal()

    emp = session.get(Employee2, 1)

    if emp is not None:
        card = EmpCard2(card_number="CARD-1001")

        # Relationship way:
        emp.card = card

        session.commit()

        print("EmpCard2 will be added")
        print("Employee ID:", card.employee_id)

    else:
        print("Employee2 not found")

    session.close()



# Engine created successfully
# session factor created
# 2026-11-21 00:24:40,119 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2026-11-21 00:24:40,119 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:24:40,121 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2026-11-21 00:24:40,121 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:24:40,123 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2026-11-21 00:24:40,124 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:24:40,125 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-21 00:24:40,125 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`employee2`
# 2026-11-21 00:24:40,125 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:24:40,131 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`empcard2`
# 2026-11-21 00:24:40,137 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:24:40,142 INFO sqlalchemy.engine.Engine COMMIT
# agar sab shi rha to dono table ban jaegiii
# 2026-11-21 00:24:40,151 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-21 00:24:40,162 INFO sqlalchemy.engine.Engine SELECT employee2.id, employee2.name, employee2.email, employee2.salary 
# FROM employee2 
# WHERE employee2.id = %(pk_1)s
# 2026-11-21 00:24:40,164 INFO sqlalchemy.engine.Engine [generated in 0.00185s] {'pk_1': 1}
# 2026-11-21 00:24:40,170 INFO sqlalchemy.engine.Engine SELECT empcard2.card_id, empcard2.card_number, empcard2.employee_id 
# FROM empcard2 
# WHERE %(param_1)s = empcard2.employee_id
# 2026-11-21 00:24:40,170 INFO sqlalchemy.engine.Engine [generated in 0.00029s] {'param_1': 1}
# 2026-11-21 00:24:40,177 INFO sqlalchemy.engine.Engine INSERT INTO empcard2 (card_number, employee_id) VALUES (%(card_number)s, %(employee_id)s)
# 2026-11-21 00:24:40,177 INFO sqlalchemy.engine.Engine [generated in 0.00033s] {'card_number': 'CARD-1001', 'employee_id': 1}
# 2026-11-21 00:24:40,182 INFO sqlalchemy.engine.Engine COMMIT
# EmpCard2 will be added
# 2026-11-21 00:24:40,189 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-21 00:24:40,192 INFO sqlalchemy.engine.Engine SELECT empcard2.card_id, empcard2.card_number, empcard2.employee_id 
# FROM empcard2 
# WHERE empcard2.card_id = %(pk_1)s
# 2026-11-21 00:24:40,192 INFO sqlalchemy.engine.Engine [generated in 0.00052s] {'pk_1': 1}
# Employee ID: 1
# 2026-11-21 00:24:40,194 INFO sqlalchemy.engine.Engine ROLLBACK












# GET EMPLOYEE WITH CARD

def getemployee2():
    session = sessionlocal()

    stmt = select(Employee2)
    employees = session.scalars(stmt).all()

    for emp in employees:
        print("ID", emp.id)
        print("Name", emp.name)
        print("Email", emp.email)
        print("Salary", emp.salary)

        if emp.card is not None:
            print("Card ID", emp.card.card_id)
            print("Card Number", emp.card.card_number)
            print("Card Employee ID", emp.card.employee_id)
        else:
            print("Card not assigned")

    session.close()




# session factor created
# 2026-11-21 00:25:50,894 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2026-11-21 00:25:50,916 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:25:50,919 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2026-11-21 00:25:50,919 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:25:50,921 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2026-11-21 00:25:50,924 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:25:50,927 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-21 00:25:50,928 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`employee2`
# 2026-11-21 00:25:50,928 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:25:50,933 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`empcard2`
# 2026-11-21 00:25:50,933 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:25:50,936 INFO sqlalchemy.engine.Engine COMMIT
# agar sab shi rha to dono table ban jaegiii
# 2026-11-21 00:25:50,946 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-21 00:25:50,962 INFO sqlalchemy.engine.Engine SELECT employee2.id, employee2.name, employee2.email, employee2.salary 
# FROM employee2
# 2026-11-21 00:25:50,964 INFO sqlalchemy.engine.Engine [generated in 0.00132s] {}
# ID 1
# Name deepika
# Email dipu2@gmail.com
# Salary 9000
# 2026-11-21 00:25:50,985 INFO sqlalchemy.engine.Engine SELECT empcard2.card_id, empcard2.card_number, empcard2.employee_id 
# FROM empcard2 
# WHERE %(param_1)s = empcard2.employee_id
# 2026-11-21 00:25:50,986 INFO sqlalchemy.engine.Engine [generated in 0.00037s] {'param_1': 1}
# Card ID 1
# Card Number CARD-1001
# Card Employee ID 1
# 2026-11-21 00:25:50,997 INFO sqlalchemy.engine.Engine ROLLBACK    







# GET CARD AND ITS EMPLOYEE

def getempcard2():
    session = sessionlocal()

    stmt = select(EmpCard2)
    cards = session.scalars(stmt).all()

    for card in cards:
        print("Card ID", card.card_id)
        print("Card Number", card.card_number)
        print("Employee ID", card.employee.id)
        print("Employee Name", card.employee.name)

    session.close()



# Engine created successfully
# session factor created
# 2026-11-21 00:27:02,161 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2026-11-21 00:27:02,161 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:27:02,163 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2026-11-21 00:27:02,163 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:27:02,164 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2026-11-21 00:27:02,164 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:27:02,166 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-21 00:27:02,166 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`employee2`
# 2026-11-21 00:27:02,166 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:27:02,171 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`empcard2`
# 2026-11-21 00:27:02,171 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-21 00:27:02,174 INFO sqlalchemy.engine.Engine COMMIT
# agar sab shi rha to dono table ban jaegiii
# 2026-11-21 00:27:02,178 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-21 00:27:02,190 INFO sqlalchemy.engine.Engine SELECT empcard2.card_id, empcard2.card_number, empcard2.employee_id 
# FROM empcard2
# 2026-11-21 00:27:02,190 INFO sqlalchemy.engine.Engine [generated in 0.00046s] {}
# Card ID 1
# Card Number CARD-1001
# 2026-11-21 00:27:02,197 INFO sqlalchemy.engine.Engine SELECT employee2.id, employee2.name, employee2.email, employee2.salary 
# FROM employee2 
# WHERE employee2.id = %(pk_1)s
# 2026-11-21 00:27:02,198 INFO sqlalchemy.engine.Engine [generated in 0.00116s] {'pk_1': 1}
# Employee ID 1
# Employee Name deepika
# 2026-11-21 00:27:02,202 INFO sqlalchemy.engine.Engine ROLLBACK    










# createemployee2()
# createempcard2()
# getemployee2()
# getempcard2()