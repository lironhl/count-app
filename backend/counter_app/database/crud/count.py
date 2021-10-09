from typing import List, Optional

from sqlalchemy.orm import Session

from counter_app.database import models
from counter_app.server.schemas import count as count_schema


def get_count(db: Session, count_id: int) -> Optional[models.Count]:
    return (
        db.query(models.Count)
        .filter(models.Count.id == count_id)
        .first()
    )


def get_counts(
    db: Session, skip: int = 0, limit: int = 100
) -> List[models.Count]:
    return db.query(models.Count).offset(skip).limit(limit).all()


def create_count(
    db: Session, counts: count_schema.CountBase
) -> models.Count:
    db_count = models.Count(**counts.dict())
    db.add(db_count)
    db.commit()
    db.refresh(db_count)
    return db_count
