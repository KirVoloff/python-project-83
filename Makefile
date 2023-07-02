install:
	poetry install

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

build:
	poetry build

dev:
	poetry run flask --app page_analyzer:app run

setup: install lock

PORT ?= 8000
