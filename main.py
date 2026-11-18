
from fastapi import FastAPI

# Create FastAPI application
app = FastAPI(
    title="Automated Multi-Platform Posting System",
    description="API for automated multi-platform posting",
    version="1.0.0"
)


# Home route
@app.get("/")
def home():
    return {
        "success": True,
        "message": "Welcome to Automated Posting System"
    }


# Test route
@app.get("/test")
def test():
    return {
        "success": True,
        "message": "FastAPI is working!"
    }
