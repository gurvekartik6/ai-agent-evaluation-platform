
from fastapi import APIRouter, HTTPException, status

from app.schemas.agent import (
    AgentCreate,
    AgentResponse,
    AgentListResponse
)

router = APIRouter()


# Temporary in-memory data
agents = [
    {
        "id": "agent-001",
        "name": "Research Agent",
        "description": "Researches technical topics",
        "framework": "LangGraph",
        "active": True
    },
    {
        "id": "agent-002",
        "name": "Analysis Agent",
        "description": "Analyses collected information",
        "framework": "Custom",
        "active": True
    }
]


# Get all agents
@router.get(
    "/",
    response_model=AgentListResponse
)
async def get_agents(
    active: bool | None = None,
    limit: int = 10
):

    results = agents

    if active is not None:
        results = [
            agent for agent in agents
            if agent["active"] == active
        ]

    selected_agents = results[:limit]

    return {
        "count": len(selected_agents),
        "agents": selected_agents
    }


# Get one agent
@router.get(
    "/{agent_id}",
    response_model=AgentResponse
)
async def get_agent(agent_id: str):

    for agent in agents:
        if agent["id"] == agent_id:
            return agent

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Agent not found"
    )


# Create a new agent
@router.post(
    "/",
    response_model=AgentResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_agent(agent_data: AgentCreate):

    new_agent = {
        "id": f"agent-{len(agents) + 1:03d}",
        "name": agent_data.name,
        "description": agent_data.description,
        "framework": agent_data.framework,
        "active": True
    }

    agents.append(new_agent)

    return new_agent
