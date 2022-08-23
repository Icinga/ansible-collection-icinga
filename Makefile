.PHONY: test lint

test:
	python -m unittest -v

lint:
	python -m pylint plugins
