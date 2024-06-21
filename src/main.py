from gensim.models import Word2Vec


def main():
    w2v_model = Word2Vec.load("./models/vocabulary")
    print(w2v_model.wv.most_similar(positive=["SQL"]))


if __name__ == "__main__":
    main()
