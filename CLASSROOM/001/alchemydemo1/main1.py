print("welcome to our first app")
from db.db_config import engine,Base
from model.employee import Employee
from model.student import Student
Base.metadata.create_all(engine)
print("Employee table created in database")













# welcome to our first app
# Engine created successfully
# session factor created
# employee model
# 2026-11-18 22:23:19,076 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2026-11-18 22:23:19,084 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-18 22:23:19,086 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2026-11-18 22:23:19,088 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-18 22:23:19,089 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2026-11-18 22:23:19,093 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-18 22:23:19,100 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-18 22:23:19,104 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`alchemyemployee`
# 2026-11-18 22:23:19,104 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-18 22:23:19,131 INFO sqlalchemy.engine.Engine DESCRIBE `batch18`.`alchemystudent`
# 2026-11-18 22:23:19,155 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-18 22:23:19,158 INFO sqlalchemy.engine.Engine 
# CREATE TABLE alchemyemployee (
#         id INTEGER NOT NULL AUTO_INCREMENT, 
#         name VARCHAR(100) NOT NULL, 
#         email VARCHAR(100) NOT NULL, 
#         age INTEGER NOT NULL, 
#         salary NUMERIC(10, 2) NOT NULL, 
#         is_active BOOL NOT NULL, 
#         description VARCHAR(200) NOT NULL, 
#         PRIMARY KEY (id), 
#         UNIQUE (email)
# )


# 2026-11-18 22:23:19,159 INFO sqlalchemy.engine.Engine [no key 0.00071s] {}
# 2026-11-18 22:23:19,321 INFO sqlalchemy.engine.Engine 
# CREATE TABLE alchemystudent (
#         id INTEGER NOT NULL AUTO_INCREMENT, 
#         name VARCHAR(100), 
#         PRIMARY KEY (id)
# )


# 2026-11-18 22:23:19,321 INFO sqlalchemy.engine.Engine [no key 0.00043s] {}
# 2026-11-18 22:23:19,354 INFO sqlalchemy.engine.Engine COMMIT
# Employee table created in database