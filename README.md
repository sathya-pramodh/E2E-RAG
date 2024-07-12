# E2E-RAG
Repository to follow along with the RAG Workshop conducted by Harsh Singhal Sir at RIT.

# Usage (For development)
Install Dependencies
```bash
make deps
```
Setup
- Use `src/E2E-RAG.ipynb` to train all fasttext models and convert them to a readable format.
- After downloading the `crawl-300d-2M-subword.bin` and `crawl-300d-2M-subword.bin.vectors` file from the colab notebook, move them to `src/models` (should be created).
- Now setup a [Neon](https://neon.tech) DB project/any Postgres server (along with the pgvector extension) and make a `.env` at the project root with the following contents.
```
NEON_URL="<your url goes here>"
```
- Now in the DB, make a table called `embeddings` with the columns:
  - `id BIGSERIAL PRIMARY KEY`
  - `word TEXT` and,
  - `embedding VECTOR(300)`.
- Now run the script at `src/db/insert.py` and it should start inserting the vectors from `crawl-300d-2M-subword.bin`.

Run
```bash
make dev-run 
```

# Usage (For production)
Make docker image
```bash
make docker
```
Perform the setup instructions from the development usage instructions above.

Run
```bash
make docker-run
```
