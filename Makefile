DEPS=flask gensim python-dotenv waitress
FLASK_APP=main
HOST="0.0.0.0"
PORT=5000
IMAGE_TAG="e2e-rag"
deps:
	python3 -m pip install $(DEPS)

test:
	cd scripts && sh test_handshake.sh

dev-run:
	cd src && env FLASK_APP=$(FLASK_APP) flask --debug run --host=$(HOST)
deploy:
	cd src && python3 main.py

docker:
	sudo docker build --tag $(IMAGE_TAG) .

docker-run:
	sudo docker run -d -p $(PORT):$(PORT) $(IMAGE_TAG)
