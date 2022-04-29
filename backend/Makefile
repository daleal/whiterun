# Env stuff
.PHONY: build-env
build-env:
	python3 -m venv .venv
	poetry run pip install --upgrade pip
	poetry run poetry install

# Passive linters
.PHONY: black
black:
	poetry run black whiterun --check

.PHONY: flake8
flake8:
	poetry run flake8 whiterun

.PHONY: isort
isort:
	poetry run isort whiterun --profile=black --check

.PHONY: pylint
pylint:
	poetry run pylint whiterun

.PHONY: mypy
mypy:
	poetry run mypy whiterun

# Aggresive linters
.PHONY: black!
black!:
	poetry run black whiterun

.PHONY: isort!
isort!:
	poetry run isort whiterun --profile=black
