from fastapi import FastAPI
from app.api.routes import agents

app = FastAPI(
    title="AI Agent Evaluation Platform",
    description="A platform to monitor and evaluate AI Agents",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "msg" : "AI Agent Evaluation Platoform is running",
        "status" : "running"
    }
    
app.include_router(
    agents.router,
    prefix="/api/v1/agents",
    tags=["Agents"]
)