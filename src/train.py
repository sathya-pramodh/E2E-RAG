from collections import defaultdict
from gensim.models import Word2Vec
from gensim.models.phrases import Phraser, Phrases
from gensim.utils import multiprocessing, os


def train():
    base_dir = "data"
    files = os.listdir(path=base_dir)
    all_lines = []
    for file in files:
        with open(os.path.join(base_dir, file)) as file:
            lines = file.readlines()
            for line in lines:
                all_lines.append(line.strip())

    # Generate phrases from all the lines in the file from a list of words.
    sent = [line.split() for line in all_lines]
    phrases = Phrases(sent, min_count=10, progress_per=10000)
    bigram = Phraser(phrases)
    sentences = bigram[sent]

    word_freq = defaultdict(int)
    for sent in sentences:
        for i in sent:
            word_freq[i] += 1

    # Train the Word2Vec model on our case study text.
    cores = multiprocessing.cpu_count()
    w2v_model = Word2Vec(
        min_count=1,
        window=2,
        sample=6e-5,
        alpha=0.02,
        min_alpha=0.0008,
        negative=20,
        workers=cores-1,
    )
    w2v_model.build_vocab(sentences, progress_per=10000)
    w2v_model.train(
        sentences, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)
    w2v_model.save("./models/vocabulary")


if __name__ == "__main__":
    train()