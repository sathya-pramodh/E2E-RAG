from gensim.models import KeyedVectors
from pgvector.psycopg2.register import psycopg2, register_vector
from psycopg2.extras import execute_values
from dotenv import load_dotenv, find_dotenv
import numpy as np
import os

load_dotenv(find_dotenv())

LOAD_DIR = "models"
FILE_NAME = "crawl-300d-2M-subword.bin"
TOTAL_KEYS = 2_00_000

neon_url = os.environ["NEON_URL"]
conn = psycopg2.connect(neon_url)
cursor = conn.cursor()

w2v_model: KeyedVectors = KeyedVectors.load(
    os.path.join(os.path.join("..", LOAD_DIR), FILE_NAME), mmap='r')

data_list = []

for i in range(TOTAL_KEYS):
    print(i)
    word = w2v_model.index_to_key[i]
    embedding = np.array(w2v_model.get_vector(word))

    data_list.append((word, embedding))

register_vector(conn)
execute_values(
    cursor, "INSERT INTO public.embeddings (word, embedding) \
            VALUES %s", data_list)
conn.commit()
conn.close()
