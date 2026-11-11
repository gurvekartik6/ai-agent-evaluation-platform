# High-Level Architecture

## 1. Overview

The platform has a frontend, an API backend, an evaluation engine, agent adapters, and a database.

The frontend is used to manage agents and datasets and to inspect evaluation results. The backend validates requests and coordinates the work. The evaluation engine runs test cases and calculates metrics.

## 2. Main components

### Frontend

**Technology:** React and TypeScript

Responsibilities:

- Register and view agents.
- Create benchmark datasets.
- Start evaluation runs.
- View run status and metrics.
- Inspect traces and failures.
- Compare runs.

### API backend

**Technology:** Python and FastAPI

Responsibilities:

- Provide REST API endpoints.
- Validate requests and responses.
- Coordinate application services.
- Return evaluation run IDs.
- Provide results to the frontend.

Keep business logic in service modules, not directly inside route handlers.

### Evaluation engine

Responsibilities:

- Load dataset test cases.
- Call the selected agent adapter.
- Record each test result.
- Collect traces.
- Calculate metrics.
- Update run status.

Long-running evaluations should be executed in the background.

### Agent adapter

The adapter gives the evaluation engine one common way to call different agents.

Initial interface proposal:

```python
from typing import Any, Protocol

class AgentAdapter(Protocol):
    async def execute(self, task: str) -> dict[str, Any]:
        ...

    async def get_metadata(self) -> dict[str, Any]:
        ...
```

This interface is an initial proposal. We will refine it when defining the trace and result data models.

### Database

**Technology:** PostgreSQL

Stores:

- Users.
- Agents.
- Datasets.
- Dataset test cases.
- Evaluation runs.
- Test-case results.
- Execution traces.
- Metric summaries.

Use database migrations to manage schema changes.

## 3. Evaluation flow

1. A user selects an agent and a dataset in the frontend.
2. The frontend sends a request to the FastAPI backend.
3. The backend validates the request.
4. The backend creates an evaluation run with `pending` status.
5. A background worker picks up the run.
6. The evaluation engine loads the dataset's test cases.
7. The engine calls the agent through its adapter.
8. The adapter returns the agent output and available execution information.
9. The engine stores the test result and trace.
10. The metrics evaluator calculates summary metrics.
11. The run is marked `completed`, `failed`, or `cancelled`.
12. The frontend retrieves and displays the results.

## 4. Simplified component diagram

```text
+---------------------------+
| React + TypeScript        |
| Dashboard                 |
+-------------+-------------+
              |
              | HTTP / REST
              v
+---------------------------+
| FastAPI                   |
| API routes and services   |
+-------------+-------------+
              |
              v
+---------------------------+
| Evaluation Engine         |
| Runner + Metrics          |
+-------------+-------------+
              |
              v
+---------------------------+
| Agent Adapter             |
| Common execution contract |
+-------------+-------------+
              |
              v
+---------------------------+
| AI Agent                  |
| LangGraph or other agent  |
+---------------------------+

       Evaluation data
              |
              v
+---------------------------+
| PostgreSQL                |
| Agents, datasets, runs,   |
| results, traces, metrics  |
+---------------------------+
```

## 5. Background execution

An evaluation may take seconds or minutes. The API should not wait for the complete evaluation.

The API should create a run, schedule the work, and return the run ID. A worker performs the evaluation and saves progress.

For the first working version, we can begin with a simple background execution approach. We will introduce a dedicated queue and worker when the project reaches that milestone.

## 6. Error handling

- Validate input before starting work.
- Apply a timeout to agent execution.
- Record errors for individual test cases.
- Prevent one failed case from silently losing the other results.
- Mark the run with an appropriate final status.
- Redact secrets from logs and traces.

## 7. Initial design boundaries

- PostgreSQL is the source of truth for evaluation records.
- No vector database is needed for the first version.
- Agent integrations go through adapters.
- Metric calculations should be testable independently.
- LLM-based judging is optional and must be identified separately from deterministic checks.
