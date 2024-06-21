DEPS=numpy annoy
deps:
	python3 -m pip install $(DEPS)

run:
	python3 src/main.py
