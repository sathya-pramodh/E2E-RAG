from flask import Flask, Response, request
from api.routes import query_similar
from gensim.models import KeyedVectors
import os

app = Flask(__name__)


LOAD_DIR = os.path.join("src", "models")
BIN_FILE_EXT = ".bin"

w2v_model = None
files = [file for file in os.listdir(LOAD_DIR) if file.endswith(BIN_FILE_EXT)]
for file in files:
    if file.endswith(BIN_FILE_EXT):
        print(f"Loading {os.path.join(LOAD_DIR, file)}...")
        w2v_model = KeyedVectors.load(
            os.path.join(LOAD_DIR, file), mmap='r')

if w2v_model is None:
    print(f"Unable to get any .bin files in {LOAD_DIR}")
    exit(0)


@app.route("/api/query_similar", methods=["POST"])
def query_caller() -> Response:
    return query_similar(request, w2v_model)


app.run()
