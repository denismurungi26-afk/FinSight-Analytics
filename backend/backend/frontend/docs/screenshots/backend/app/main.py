from fastapi import FastAPI

app = FastAPI(
    title="FinSight Analytics API",
    description=(
        "Backend API for managing transactions, budgets, "
        "savings goals, and financial analytics."
    ),
    version="1.0.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Welcome to the FinSight Analytics API",
        "status": "running",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "FinSight Analytics API",
    }
