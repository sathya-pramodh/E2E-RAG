class QueryRequest:
    query_word: str = ""
    num_neighbours: int = 1

    def __init__(self, query_word, num_neighbours):
        self.query_word = query_word
        self.num_neighbours = num_neighbours

    @staticmethod
    def from_json(json):
        return QueryRequest(json["query_word"], json["num_neighbours"])
