from utils.db import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from utils.constants import Tables, Columns
from sqlalchemy.sql import func


class Admin(Base):
    __tablename__ = Tables.ADMIN

    admin_id = Column(Columns.ADMIN_ID, Integer, primary_key=True, index=True)
    email = Column(Columns.EMAIL, String, unique=True, index=True, nullable=False)
    name = Column(Columns.NAME, String, nullable=False)
    hashed_password = Column(Columns.HASHED_PASSWORD, String, nullable=False)
    created_at = Column(Columns.CREATED_AT, TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(Columns.UPDATED_AT, TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    deleted_at = Column(Columns.DELETED_AT, TIMESTAMP(timezone=True), nullable=True, server_default=None)
    note = Column(Columns.NOTE, String, nullable=True)


# Base.metadata.create_all(bind=Engine)
