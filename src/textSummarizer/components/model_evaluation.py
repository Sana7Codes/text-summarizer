import torch
import evaluate
import pandas as pd
from tqdm import tqdm
from datasets import load_dataset, load_from_disk
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class ModelEvaluation:
    def __init__(self, config):
        self.config = config
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def generate_batch_sized_chunks(self, list_of_elements, batch_size):
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i : i + batch_size]


    def calculate_metric_on_test_ds(self, dataset, metric, model, tokenizer,
                                    batch_size=16,
                                    column_text="article",
                                    column_summary="highlights"):

        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))

        for article_batch, target_batch in tqdm(
            zip(article_batches, target_batches), total=len(article_batches)
        ):
            inputs = tokenizer(
                article_batch, max_length=1024, truncation=True,
                padding="max_length", return_tensors="pt"
            )

            summaries = model.generate(
                input_ids=inputs["input_ids"].to(self.device),
                attention_mask=inputs["attention_mask"].to(self.device),
                length_penalty=0.8,
                num_beams=8,
                max_length=128
            )

            decoded_summaries = [
                tokenizer.decode(s, skip_special_tokens=True, clean_up_tokenization_spaces=True)
                for s in summaries
            ]

            metric.add_batch(predictions=decoded_summaries, references=target_batch)

        return metric.compute()


    def evaluate(self):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(self.device)

        dataset = load_from_disk(self.config.data_path)

        rouge_metric = evaluate.load('rouge')
        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]

        score = self.calculate_metric_on_test_ds(
            dataset["test"],
            rouge_metric,
            model,
            tokenizer,
            batch_size=2,
            column_text="dialogue",
            column_summary="summary"
        )

        rouge_dict = {rn: round(score[rn]*100 , 2) for rn in rouge_names}
        df = pd.DataFrame(rouge_dict, index=["pegasus"])
        df.to_csv(self.config.metrics_file_name, index=False)
