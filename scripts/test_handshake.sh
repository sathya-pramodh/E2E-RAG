#!/bin/bash
curl -X POST -H "Content-Type: application/json" -d @json/handshake.json http://0.0.0.0:5000/api/query_similar
