# Acceptance Criteria

Acceptance criteria explain how we decide that a feature is complete.

## AC-01: Register an agent

- The user can submit an agent name and supported adapter configuration.
- The name cannot be empty.
- The system creates a unique agent ID.
- The registered agent can be retrieved later.
- Invalid configuration produces a clear validation error.
- Secrets are not returned in API responses.

## AC-02: Create a dataset

- The user can create a dataset with a name and description.
- The user can add one or more test cases.
- Each test case has a task input.
- Invalid or empty test cases are rejected with a clear error.
- The dataset and its test cases can be retrieved later.

## AC-03: Start an evaluation run

- The user can select an existing agent and dataset.
- The API validates that both exist and can be used.
- The system creates a unique run ID.
- The API returns the run ID and initial status.
- The evaluation continues in the background.

## AC-04: Execute test cases

- The evaluation engine processes the dataset's test cases.
- Each test case receives an individual result.
- A test-case error is recorded and does not silently disappear.
- The run reaches a final status.
- The system records start and end times.

## AC-05: Capture traces

- Each executed test case has a trace record, even if execution fails.
- Available steps and tool calls are recorded in order.
- Errors are recorded in a readable form.
- Secrets and API keys are redacted.
- A trace can be retrieved using the relevant run and test-case identifiers.

## AC-06: Calculate metrics

- The platform calculates task success rate from the defined success labels.
- The platform calculates failure rate.
- Latency is calculated from recorded timestamps.
- Tool accuracy is calculated only when expected tool behaviour is available.
- Missing token or cost data is shown as unavailable, not as zero.
- Metric definitions are documented.

## AC-07: View run results

- The user can retrieve a run by ID.
- The response includes status and summary metrics when available.
- The user can retrieve per-case results.
- Failed cases include useful error information.
- Running results are clearly distinguished from completed results.

## AC-08: Compare two runs

- The user can select two existing runs.
- The system displays their key metrics side by side.
- The system identifies the agent and dataset for each run.
- The system does not compare incompatible datasets without clearly warning the user.

## AC-09: Export results

- The user can export a completed run.
- The exported file contains run metadata, metrics, and per-case results.
- The export does not contain API keys or other secrets.

## AC-10: Cancel a run

- A cancellation request is accepted only for a run that can still be cancelled.
- The run is marked cancelled after cancellation is handled.
- Results already saved remain available.
- The API clearly reports when a run is already completed or cannot be cancelled.
