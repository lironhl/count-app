start:
	docker run -p 5432:5432 --name dev-postgres -e POSTGRES_PASSWORD=mysecretpassword -v postgres-vol:/var/lib/postgresql -d postgres:13-alpine &
	poetry run uvicorn yashish.main:app --host 0.0.0.0 --reload

stop:
	docker stop dev-postgres &
	docker rm dev-postgres

prod:
	poetry run uvicorn yashish.main:app --host 0.0.0.0

format:
	poetry run isort yashish alembic
	poetry run black yashish alembic

format-check:
	poetry run isort --check yashish alembic
	poetry run black --check yashish alembic

lint:
	poetry run flake8 yashish alembic
	poetry run mypy --strict yashish

is-idiomatic:
	make format-check
	make lint