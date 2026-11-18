from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
url = "mysql+pymysql://pythonuser:Python%401234@localhost:3306/batch18"

engine = create_engine(url, echo = True)
print("Engine created successfully")
sessionlocal = sessionmaker(bind = engine)
print("session factor created")
class Base(DeclarativeBase):
    pass