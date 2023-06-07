from fastapi import FastAPI

from app.api.trades import router as trades_router

app = FastAPI()

# Include the trades router
app.include_router(trades_router, prefix="/trades", tags=["trades"])

# Run the application using Uvicorn server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
