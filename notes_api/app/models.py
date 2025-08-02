from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
Base= declarative_base()
class Note(Base):
    __tablename__="notes"
    id= Column(Integer, primary_key=True, index=True)
    title= Column(String, index=True)
    content=Column(String, index=True) 
    category= Column(String, index=True)
    tags= Column(String, index=True)
    is_favorite= Column(Boolean, default=False)
    is_archived= Column(Boolean, default=False)
    created_at= Column(DateTime(timezone=True), server_default=func.now())
    updated_at= Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    color= Column(String(7),default="#FFFFFF") 