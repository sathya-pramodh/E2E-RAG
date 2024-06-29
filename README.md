# E2E-RAG
Repository to follow along with the RAG Workshop conducted by Harsh Singhal Sir at RIT.

# Usage (using GNU Make)
Install Dependencies
```bash
make deps
```
Setup
- Use `src/E2E-RAG.ipynb` to train/convert all fasttext models and convert them to a readable format.
- After downloading the `.bin` and `.bin.vectors` files from the colab notebook, move them to `src/models` (should be created) and you should be completely setup. (The flask API only uses one of those models and loads them onto RAM when running it).

Run
```bash
make run
```
