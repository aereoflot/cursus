# Variables
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

# Regla por defecto
.DEFAULT_GOAL := help

help:
	@echo "════════════════════════════════════════════════════════════"
	@echo "  A-MAZE-ING - Makefile Commands"
	@echo "════════════════════════════════════════════════════════════"
	@echo ""
	@echo "📦 SETUP:"
	@echo "  make venv       - Create virtual environment (asks if exists)"
	@echo "  make install    - Install dependencies (auto-creates venv)"
	@echo ""
	@echo "🚀 EXECUTION:"
	@echo "  make generate   - Generate example mazes (non-interactive)"
	@echo "  make run        - Run main program (interactive mode)"
	@echo ""
	@echo "🔍 VALIDATION:"
	@echo "  make validate   - Validate output file (maze.txt)"
	@echo "  make lint       - Run flake8 + mypy"
	@echo ""
	@echo "📦 BUILD:"
	@echo "  make build      - Build pip package (wheel + tar.gz)"
	@echo ""
	@echo "🗑️  CLEANUP:"
	@echo "  make clean      - Clean temp files (keeps venv)"
	@echo "  make fclean     - Clean ALL + remove venv"
	@echo "  make re         - Rebuild from scratch (fclean + venv)"
	@echo ""
	@echo "════════════════════════════════════════════════════════════"
	@echo "  Note: All commands auto-activate venv"
	@echo "════════════════════════════════════════════════════════════"


check-venv:
	@if [ ! -d "$(VENV)" ]; then \
		echo "⚠️  Entorno virtual no encontrado. Creándolo..."; \
		./setup_venv.sh; \
	fi

generate: check-venv
	@. $(VENV)/bin/activate && $(PYTHON) generate_examples.py

venv:
	./setup_venv.sh

install: check-venv
	@. $(VENV)/bin/activate && $(PIP) install flake8 mypy build

run: check-venv
	@. $(VENV)/bin/activate && $(PYTHON) a_maze_ing.py config.txt

validate: check-venv
	@. $(VENV)/bin/activate && $(PYTHON) output_validator.py maze.txt

lint: check-venv
	@. $(VENV)/bin/activate && flake8 .
	@. $(VENV)/bin/activate && mypy . --warn-return-any --warn-unused-ignores \
		--ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

build: check-venv
	@. $(VENV)/bin/activate && $(PYTHON) -m build

clean:
	rm -rf __pycache__ .mypy_cache maze.txt dist/ build/ *.egg-info

fclean: clean
	rm -rf $(VENV)
	@echo "✓ Entorno virtual eliminado"

re: fclean venv

.PHONY: help check-venv generate venv install run validate lint build clean fclean re

# Capturar comandos no válidos
%:
	@echo "\033[91m❌ Error: Command '$@' not found in make\033[0m"
	@echo "\033[93mFor more information, run: make help\033[0m"
	@exit 1