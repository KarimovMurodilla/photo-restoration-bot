from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, DateTime

from utils.db_api.base import Base
from datetime import datetime


# Модель (таблица) для юзеров
class Users(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String(20))
    first_name = Column(String(50))
    date = Column(DateTime, default=datetime.utcnow)