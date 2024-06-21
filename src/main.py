from gensim.models import Word2Vec
from annoy import AnnoyIndex


def main():
    query_word = "SQL"
    num_neighbours = 10

    w2v_model = Word2Vec.load("./models/vocabulary")
    print(f"Most similar to '{query_word}' are: ")
    print(w2v_model.wv.most_similar(positive=[query_word]))
    aidx = AnnoyIndex(w2v_model.wv.vector_size,
                      "hamming")
    aidx.load("./models/neighbours")
    idx = w2v_model.wv.get_index(query_word)
    neigbours = aidx.get_nns_by_item(int(idx), num_neighbours)
    matched_keys = []
    for neighbour in neigbours:
        matched_keys.append(w2v_model.wv.index_to_key[neighbour])
    print()
    print(f"{num_neighbours} neighbours for '{query_word}' are:")
    print(matched_keys)


if __name__ == "__main__":
    main()
