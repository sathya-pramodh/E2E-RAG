from flask import jsonify


class QueryResponse():
    neighbours = []

    def __init__(self, neighbours):
        self.neighbours = neighbours

    def jsonify(self):
        return jsonify(self.__dict__)
