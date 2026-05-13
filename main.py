from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Hello from DigitalOcean App Platform!",
        "status": "working",
        "environment": os.getenv("APP_ENV", "not-set")
    }


@app.get("/health")
def health():
    return {"health": "ok"}
