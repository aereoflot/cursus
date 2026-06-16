.PHONY: install run debug clean lint lint-strict help

PYTHON = python3
MAIN = main.py
MAPS ?= maps

help:
	@echo "Available commands:"
	@echo "  make install     - Install project dependencies"
	@echo "  make run         - Execute the main script"
	@echo "\t  make run-easy   - Execute maps/easy"
	@echo "\t  make run-medium - Execute maps/medium"
	@echo "\t  make run-hard   - Execute maps/hard"
	@echo "\t  make run-challenger   - Execute maps/challenger"
	@echo "  make debug       - Run the main script in debug mode using pdb"
	@echo "  make clean       - Remove temporary files and caches"
	@echo "  make lint        - Run flake8 and mypy for linting and type checking"
	@echo "  make lint-strict - Run flake8 and mypy with strict checking"
	@echo "  make help        - Show this help message"

install:
	$(PYTHON) -m pip install flake8 mypy
	@if [ -f requirements.txt ]; then $(PYTHON) -m pip install -r requirements.txt; fi

run:
	$(PYTHON) $(MAIN)

run-easy:
	@if [ ! -d "$(MAPS)/easy" ]; then \
		printf "Add maps/easy folder please.\n"; \
	else \
		for map in $(MAPS)/easy/*.txt; do \
			printf "Map: %s\n" "$$map"; \
			$(PYTHON) $(MAIN) "$$map"; \
			echo ""; \
		done; \
	fi

run-medium:
	@if [ ! -d "$(MAPS)/medium" ]; then \
		printf "Add $(MAPS)/medium folder please.\n"; \
	else \
		for map in $(MAPS)/medium/*.txt; do \
			echo ""; \
			printf "Map $$map:\n"; \
			$(PYTHON) $(MAIN) "$$map"; \
		done; \
	fi

run-hard:
	@if [ ! -d "$(MAPS)/hard" ]; then \
		printf "Add $(MAPS)/hard folder please.\n"; \
	else \
		for map in $(MAPS)/hard/*.txt; do \
			echo ""; \
			printf "Map $$map:\n"; \
			$(PYTHON) $(MAIN) "$$map"; \
		done; \
	fi

run-challenger:
	@if [ ! -d "$(MAPS)/challenger" ]; then \
		printf "Add $(MAPS)/challenger folder please.\n"; \
	else \
		printf "\nMap Challenger:\n"; \
		$(PYTHON) $(MAIN) $(MAPS)/challenger/01_the_impossible_dream.txt; \
	fi

run-count:
	@if [ ! -d "$(MAPS)" ]; then \
		printf "Add maps folder please.\n"; \
	else \
		for level in easy medium hard challenger; do \
			if [ ! -d "$(MAPS)/$$level" ]; then \
				printf "Add $(MAPS)/%s folder please.\n" "$$level"; \
				continue; \
			fi; \
			printf "\nLevel: %s\n" "$$level"; \
			for map in $(MAPS)/$$level/*.txt; do \
				[ -e "$$map" ] || continue; \
				printf "  File: %s\n" "$$(basename "$$map")"; \
				lines=`$(PYTHON) $(MAIN) "$$map" | wc -l`; \
				printf "    Moves: %s\n\n" "$$lines"; \
			done; \
		done; \
	fi

debug:
	$(PYTHON) -m pdb $(MAIN)

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

lint:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --strict

%:
	@echo "Error: Unknown target '$@'"
	@$(MAKE) help
