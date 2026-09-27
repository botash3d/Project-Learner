from pydantic import BaseModel

class NodeOut(BaseModel):
    id: int
    title: str
    description: str | None=None

    class Config:
        from_attributes = True

class EdgeOut(BaseModel):
    id: int
    source_node_id: int
    target_node_id: int

    class Config:
        from_attributes = True

class CurriculumGraphOut(BaseModel):
    id: int 
    name: str
    description: str | None = None
    nodes: list[NodeOut]
    edges: list[EdgeOut]

