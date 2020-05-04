OUTPUT_DIR=$PWD/model//NorBERTa-small-v1
TRAIN_FILE=$PWD/no_small.txt
CONFIG_DIR=$PWD/model
mkdir $OUTPUT_DIR


python run_language_modeling.py --train_data_file $TRAIN_FILE --output_dir $OUTPUT_DIR --model_type roberta --mlm --config_name $CONFIG_DIR --tokenizer_name $CONFIG_DIR --do_train --line_by_line --learning_rate 1e-4 --num_train_epochs 1 --save_total_limit 2 --save_steps 2000 --per_gpu_train_batch_size 4 --seed 42

