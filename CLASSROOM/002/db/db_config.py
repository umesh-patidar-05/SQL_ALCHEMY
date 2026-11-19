from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
url = "mysql+pymysql://root:%40umesh2005@localhost:3306/batch18"

engine = create_engine(url, echo = False)
print("Engine created successfully")
sessionlocal = sessionmaker(bind = engine)
print("session factor created")
class Base(DeclarativeBase):
    pass