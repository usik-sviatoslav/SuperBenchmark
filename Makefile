# --- Variables --------------------------------------------------------------------------------------------------------
include .env
export SUPERBENCHMARK_DEBUG

IMAGE = super-benchmark:latest

# --- Docker -----------------------------------------------------------------------------------------------------------
.PHONY: build rebuild destroy up stop down down-v logs

rebuild: down destroy build

build:
	docker build --build-arg DEBUG=$(SUPERBENCHMARK_DEBUG) -t $(IMAGE) .

destroy:
	docker rmi -f $(IMAGE)

up:
	docker compose up -d

stop:
	docker compose stop

down:
	docker compose down

down-v:
	docker compose down -v

logs:
	docker compose logs -f


# --- Code Linters -----------------------------------------------------------------------------------------------------
.PHONY: lint flake8

lint: flake8

flake8:
	@echo "Starting flake8..."
	poetry run flake8 --toml-config=pyproject.toml .
	@echo "All done! ✨ 🍰 ✨"


# --- Code Formatters --------------------------------------------------------------------------------------------------
.PHONY: reformat isort black

reformat: isort black

isort:
	@echo "Starting isort..."
	poetry run isort --settings=pyproject.toml .

black:
	@echo "Starting black..."
	poetry run black --config=pyproject.toml .

# --- Type Checking ----------------------------------------------------------------------------------------------------
.PHONY: mypy

mypy:
	@echo "Starting type checking..."
	poetry run mypy --config-file=pyproject.toml .

# --- Pytest -----------------------------------------------------------------------------------------------------------
.PHONY: pytest pytest-cov

pytest:
	@echo "Starting pytest..."
	docker compose run --rm app pytest
	docker compose down -v

pytest-cov:
	@echo "Starting pytest with coverage..."
	docker compose run --rm app pytest --cov=. --cov-report=html
	docker compose down -v
