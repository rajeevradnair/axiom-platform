from fastapi import FastAPI

app = FastAPI(
    title="Axiom Platform",
    version="0.1.0",
    description="Trusted authorization infrastructure for agentic commerce.",
)


@app.get("/api/v1/axiom/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "axiom-platform",
        "package": "axiom",
        "runtime": "gcp-cloud-run-ready",
    }