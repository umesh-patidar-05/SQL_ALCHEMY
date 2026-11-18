from db.db_config import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Numeric, Float, Boolean
print("employee model")
class Employee(Base):
    __tablename__= "alchemyemployee"
    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    name:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(100), unique= True)
    age:Mapped[float] = mapped_column(Integer)
    salary:Mapped[bool] = mapped_column(Numeric(10,2))
    is_active:Mapped[bool] = mapped_column(Boolean, default = True)
    description:Mapped[str] = mapped_column(String(200))