from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from yashish.database import models
from yashish.database.crud import interactions as crud_interactions
from yashish.server.dependencies import get_db
from yashish.server.schemas import interactions as interactions_schema

router = APIRouter()


@router.post(
    "/interaction/",
    response_model=interactions_schema.Interaction,
    operation_id="createInteraction",
)
async def create_interaction(
    interactions_create: interactions_schema.InteractionBase,
    db: Session = Depends(get_db),
) -> models.Interaction:
    interaction = crud_interactions.create_interaction(
        db, interactions=interactions_create
    )
    return interaction


@router.get(
    "/interaction/",
    response_model=List[interactions_schema.Interaction],
    operation_id="readInteractions",
)
async def read_interactions(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> List[models.Interaction]:
    interactions = crud_interactions.get_interactions(db, skip=skip, limit=limit)
    return interactions


@router.get(
    "/interaction/{interaction_id:int}",
    response_model=interactions_schema.Interaction,
    operation_id="readInteraction",
)
async def read_interaction(
    interaction_id: int, db: Session = Depends(get_db)
) -> models.Interaction:
    db_interaction = crud_interactions.get_interaction(db, interaction_id)

    if db_interaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interaction not found",
        )
    return db_interaction
