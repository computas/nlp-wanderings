# Experimental
Create a small version of a norwegian language model from scratch

## Setup

Use the `norberta.yaml` file to produce a conda environment:

```shell
conda env update -f norberta.yaml
```

Run then the following:
1. `source get_data.sh`  will download the dataset
2. `python train_tokenizer.py` will create the vocabulary files for the model
3. `source get_training_file.sh` will download the training script
4. `python config_model.py` will setup the training configuration
5. The file is too big to process and the whole thing dies without spitting any error. I'm assuming the process runs out of memory. The train script should be modified. A small workaround is to use a smaller version of the file:

```shell
head -n 100000 no.txt >> no_small.txt
```

6. `source train.sh` will train the model on the small file with the configuration I fould that works so far on CPU. If you have a GPU, you can increase the `--per_gpu_train_batch_size 8` (for colab).

A colab notebook is available to use with the standard plan: [01_how_to_train_norbert.ipynb](01_how_to_train_norbert.ipynb). Nevertheles it is a painful process since the notebook dies after a few iterations. Use the `--should_continue` parameter to continue where you left (but do not use this parameter the first time, since it will find no directory and return an error, since you have not produced anything yet). The checkpoints are saved on your google drive (must run the cell to mount your drive).
