from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.curriculum import Curriculum, Node
from app.models.edge import Edge
from app.models.progress import Progress
from app.schemas.curriculum import CurriculumGraphOut
from app.schemas.progress import ProgressOut , CoverageOut

router = APIRouter(prefix="/api/curricula",tags=["curricula"])

DEFAULT_USER_ID = 1

@router.get("/{curriculum_id}/graph",response_model=CurriculumGraphOut)
def get_curriculum_graph(curriculum_id : int,db : Session=Depends(get_db)):
    curriculum = db.query(Curriculum).filter(Curriculum.id==curriculum_id).first()
    if not curriculum:
        raise HTTPException(status_code=404 , detail="Curriculum Not Found")

    node_ids = [n.id for n in curriculum.nodes]
    edges = db.query(Edge).filter(Edge.source_node_id.in_(node_ids),
            Edge.target_node_id.in_(node_ids)).all()
    return CurriculumGraphOut(
        id=curriculum.id,
        name=curriculum.name,
        description=curriculum.description,
        nodes=curriculum.nodes,
        edges=edges,
    )

@router.get("/{curriculum_id}/progress",response_model=list[ProgressOut])
def get_curriculum_progress(curriculum_id: int, db: Session = Depends(get_db)):
    node_ids = [n.id for n in db.query(Node).filter(Node.curriculum_id==curriculum_id).all()]
    progress_rows = db.query(Progress).filter(
        Progress.user_id==DEFAULT_USER_ID,
        Progress.node_id.in_(node_ids)
    ).all()

    return progress_rows

@router.get("/{curriculum_id}/coverage", response_model=CoverageOut)
def get_coverage(curriculum_id: int, db: Session = Depends(get_db)):
    curriculum = db.query(Curriculum).filter(Curriculum.id==curriculum_id).first()
    if not curriculum:
        raise HTTPException(status_code=404, detail="Curriculum Not Found")

    total_nodes = len(curriculum.nodes)
    node_ids = [n.id for n in curriculum.nodes]

    completed_nodes = db.query(Progress).filter(
        Progress.user_id == DEFAULT_USER_ID,
        Progress.node_id.in_(node_ids),
        Progress.completed == True
    ).count()

    percentage = (completed_nodes/total_nodes*100) if total_nodes > 0 else 0.0

    return CoverageOut(
        curriculum_id=curriculum_id,
        total_nodes=total_nodes,
        completed_nodes=completed_nodes,
        percentage=round(percentage,1)
        )