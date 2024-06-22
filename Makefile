DEPS=numpy annoy scikit-learn gensim scipy==1.12 word_vectors
deps:
	python3 -m pip install $(DEPS)

run:
	python3 src/main.py

train:
	python3 src/train.py
