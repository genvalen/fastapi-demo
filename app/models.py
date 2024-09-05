from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base

class Credentials(Base):
    __tablename__ = "credentials"  # the name of the table in the database

    # CREATE COLUMNS
    id = Column(Integer, primary_key=True, nullable=False)
    password = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
