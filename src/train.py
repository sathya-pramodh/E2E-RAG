from gensim.models import Word2Vec
from gensim.models.phrases import Phraser, Phrases
from gensim.utils import multiprocessing, os
from word_vectors import FileType, convert


def store_file(read_path, store_path):
    convert(
        read_path,
        output=store_path,
        output_file_type=FileType.W2V,
        input_file_type=FileType.FASTTEXT
    )


def store_w2v():
    base_dir = "models"
    save_dir = "models"

    # Read and store all vocabularies
    files = os.listdir(base_dir)
    for file in files:
        if file.endswith(".vec"):
            store_file(os.path.join(base_dir, file),
                       os.path.join(save_dir, f"vocab-{file.replace('.vec', '.w2v')}"))


def train_w2v():
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
    store_w2v()
