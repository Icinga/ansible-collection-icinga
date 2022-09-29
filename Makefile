.PHONY: test lint

build:
	ansible-galaxy collection build .
test:
	python -m unittest -v
lint:
	python -m pylint plugins
