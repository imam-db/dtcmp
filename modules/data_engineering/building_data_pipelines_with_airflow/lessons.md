# Building Data Pipelines with Airflow — lesson checklist

Reference (titles only; unofficial): [Building Data Pipelines with Airflow](https://www.datacamp.com/courses/building-data-pipelines-with-airflow)

Write all notes, exercises, and solutions in your own words. Use synthetic data only.

Placeholders under each lesson:

- Notes (own words)
- Exercise (synthetic data)
- Solution

## Chapter 1: Authoring Dags with TaskFlow and XCom

### Airflow core concepts

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Writing a minimal TaskFlow Dag

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Matching Airflow components to their roles

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### The TaskFlow API

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Converting a classic Dag to TaskFlow

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Adding a task and wiring dependencies

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Exploring a pipeline in the Airflow UI

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Sharing data between tasks

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Returning data from a TaskFlow function

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Connecting a classic operator to a TaskFlow task

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Understanding XCom limitations

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

## Chapter 2: Dynamic and Data-Aware Pipelines

### Dynamic Task Mapping

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Processing multiple endpoints with expand

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Fixing a shared parameter with partial

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Pairing inputs with zip

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Data-aware scheduling with Assets

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Signaling data availability with an Asset outlet

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Scheduling a consumer Dag on an Asset

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Seeing asset-based scheduling in action

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Templating, idempotency, and backfilling

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Adding date-aware templating

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Making a pipeline idempotent

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Triggering a backfill

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Human-in-the-loop workflows

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Collecting form input with HITLEntryOperator

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Responding to a Required Action in the UI

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Branching with HITLBranchOperator

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

## Chapter 3: Preparing Dags for Production

### Robust Dags with failure handling and retries

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Configuring retries with exponential backoff

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Auto-pausing a failing Dag

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Choosing the right failure handling strategy

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Deferrable operators

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Configuring a sensor for production

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Making a sensor deferrable

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### When to use poke, reschedule, or deferrable

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Testing Airflow code

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Writing a Dag integrity test

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Unit testing a task function

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Integration testing with dag.test()

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Organizing complex Dags with Task Groups

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Grouping related tasks

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Nesting task groups with display names

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Organizing tasks by domain

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

## Chapter 4: Building a Production SQL ETL Pipeline

### Running SQL workloads

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Aggregating sales data with SQL

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Parameterizing SQL and extracting it into files

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Choosing the safe approach for user input

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Partition-aware scheduling with Asset Partitions

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Creating a partitioned pipeline

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Scheduling on partitioned assets

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Watching partitioned assets trigger a downstream Dag

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Data quality checks

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Adding column-level quality checks

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Adding table-level quality checks

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Catching data issues with the right operator

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### From development to production

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Triggering a pipeline from the CLI

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Backfilling historical data

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Production challenges with Airflow

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution

### Congratulations!

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution
