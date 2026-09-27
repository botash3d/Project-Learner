from sqlalchemy import Column , Integer , ForeignKey
from app.core.database import Base

class Edge(Base):
    __tablename__ = "edges"

    id = Column(Integer, primary_key=True, index=True)
    source_node_id = Column(Integer, ForeignKey("nodes.id"),nullable=False)
    target_node_id = Column(Integer, ForeignKey("nodes.id"),nullable=False)

