# AI Agent Evaluation & Observability Platform

A platform to test AI agents, measure how well they perform, and understand why they fail.

## What this project does

The platform helps AI developers:

- Register AI agents.
- Create datasets of tasks that agents should complete.
- Run the same tasks against different agents.
- Record agent steps and tool calls.
- Measure success, accuracy, latency, and token usage.
- Compare evaluation runs.
- Inspect failed tasks and their traces.

## Main technology choices

- **Backend:** Python and FastAPI
- **Agent workflow:** LangGraph
- **Database:** PostgreSQL
- **Frontend:** React and TypeScript
- **Testing:** Pytest
- **Deployment:** Docker

We will add more tools only when the project needs them.

## Project documentation

- [Product vision](docs/product/product-vision.md)
- [Functional requirements](docs/requirements/functional-requirements.md)
- [Non-functional requirements](docs/requirements/non-functional-requirements.md)
- [User stories](docs/requirements/user-stories.md)
- [Acceptance criteria](docs/requirements/acceptance-criteria.md)
- [High-level architecture](docs/architecture/high-level-architecture.md)
- [ADR 001: Technology stack](docs/decisions/ADR-001-technology-stack.md)

## First version (MVP)

The first version will support agent registration, benchmark datasets, evaluation runs, basic metrics, trace inspection, and run comparison.

## Development approach

Build the platform in small, testable steps. Keep requirements and architecture documentation updated when important decisions change.

## Important measurement rule

A metric is only useful when its meaning is clear. Task success should be checked using known expected results, deterministic checks, or human-reviewed labels. An AI judge can provide an additional opinion, but it should not be treated as perfect ground truth.
