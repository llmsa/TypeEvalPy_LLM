## Lint code using ruff
.PHONY: lint
lint:
	@echo "\n################\n Running ruff \n################\n"
	python -m ruff --version
	python -m ruff scalpel --exit-zero
	@echo "\n################\n Running isort \n################\n"
	python -m isort scalpel

## Format code using black
.PHONY: black
black:
	@echo "\n################\n Running black \n################\n"
	python -m black --version
	python -m black scalpel

## Run tests using pytest
.PHONY: pytest
pytest:
	@echo "\n################\n Running tests (pytest) \n################\n"
	python -m pytest --version
	# python -m pytest tests

## Run all tests
.PHONY: test
test: pytest

## Run all
.PHONY: all
all: lint black test
