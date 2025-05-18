from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, Integer, DateTime, Column
from datetime import datetime, timezone
from app import Base

class OrderTable(Base):
    __tablename__ = "order_table"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_date= Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    