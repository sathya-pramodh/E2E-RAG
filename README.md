# E2E-RAG
Repository to follow along with the RAG Workshop conducted by Harsh Singhal Sir at RIT.

# Usage (using GNU Make)
Install Dependencies
```bash
make deps
```
Setup
- Make a directory called `models` at the root.
- Download any fasttext models from [here](https://fasttext.cc/docs/en/english-vectors.html).
- Extract the zips so that all the `.vec` files are in the `models` directory.

Train
```bash
make train
```
Run
```bash
make run
```
