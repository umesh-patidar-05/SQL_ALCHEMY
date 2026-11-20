from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from db.db_config import Base
class Employee(Base):
    __tablename__ = "employee10"
    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    name:Mapped[str] = mapped_column(String(100), nullable = False)
    email:Mapped[str] = mapped_column(String(100), unique = True, nullable = False)
    salary:Mapped[int] = mapped_column(Integer)
    dept_id: Mapped[int] = mapped_column(Integer,ForeignKey("department10.dept_id"))
    department:Mapped["Department"] = relationship("Department", back_populates = "employees") 