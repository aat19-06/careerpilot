from fastapi import FastAPI

app=FastAPI(title="CareerPilot API")

@app.get("/")
def root() -> dict[str,str]:
    return {"message":"CareerPilot API is running"}

