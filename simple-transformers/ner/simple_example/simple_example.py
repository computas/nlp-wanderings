from simpletransformers.ner.ner_model import NERModel


# Create a NERModel
model = NERModel('bert', 'bert-base-cased', use_cuda=False, args={'learning_rate': 2e-5, 'overwrite_output_dir': True, 'reprocess_input_data': True})

# Train the model
model.train_model('data/train.txt')

# Evaluate the model
result, model_outputs, predictions = model.eval_model('data/test.txt')

# Check predictions
print(predictions[:5])