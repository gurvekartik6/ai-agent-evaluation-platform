# Non-Functional Requirements

Non-functional requirements describe how well and how safely the platform must work.

## NFR-01: Reliability

The platform should handle an agent error without crashing the whole application.

A failed test case should be recorded with a useful error message.

## NFR-02: Performance

Normal API requests should return quickly.

Long evaluation runs must execute in the background. The API should return a run ID instead of keeping the HTTP request open until every test finishes.

## NFR-03: Scalability

The design should allow evaluation work to be moved to background workers and allow more workers to be added later.

## NFR-04: Security

- Never commit API keys or passwords to Git.
- Read secrets from environment variables or a secret manager.
- Do not expose secrets in API responses or logs.
- Validate incoming requests.
- Restrict access to data owned by other users when authentication is implemented.

## NFR-05: Data isolation

One user's agents, datasets, runs, and traces must not be visible to another user.

Database queries must enforce ownership rather than relying only on frontend checks.

## NFR-06: Reproducibility

Store enough information to understand how a run was performed, including:

- Agent identifier and version, when available.
- Dataset identifier and version, when available.
- Evaluation configuration.
- Metric definitions or evaluator version.
- Start and completion times.

Exact reproducibility may not always be possible because model providers can change model behaviour.

## NFR-07: Observability

The platform itself must produce useful application logs and error details.

Each evaluation run should have a correlation ID so related logs can be found.

## NFR-08: Maintainability

Use clear modules, type hints, consistent naming, automated tests, and database migrations.

Avoid placing all business logic inside API route handlers.

## NFR-09: Extensibility

The agent adapter interface should make it possible to add support for another agent framework without rewriting the evaluation engine.

## NFR-10: Data integrity

Use database constraints and transactions where appropriate. Do not report a run as completed until its final results have been saved successfully.

## NFR-11: Resource limits

Agent executions must have configurable timeouts and reasonable limits on retries and parallel tasks.

## NFR-12: Privacy

Store only information needed for evaluation. Provide a way to avoid recording sensitive inputs or tool outputs. Redact secrets before saving traces.
