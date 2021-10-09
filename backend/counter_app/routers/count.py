from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from counter_app.database import models
from counter_app.database.crud import count as crud_count
from counter_app.server.dependencies import get_db
from counter_app.server.schemas import count as count_schema

router = APIRouter()


@router.post(
    "/count/",
    response_model=count_schema.Count,
    operation_id="createCount",
)
async def create_count(
    count_create: count_schema.CountCreate,
    db: Session = Depends(get_db),
) -> models.Count:
    count = crud_count.create_count(
        db, counts=count_create
    )
    return count


@router.get(
    "/count/",
    response_model=List[count_schema.Count],
    operation_id="readCounts",
)
async def read_counts(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> List[models.Count]:
    counts = crud_count.get_counts(db, skip=skip, limit=limit)
    return counts
