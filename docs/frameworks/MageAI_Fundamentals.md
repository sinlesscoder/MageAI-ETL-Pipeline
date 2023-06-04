## MageAI Fundamentals

### Installation

#### Method 1: `pip`

- Install `MageAI` using `pip`.

```bash
pip install mage-ai
```

#### Method 2: `Docker`

- Install `MageAI` via `docker`

```bash
docker pull mageai/mageai
```

### Pipelines

- Pipelines are essentially a sequence of steps to get data from one form to another.

  - Often referred to as an ELT or ETL process.

- MageAI has support for the following types of data pipelines:
  - Batch (Standard) (Historical)
  - Data Integration (Merging with another technology)
  - Streaming (Real-time data processing)

### Triggers

- A mechanism that allows a pipeline to start or to be scheduled.

- Supported Mechanisms
  - Click-based event (button)
  - API Call
  - Schedule

### Runs

- A run is a specific instance of a trigger. If a trigger is started, your pipeline starts to run from step 1. That specific instance is called a run.

### Blocks

- A block is a component of your pipeline. Each step of the sequence is wrapped as a block.
- Within MageAI, blocks are actually Python scripts.

- Types of Blocks
  - Data Loaders (Primary)
  - Data Transformers (Primary)
  - Data Exporters (Primary)
  - DBT Model (Secondary)
  - Sensor (Secondary)
  - Scratchpad (Secondary)
