from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.db_config import Base


class EmpCard2(Base):
    __tablename__ = "empcard2"

    card_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    card_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    employee_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("employee2.id"),
        unique=True,
        nullable=False
    )

    employee: Mapped["Employee2"] = relationship("Employee2",back_populates="card")
