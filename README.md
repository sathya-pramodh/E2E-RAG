# E2E-RAG
Repository to follow along with the RAG Workshop conducted by Harsh Singhal Sir at RIT.

# Usage (For development)
Install Dependencies
```bash
make deps
```
Setup
- Use `src/E2E-RAG.ipynb` to train all fasttext models and convert them to a readable format.
- After downloading the `.bin` and `.bin.vectors` files from the colab notebook, move them to `src/models` (should be created) and you should be completely setup. (The flask API only uses any one of those models and loads them onto RAM when running).

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
