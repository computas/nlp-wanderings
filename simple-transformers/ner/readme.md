# Setup

1. Create the conda environment `simple-transformers`:
  ```
    conda create -f simple-transformers.yaml
    conda activate simple-transformers
  ```

## Run the simple example

Reference: [https://towardsdatascience.com/simple-transformers-named-entity-recognition-with-transformer-models-c04b9242a2a0](https://towardsdatascience.com/simple-transformers-named-entity-recognition-with-transformer-models-c04b9242a2a0)

1. Go into `simple_example` folder and create a directory called `data`.
2. Download dataset from Kaggle: [https://www.kaggle.com/alaakhaled/conll003-englishversion/data](https://www.kaggle.com/alaakhaled/conll003-englishversion/data) and save `train.txt`, `test.txt` and `valid.txt` into `data` directory.
3. Run `python simple_example.py` and wait for it to finish the fine tuning.
4. Try different models from [https://github.com/ThilinaRajapakse/simpletransformers#current-pretrained-models](https://github.com/ThilinaRajapakse/simpletransformers#current-pretrained-models)

## Fine-tune BERT for NER with norwegian data (in progress)

1. Get Norwegian NER data from `https://github.com/ltgoslo/norne.git`:
  ```
    git clone https://github.com/ltgoslo/norne.git
  ```
