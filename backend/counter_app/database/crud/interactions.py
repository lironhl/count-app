from typing import List, Optional

from sqlalchemy.orm import Session

from yashish.database import models
from yashish.server.schemas import interactions as interactions_schema


def get_interaction(db: Session, interaction_id: int) -> Optional[models.Interaction]:
    return (
        db.query(models.Interaction)
        .filter(models.Interaction.id == interaction_id)
        .first()
    )


def get_interactions(
    db: Session, skip: int = 0, limit: int = 100
) -> List[models.Interaction]:
    return db.query(models.Interaction).offset(skip).limit(limit).all()


def create_interaction(
    db: Session, interactions: interactions_schema.InteractionBase
) -> models.Interaction:
    db_interaction = models.Interaction(**interactions.dict())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction
