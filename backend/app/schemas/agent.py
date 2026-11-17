from pydantic import BaseModel, Field

class AgentCreate(BaseModel):
    
    name : str = Field (
        min_length=3,
        max_length=80,
        description="Name of the Agent"
    )
    
    description : str = Field (
        default="",
        max_length=500
    )
    
    framework : str = Field  (
        default="Custom",
        min_length=3,
        max_length=500
    )
    
class AgentResponse(BaseModel) :
    id: str
    name: str
    description: str
    framework: str
    active: bool

class AgentListResponse(BaseModel):

    count: int
    agents: list[AgentResponse]
