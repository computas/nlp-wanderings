# sentence-transformers
Testing of tranformer architectures for NLP with better sentence embeddings

## Setup

To create the environment you will need [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed.
1. Create the environment
    ```
    conda create env -f sentence-transformers.yaml
    ```
2. Activate the environment
    ```
    conda activate sentence-transformers
    jupyter nbextension enable --py widgetsnbextension
    ```
3. Enable jupyter widgets. Seems we need them because of the `tqdm` dependency when loading models directly from the `models` class and not the pre-trained ones.
    ```
    jupyter nbextension enable --py widgetsnbextension
    ```
    ToDo: See if you can remove this dependency by turning off these progress bars!
