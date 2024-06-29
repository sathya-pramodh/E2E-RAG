from flask import Request, Response
from gensim.models import KeyedVectors
from query_types.query_response import QueryResponse
from query_types.query_request import QueryRequest


def query_similar(
    request: Request,
    w2v_model: KeyedVectors,
) -> Response:
    query_request = QueryRequest.from_json(request.get_json())
    nearest_neighbours = w2v_model.most_similar(
        positive=[query_request.query_word],
        topn=query_request.num_neighbours,
    )
    response = QueryResponse(nearest_neighbours)
    return response.jsonify()
