from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, VARCHAR
from sqlalchemy.orm import relationship
import database
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(VARCHAR(20))
    email = Column(VARCHAR(20), unique=True, index=True)
    full_name = Column(VARCHAR(20))
    hashed_password = Column(VARCHAR(200))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(20), index=True)
    description = Column(VARCHAR(20), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
