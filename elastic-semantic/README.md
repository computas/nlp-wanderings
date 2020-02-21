# Elastic Semantic

This repo aims to try out how to combine Elastic and Semantic search in a solution.

## FAISS
Faiss is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning. Faiss is written in C++ with complete wrappers for Python/numpy. Some of the most useful algorithms are implemented on the GPU. It is developed by Facebook AI Research.

[Github](https://github.com/facebookresearch/faiss)

## Setup
1. We assume you have miniconda installed. Then create the conda environment:
```
conda env create -f elastic-semantic.yaml
conda activate elastic-semantic
```

2. We use `sentence_transformers` and the current version has a bug. Patch your environment by copying the file [Dense.py](patch/Dense.py) to the correct path in your environment. Look at [patch-sentence_transformers.sh](patch/patch-sentence_transformers.sh) for an example on how to do this.

3. Start `jupyter lab` by running
``` 
jupyter lab
```
And go to the notebooks directory to run the notebooks.

4. In another terminal, start `elasticsearch` and `kibana` by running:
```
source run.sh
```