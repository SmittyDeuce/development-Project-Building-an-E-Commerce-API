from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer, Float
from app import Base

class ProductTable(Base):
    __tablename__ = "product_table"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_name: Mapped[str] = mapped_column(String(300), nullable=False)
    price: Mapped[Float] = mapped_column(Float)