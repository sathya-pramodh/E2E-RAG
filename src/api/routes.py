from flask import Request, Response
from query_types.query_response import QueryResponse
from query_types.query_request import QueryRequest
from psycopg2.extensions import connection


def query_similar(
    request: Request,
    conn: connection
) -> Response:
    query_request = QueryRequest.from_json(request.get_json())
    nearest_neighbours = []
    cursor = conn.cursor()
    embedded_query = (
        f"SELECT embedding \
            FROM public.embeddings \
            WHERE word = '{query_request.query_word}'"
    )
    query = (
        f"SELECT word \
            FROM public.embeddings \
            ORDER BY embedding <=> ({embedded_query}) \
            LIMIT {query_request.num_neighbours}"
    )
    cursor.execute(query)
    for row in cursor:
        nearest_neighbours.append(row[0])
    cursor.close()
    response = QueryResponse(nearest_neighbours)
    return response.jsonify()
