from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey
from app import Base

class OrderProductAssociationTable(Base):
    __tablename__ = "order_product_association"
    order_id: Mapped[int] = mapped_column(ForeignKey("order_table.id"),primary_key=True, nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("product_table.id"),primary_key=True, nullable=False)