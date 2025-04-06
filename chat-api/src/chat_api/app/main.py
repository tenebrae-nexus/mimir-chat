from fastapi import FastAPI
from loguru import logger

app = FastAPI(
    title="Chat API",
    description="API for chat functionality",
    version="0.1.0",
)

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    logger.info("Health check endpoint called")
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
