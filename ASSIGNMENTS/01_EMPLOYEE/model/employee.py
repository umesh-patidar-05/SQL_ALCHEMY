from sqlalchemy import Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from db.db_config import Base
class Employee(Base):
    __tablename__ = "employeelayered" 
    id:Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    name:Mapped[str] = mapped_column(String(100), nullable = False)
    email:Mapped[str] = mapped_column(String(100), unique=True, nullable = False)
    salary:Mapped[float] = mapped_column(Numeric(10,2), nullable =  False, default = 10000)