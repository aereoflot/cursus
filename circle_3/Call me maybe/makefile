UV := py -m uv

.PHONY: install lint run debug clean

install:
	$(UV) sync

run:
	$(UV) run python -m src

debug:
	$(UV) run python -m pdb -m src

lint:
	$(UV) run flake8 src
	$(UV) run mypy src --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

clean:
	$(UV) run python -c "from pathlib import Path; import shutil; root = Path('.'); [shutil.rmtree(path, ignore_errors=True) for path in root.rglob('__pycache__')]; [path.unlink() for path in root.rglob('*.pyc')]; [shutil.rmtree(path, ignore_errors=True) for path in (root / '.mypy_cache', root / '.pytest_cache', root / 'build', root / 'dist')]"