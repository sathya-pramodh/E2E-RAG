#!/bin/bash
curl -X POST -H "Content-Type: application/json" -d @json/handshake.json http://127.0.0.1:5000/api/query_similar
