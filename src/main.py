import os
from flask import Flask, Response, request
from api.routes import query_similar
import psycopg2
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)

load_dotenv(find_dotenv())
neon_url = os.environ["NEON_URL"]
conn = psycopg2.connect(neon_url)


@ app.route("/api/query_similar", methods=["POST"])
def query_caller() -> Response:
    return query_similar(request, conn)


if __name__ == "__main__":
    from waitress import serve
    host = "0.0.0.0"
    port = 5000
    print(f"Serving production app at http://{host}:{port}.")
    serve(app, host=host, port=port)
