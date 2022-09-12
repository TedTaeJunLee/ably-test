.PHONY: all help

run-poetry-shell:
	@poetry shell

certs:
	@mkcert -install
	@rm -rf infra/local/cert && mkdir infra/local/cert
	@cd infra/local/cert && mkcert ably-test.local '*.ably-test.local'

poetry-install-ably-test-backend:
	@poetry install

run-docker-ably-test-backend:
	@uwsgi --ini infra/local/wsgi/ably_test.ini


run-local-ably-test-backend:
	@export ENVIRONMENT='local'
	@cd src && poetry run ./manage.py runserver 0.0.0.0:8000
