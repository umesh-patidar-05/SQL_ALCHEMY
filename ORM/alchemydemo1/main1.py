print("welcome to our first app")
from db.db_config import engine,Base
from model.employee import Employee
from model.student import Student
Base.metadata.create_all(engine)
print("Employee table created in database")