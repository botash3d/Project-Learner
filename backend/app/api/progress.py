from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.curriculum import Curriculum , Node
from app.models.progress import Progress
from app.schemas.progress import ProgressUpdate , ProgressOut , CoverageOut

router = APIRouter(prefix="/api" , tags=["progress"])

DEFAULT_USER_ID = 1

@router.put("/progress/{node_id}",response_model=ProgressOut)
def update_progress(node_id: int , update : ProgressUpdate , db: Session = Depends(get_db)):
    node = db.query(Node).filter(Node.id==node_id).first()
    if not node:
        raise HTTPException(status_code=404 , detail="Node Not Found")
    
    progress = db.query(Progress).filter(
        Progress.user_id==DEFAULT_USER_ID,
        Progress.node_id==node_id
    ).first()

    if progress:
        progress.completed = update.completed
    else:
        progress = Progress(user_id=DEFAULT_USER_ID , node_id=node_id , completed = update.completed)
        db.add(progress)

    db.commit()
    db.refresh(progress)
    return progress

