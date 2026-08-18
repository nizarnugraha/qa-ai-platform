from fastapi import FastAPI

from backend.app.api.health import router as health_router

app = FastAPI(
    title="QA AI Platform",
    version="0.1.0"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "QA AI Platform is running"
    }