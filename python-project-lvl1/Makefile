install:
	@poetry install
update:
	@poetry update
lint:
	@poetry run flake8
# for Travis CI compatibility
ci_test: lint
publish:
	poetry publish -r merkushov_brain_games
.PHONY: install update lint test publish ci_test
