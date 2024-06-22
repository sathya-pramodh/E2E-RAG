import os
from gensim.models import KeyedVectors
from gensim.similarities.annoy import AnnoyIndexer
import threading


def load_model_and_predict(file, load_dir, query_word, num_neighbours):
    print(f"Loading {file}...")
    w2v_model = KeyedVectors.load_word2vec_format(
        os.path.join(load_dir, file), binary=True)
    annoy_indexer = AnnoyIndexer(w2v_model, 100)
    print(f"Most similar (approx) {num_neighbours} neighbours to '{
          query_word}' according to model '{file}' are: ")
    for pred in w2v_model.most_similar(
            positive=[query_word], topn=num_neighbours, indexer=annoy_indexer):
        print(pred)
    print(f"Most similar (exact) {num_neighbours} neighbours to '{
          query_word}' according to model '{file}' are: ")
    for pred in w2v_model.most_similar(
            positive=[query_word], topn=num_neighbours):
        print(pred)


def main():
    load_dir = "models"
    query_word = "Athena"
    num_neighbours = 1

    # Load w2v models saved.
    files = os.listdir(load_dir)
    threads = []
    for file in files:
        if file.startswith("vocab-"):
            thread = threading.Thread(target=lambda: load_model_and_predict(
                file, load_dir, query_word, num_neighbours))
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
