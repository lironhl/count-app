from typing import Optional, Tuple

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from counter_app.database import Base, engine
from counter_app.routers import count
from counter_app.utils.constants import COMMIT_SHA, ENV, ApiTags

Base.metadata.create_all(bind=engine)

openapi_tags = [{"name": tag.value} for tag in ApiTags]
app = FastAPI(openapi_tags=openapi_tags)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(count.router, tags=[ApiTags.Count])


@app.get("/")
async def ping() -> Tuple[str, Optional[str]]:
    return ENV, COMMIT_SHA


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
