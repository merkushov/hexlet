install:
	@poetry install
update:
	@poetry update
lint:
	@poetry run flake8
test:
	@poetry run pytest tests/
# for Travis CI compatibility
ci_test: lint test
publish:
	poetry publish -r merkushov_gendiff
.PHONY: install update lint test publish ci_test
