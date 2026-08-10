from fastapi import FastAPI

app = FastAPI(
    title="QA AI Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "QA AI Platform is running"
    }