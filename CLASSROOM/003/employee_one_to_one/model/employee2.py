from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.db_config import Base


class Employee2(Base):
    __tablename__ = "employee2"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    salary: Mapped[int] = mapped_column(Integer)

    # One Employee2 -> One EmpCard2
    card: Mapped["EmpCard2"] = relationship("EmpCard2",back_populates="employee",uselist=False)
