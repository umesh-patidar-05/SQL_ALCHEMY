import sqlalchemy
import pymysql
print(sqlalchemy.__version__)   # 2.1.9
print(pymysql.__version__)      # 2.2.8





from sqlalchemy import text
from database import engine
connection = engine.connect()
print("database connected successfully")
result1 = connection.execute(text("select database()"))
result2 = connection.execute(text("select version()"))
result3 = connection.execute(text("select current_date()"))
print(result1.fetchone())
print(result2.fetchone())
print(result3.fetchone())
connection.close()


# SQL alchemy engine created successfully
# session factor created
# 2026-11-18 21:51:31,728 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2026-11-18 21:51:31,729 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-18 21:51:31,730 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2026-11-18 21:51:31,730 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2026-11-18 21:51:31,731 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2026-11-18 21:51:31,731 INFO sqlalchemy.engine.Engine [raw sql] {}
# database connected successfully
# 2026-11-18 21:51:31,736 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-11-18 21:51:31,736 INFO sqlalchemy.engine.Engine select database()
# 2026-11-18 21:51:31,737 INFO sqlalchemy.engine.Engine [generated in 0.00130s] {}
# 2026-11-18 21:51:31,739 INFO sqlalchemy.engine.Engine select version()
# 2026-11-18 21:51:31,740 INFO sqlalchemy.engine.Engine [generated in 0.00078s] {}
# 2026-11-18 21:51:31,743 INFO sqlalchemy.engine.Engine select current_date()
# 2026-11-18 21:51:31,743 INFO sqlalchemy.engine.Engine [generated in 0.00035s] {}
# ('batch18',)
# ('8.0.46',)
# (datetime.date(2026, 11, 18),)
# 2026-11-18 21:51:31,745 INFO sqlalchemy.engine.Engine ROLLBACK