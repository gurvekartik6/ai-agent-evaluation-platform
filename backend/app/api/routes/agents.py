from fastapi import FastAPI, APIRouter, HTTPException, status

router = APIRouter()

app = FastAPI()

agents = [
    {
        "agent_id" : "001",
        "agent_name" : "Calculator Agent",
        "agent_description" : "Perform Mathematics Opeations",
        "active" : True
    },
    {
        "agent_id" : "002",
        "agent_name" : "Calculator Agent",
        "agent_description" : "Perform Mathematics Opeations",
        "active" : True
    },
    {
        "agent_id" : "003",
        "agent_name" : "Calculator Agent",
        "agent_description" : "Perform Mathematics Opeations",
        "active" : False
    },
    {
        "agent_id" : "004",
        "agent_name" : "Calculator Agent",
        "agent_description" : "Perform Mathematics Opeations",
        "active" : False
    }
]

@router.get("/")
async def get_agents():
    
    active_agents = []
    total_agents = len(agents)
    
    for agent in agents:
        if agent["active"] == True:
            active_agents.append(agent)
            
    return {
        "Active Agents": active_agents,
        "Total Agents" : total_agents
    }


@router.get("/{agent_id}")
async def get_agent(agent_id : str):
    
    for agent in agents:
        if agent["agent_id"] == agent_id:
            return agent
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Agent Not Found"
    )
    
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_agent(agent_data: dict):

    if not agent_data.get("name"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Agent name is required"
        )

    new_agent = {
        "id": f"agent-{len(agents) + 1:03d}",
        "name": agent_data["name"],
        "description": agent_data.get("description", ""),
        "framework": agent_data.get("framework", "Custom"),
        "active": True
    }

    agents.append(new_agent)

    return new_agent