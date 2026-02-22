from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Backend Core Service",
    version="1.0.0"
)

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow()
    }


@app.get("/anouar", tags=["Anouar"])
def anouar_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow()
    }