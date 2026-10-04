from fastapi import FastAPI

from app.api.routes.health import router as health_router

app = FastAPI(title="CareerPilot API")

app.include_router(health_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "CareerPilot API is running"}