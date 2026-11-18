from db.db_config import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Numeric, Float, Boolean
class Student(Base):
    __tablename__ = "alchemystudent"
    id = mapped_column(Integer,primary_key = True)
    name = mapped_column(String(100))