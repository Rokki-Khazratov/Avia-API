from fastapi import FastAPI

app = FastAPI(
    title="Airline Management System API",
    description="Backend API for airline management system",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Hello World"} 