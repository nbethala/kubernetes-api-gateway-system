from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def readiness():
    return {"status": "ready"}

@app.get("/info")
def info():
    return {"service": "product-service", "version": "1.0.0"}
