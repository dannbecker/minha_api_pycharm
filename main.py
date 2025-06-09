import uvicorn
from fastapi import FastAPI
from database import engine, Base
from app.routers import empresa

app = FastAPI()

@app.on_event("startup")
def on_startup() -> None:
    """Create database tables if they do not exist."""
    Base.metadata.create_all(bind=engine)

@app.get("/")
def check_api():
    return {"response": "Api Online!"}

app.include_router(empresa.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)