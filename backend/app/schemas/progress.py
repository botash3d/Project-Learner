from pydantic import BaseModel

class ProgressUpdate(BaseModel):
    completed: bool

class ProgressOut(BaseModel):
    node_id: int
    completed: bool

    class Config:
        from_attributes = True

class CoverageOut(BaseModel):
    curriculum_id: int
    total_nodes: int
    completed_nodes: int
    percentage: float
    