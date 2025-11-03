from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="OCR API Production", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "🚀 OCR API - DEPLOY THANH CONG!",
        "status": "working",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}

@app.get("/test")
def test_endpoint():
    return {"test": "success", "api": "working"}

@app.get("/info")
def api_info():
    return {
        "name": "OCR API",
        "version": "1.0.0",
        "status": "active",
        "endpoints": [
            {"path": "/", "method": "GET", "description": "Home page"},
            {"path": "/health", "method": "GET", "description": "Health check"},
            {"path": "/test", "method": "GET", "description": "Test endpoint"},
            {"path": "/info", "method": "GET", "description": "API information"}
        ]
    }
