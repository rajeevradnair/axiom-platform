from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/api/v1/axiom/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "axiom-platform",
        "package": "axiom",
        "runtime": "gcp-cloud-run-ready",
    }