# app/models/user.py

from sqlalchemy import Column, String, Integer, BigInteger, Boolean, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password_hash = Column(String(128), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=True)
    full_name = Column(String(100), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    user_type = Column(String(20), nullable=False, server_default='regular')

    # 关联关系：一个用户可以有多套房子
    houses = relationship("House", back_populates="owner")
    # 一个用户可以有多条使用记录
    usage_records = relationship("UsageRecord", back_populates="user")
    # 一个用户可以提交多条反馈
    feedbacks = relationship("UserFeedback", back_populates="user")
