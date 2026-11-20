from db.db_config import engine, Base, sessionlocal
from model.employee import Employee
from sqlalchemy import select

Base.metadata.create_all(engine)


class EmployeeDao:

    def get_employee_by_id(self, id):
        session = sessionlocal()
        stmt = select(Employee).where(Employee.id ==id)
        employee = session.scalars(stmt).first()
        if employee is not None:
            return employee
        else:
            return None



    def get_all_employees(self):
        print("dao getting employee data")
        session = sessionlocal()
        stmt = select(Employee)
        employees = session.scalars(stmt).all()
        return employees


    def save_employee(self, employee):
        print("dao saving employee data")
        session = sessionlocal()
        session.add(employee)
        session.commit()
        print('Employee will be inserted')


    def update_employee_salary_by_id(self, id, salary):
        session = sessionlocal()
        stmt = select(Employee).where(Employee.id ==id)
        employee = session.scalars(stmt).first()
        employee.salary = salary
        session.commit()
        print("Employee salary update successfully")


    def delete_employee_id(self, id):
        session = sessionlocal()
        stmt = select(Employee).where(Employee.id == id)
        employee = session.scalars(stmt).first()
        if employee is not None:
            session.delete(employee)
            session.commit()
            print("Employee delete sccessfully")
        else:
            print("No employee available with this id")    
