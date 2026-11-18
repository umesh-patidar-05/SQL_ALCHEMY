# import sqlalchemy
# import pymysql
# print(sqlalchemy.__version__)
# print(pymysql.__version__)




from sqlalchemy import text
from database import engine
connection = engine.connect()
print("database connected successfully")
result = connection.execute(text("select database()"))
result = connection.execute(text("select version()"))
result = connection.execute(text("select current_date()"))
print(result.fetchone())
connection.close()