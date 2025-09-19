from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from fastapi_pet.routers.api import user_router

app = FastAPI(title="FastAPI pet")

app.include_router(user_router)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
