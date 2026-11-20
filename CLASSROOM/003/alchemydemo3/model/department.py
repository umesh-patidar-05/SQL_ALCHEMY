from sqlalchemy import String, Integer
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from db.db_config import Base
class Department(Base):
    __tablename__ = "department10"
    dept_id:Mapped[int] = mapped_column(Integer, primary_key= True)  #by default autoincrement hota hai
    dept_name:Mapped[str] = mapped_column(String(100), nullable = False)
    employees:Mapped[list["Employee"]]=relationship("Employee", back_populates = "department")
 