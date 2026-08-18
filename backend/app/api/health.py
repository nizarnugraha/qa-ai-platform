from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health():
    return {
        "status": "ok",
        "version": "0.1.0",
        "model": "Qwen2.5-Coder-7B"
    }