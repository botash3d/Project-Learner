from sqlalchemy import Column , Integer , String , Boolean , ForeignKey , UniqueConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__="users"

    id = Column(Integer,primary_key=True,index=True)

    progress = relationship("Progress",back_populates="user",cascade="all, delete-orphan")

class Progress(Base):
    __tablename__="progress"
    __table_args__= (UniqueConstraint("user_id","node_id",name="uq_user_node"),)

    id = Column(Integer , primary_key=True , index=True)
    user_id = Column(Integer , ForeignKey("users.id"),nullable=False)
    node_id = Column(Integer , ForeignKey("nodes.id"),nullable=False)
    completed = Column(Boolean , default=False , nullable=False)
    user = relationship("User",back_populates="progress")