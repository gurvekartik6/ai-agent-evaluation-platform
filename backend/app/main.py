from fastapi import FastAPI

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