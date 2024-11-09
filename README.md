# SuperBenchmark

SuperBenchmark is a project for benchmarking performance metrics of a Large Language Model (LLM).
It provides an API to collect and analyze results data using FastAPI, with structured components and tests.

## Features

- **API for benchmarking data collection** with storage and analysis capabilities.
- **Asynchronous architecture** with FastAPI for efficient processing.
- **Built-in API documentation** with Swagger UI.
- **Testing coverage** for main API endpoints and core logic.

## Project Structure

```plaintext
.
├── app/
│   ├── api/
│   │   └── routes/                   # API routes
│   │
│   ├── core/                         # Configuration files
│   ├── schemas/                      # Pydantic schemas
│   ├── services/                     # Business logic
│   ├── utils/                        # Utility functions (e.g., JSON handlers)
│   └── tests/                        # Tests
│
├── .pre-commit-config.yaml           # Pre-commit hooks for automated code checks
├── docker-compose.yml                # Docker Compose file for container management
├── Dockerfile                        # Dockerfile for building the project
├── Makefile                          # Makefile for automation commands for build and testing 
├── poetry.lock                       # Locked dependencies file for Poetry
└── pyproject.toml                    # Poetry dependencies and project configuration
```
---

## Local Installation

1. Ensure **Python 3.11** and **Poetry** are installed.

2. Clone the repository and install dependencies:

   ```bash
   git clone https://github.com/usik-sviatoslav/SuperBenchmark.git
   cd SuperBenchmark
   poetry install
   ```

3. Create an .env file based on .env.example and configure necessary environment variables.

4. Run the application:

   ```bash
   poetry run uvicorn app.main:app --reload
   ```
---

## Docker Installation

1. Create an .env file based on .env.example and configure necessary environment variables.

2. Build the Docker image:

   ```bash
   make build
   ```

3. Start the containers:

   ```bash
   make up
   ```
---

## Running Tests

To run tests:

   ```bash
   make pytest
   ```

For test coverage reporting:

   ```bash
   make pytest-cov
   ```
---

## API Usage

After starting, the application will be accessible at [localhost](http://localhost:8000).
API documentation is available at [docs](http://localhost:8000/docs) & [redoc](http://localhost:8000/redoc)