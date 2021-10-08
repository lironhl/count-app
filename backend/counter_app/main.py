from typing import Optional, Tuple

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from yashish.database import Base, engine
from yashish.routers import auth as auth_router
from yashish.routers import interactions, seniors, users
from yashish.utils.constants import COMMIT_SHA, ENV, ApiTags
from yashish.utils.sentry import init_sentry

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

app.include_router(auth_router.router, tags=[ApiTags.Auth])
app.include_router(users.router, tags=[ApiTags.Users])
app.include_router(seniors.router, tags=[ApiTags.Seniors])
app.include_router(interactions.router, tags=[ApiTags.Interactions])

init_sentry(app)


@app.get("/")
async def ping() -> Tuple[str, Optional[str]]:
    return ENV, COMMIT_SHA


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
