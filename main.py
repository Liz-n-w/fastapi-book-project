from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.books import router as books_router 

from api.router import api_router
from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is working!"}

@app.get("/api/v1/books/1")
def get_book():
    return {"id": 1, "title": "FastAPI Guide"}