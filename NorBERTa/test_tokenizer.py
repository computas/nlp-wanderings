from tokenizers.implementations import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing

path = "./model"

tokenizer = ByteLevelBPETokenizer(
    "{path}/vocab.json".format(path=path),
    "{path}/merges.txt".format(path=path),
)

tokenizer._tokenizer.post_processor = BertProcessing(
    ("</s>", tokenizer.token_to_id("</s>")),
    ("<s>", tokenizer.token_to_id("<s>")),
)

tokenizer.enable_truncation(max_length=512)

tokenizer.encode("Dette er første testen.")

tokens = tokenizer.encode("Dette er første testen.").tokens

print(tokens)
