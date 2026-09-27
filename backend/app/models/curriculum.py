from sqlalchemy import Column , Integer , String , Text , ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Curriculum(Base):
    __tablename__ = "curricula"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    description = Column(Text, nullable=True)

    nodes = relationship("Node",back_populates="curriculum",cascade="all, delete-orphan")

class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True, index=True)
    curriculum_id = Column(Integer, ForeignKey("curricula.id"),nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    curriculum = relationship("Curriculum",back_populates="nodes")

