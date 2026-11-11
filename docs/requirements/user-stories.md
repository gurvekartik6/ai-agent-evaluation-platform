# User Stories

A user story describes a feature from the user's point of view.

## US-01: Register an agent

**As an AI developer,** I want to register my agent so that I can evaluate it on benchmark tasks.

## US-02: Create a dataset

**As an AI developer,** I want to create a dataset of test tasks so that I can test an agent repeatedly.

## US-03: Start an evaluation

**As an AI developer,** I want to select an agent and dataset and start a run so that I can measure the agent's performance.

## US-04: Track run progress

**As an AI developer,** I want to see whether a run is pending, running, completed, failed, or cancelled so that I know its current state.

## US-05: Inspect a trace

**As an AI developer,** I want to inspect the steps and tool calls for a test case so that I can understand how the agent reached its result.

## US-06: Find failed tasks

**As an AI developer,** I want to filter failed test cases so that I can focus on problems.

## US-07: Compare runs

**As an AI developer,** I want to compare two runs so that I can see whether a new agent version improved or became worse.

## US-08: Review metrics

**As an AI engineering lead,** I want to review success rate, latency, tool accuracy, and token usage so that I can assess agent quality.

## US-09: Export results

**As an AI developer,** I want to export evaluation results so that I can share or analyse them elsewhere.

## US-10: Cancel an evaluation

**As an AI developer,** I want to cancel a long-running evaluation so that I can stop unnecessary work.

## Priority

For the MVP, implement in this order:

1. Register agents.
2. Create datasets.
3. Start and execute evaluation runs.
4. Save task results and traces.
5. Calculate metrics.
6. View results and failures.
7. Compare runs.
8. Export results.
9. Add authentication and run cancellation as the architecture and milestones require.
