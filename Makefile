PORT ?= 8000

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

dev:
	poetry run flask --app page_analyzer:app run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 page_analyzer

check:
	poetry check

setup: install lock

test:
		poetry run pytest -v

test-coverage:
		poetry run pytest --cov=page_analyzer --cov-report xml

MANAGE := poetry run python manage.py

install:
	@poetry install

make-migration:
	@$(MANAGE) makemigrations

migrate: make-migration
	@$(MANAGE) migrate

build: install migrate
