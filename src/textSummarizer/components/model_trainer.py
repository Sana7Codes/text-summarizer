import os
import torch
from pathlib import Path
from textSummarizer.logging import logger
from datasets import load_dataset, load_from_disk
from textSummarizer.config.configuration import ModelTrainerConfig
from transformers import AutoTokenizer,DataCollatorForSeq2Seq, TrainingArguments, Trainer,AutoModelForSeq2SeqLM





class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        

    def train(self):
        device = torch.device("cpu")
        tokenizer= AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus= AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model = model_pegasus)



        dataset_samsum_pt= load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
    output_dir=self.config.root_dir,
    num_train_epochs=self.config.num_train_epochs,
    warmup_steps=self.config.warmup_steps,
    per_device_train_batch_size=self.config.per_device_train_batch_size,
    weight_decay=self.config.weight_decay,
    logging_steps=self.config.logging_steps,
    do_eval=True,
    save_steps=self.config.save_steps,
    gradient_accumulation_steps=self.config.gradient_accumulation_steps,
    no_cuda= True,  # Set to True to use CPU
)

        trainer = Trainer(model= model_pegasus,
                          args=trainer_args,
                          tokenizer=tokenizer,
                          data_collator=seq2seq_data_collator,
                          train_dataset=dataset_samsum_pt["train"],
                          eval_dataset= dataset_samsum_pt["validation"]
                          )

        trainer.train()


        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))

        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))