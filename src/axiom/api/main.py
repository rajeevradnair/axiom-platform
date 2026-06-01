from fastapi import FastAPI

from axiom.api.routes import authorizations, health, mandates


app = FastAPI(
    title="Axiom Platform",
    version="0.1.0",
    description="Trusted authorization infrastructure for agentic commerce.",
)

app.include_router(health.router)
app.include_router(mandates.router)
app.include_router(authorizations.router)