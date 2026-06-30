.PHONY: install run debug clean lint lint-strict help

PYTHON = python3
UV = $(PYTHON) -m uv

help:
	@echo "Available commands:"
	@echo "  make install      - Install dependencies"
	@echo "  make run          - Run the application"
	@echo "  make debug        - Run the application in debug mode"
	@echo "  make lint         - Run code linting"
	@echo "  make clean        - Clean up build artifacts and caches"

export UV_CACHE_DIR = "$(PWD)/.uv_cache"

install:
	pip install uv
	$(UV) sync

run:
	@ echo "Running..."
	@ $(UV) run $(PYTHON) -m src || echo "Error: If not try 'make install'"

debug:
	$(PYTHON) run python -m pdb -m src

lint:
	$(PYTHON) -m flake8 src
	$(PYTHON) -m mypy src --follow-imports=skip --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(PYTHON) -m flake8 src
	$(PYTHON) -m mypy --strict src --follow-imports=skip --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

clean:
	@ echo "Clinning..."
	@ rm -rf .mypy_cache
	@ find . -type d -name "__pycache__" -exec rm -rf {} +
%:
	@echo "ERROR: Unknown command: '$@'"
	@echo "Use 'make help' to see available commands."
