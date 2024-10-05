from contextlib import asynccontextmanager
from core.config import settings
from fastapi import FastAPI
from pydantic import EmailStr, BaseModel

import uvicorn

from items_views import router as items_router
from users.views import router as users_router
from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(
    items_router,
)
app.include_router(
    users_router,
)


@app.get("/hello/")
async def root(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
