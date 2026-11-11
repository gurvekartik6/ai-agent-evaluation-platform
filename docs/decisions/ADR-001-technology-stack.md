# ADR-001: Initial Technology Stack

- **Status:** Accepted for the MVP
- **Date:** 2026-11-11
- **Decision owners:** Project team

## Context

We need a technology stack for a platform that registers AI agents, runs benchmark evaluations, stores traces, calculates metrics, and displays results.

The stack should support Python-based AI development, asynchronous APIs, reliable data storage, automated testing, and future deployment.

## Decision

Use the following technologies for the first version.

| Area | Choice | Reason |
|---|---|---|
| Backend language | Python | Strong AI and ML ecosystem |
| API framework | FastAPI | Typed request validation and async support |
| Agent orchestration | LangGraph | Useful for stateful agent workflows |
| Database | PostgreSQL | Reliable relational storage |
| Frontend | React + TypeScript | Interactive dashboard and type safety |
| Testing | Pytest | Python unit and integration testing |
| Containers | Docker | Consistent development and deployment environments |

## Why not add more tools immediately?

We will avoid adding Redis, a vector database, Kubernetes, or a complex message broker until a real requirement appears.

This keeps the first version easier to understand, test, and debug.

## Consequences

### Benefits

- One main backend language for the AI and evaluation logic.
- Clear API contracts.
- Relational storage for agents, datasets, runs, and results.
- A frontend that can grow into a full dashboard.
- A path toward background workers and container-based deployment.

### Trade-offs

- The team must learn and maintain both Python and TypeScript.
- Background job execution will need a deliberate design.
- LangGraph adds a framework dependency, so core evaluation logic should remain independent where possible.
- Docker introduces an additional development tool to learn.

## Future review

Review this decision when we introduce:

- Dedicated background workers and a job queue.
- Distributed execution across multiple machines.
- Vector search or retrieval features.
- Production authentication and authorization.
- Production monitoring and deployment.
