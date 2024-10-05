install:
	poetry install

install-hooks:
	poetry run pre-commit install

format-lint:
	poetry run pre-commit run --all-files

version:
	@poetry version $(v)
	@git add pyproject.toml
	@git commit -m "v$$(poetry version -s)"
	@git tag v$$(poetry version -s)
	@git push
	@git push --tags
	@poetry version

build:
	docker build . -f docker/dockerfile -t social_auto_posting

env:
	cp config/.env.template config/.env

up-dev:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d

up-prod:
	docker compose -f docker-compose.yml up -d

stop:
	docker compose -f docker-compose.yml stop

# migrations

makemigration-docker:
	docker compose exec social_auto_posting_api bash -c 'PYTHONPATH=app alembic --config "/app/src/alembic.ini" revision --autogenerate'

migrate-docker:
	docker compose exec social_auto_posting_api bash -c 'PYTHONPATH=app alembic --config "/app/src/alembic.ini" upgrade head'
