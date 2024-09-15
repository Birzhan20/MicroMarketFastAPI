from fastapi import FastAPI
from pydantic import EmailStr, BaseModel

import uvicorn

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()
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
