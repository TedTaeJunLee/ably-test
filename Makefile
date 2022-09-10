.PHONY: all help

run-poetry-shell:
	@poetry shell

certs:
	@mkcert -install
	@rm -rf infra/local/cert && mkdir infra/local/cert
	@cd infra/local/cert && mkcert ably-test.local '*.ably-test.local'

