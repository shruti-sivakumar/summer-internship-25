import torch
import pandas as pd
import numpy as np
from transformers import AutoTokenizer
import joblib
import json
import os

# Set paths to model artifacts
artifacts_path = "./model_artifacts"

# Load keyword list
with open(os.path.join(artifacts_path, "keywords.json"), "r") as f:
    keywords_list = json.load(f)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(os.path.join(artifacts_path, "tokenizer"))

# Load binarizer
mlb = joblib.load(os.path.join(artifacts_path, "mlb.pkl"))

# Define model class
class MultiLabelClassifier(torch.nn.Module):
    def __init__(self, transformer_model, num_labels):
        super().__init__()
        from transformers import AutoModel
        self.transformer = AutoModel.from_pretrained(transformer_model)
        self.classifier = torch.nn.Linear(self.transformer.config.hidden_size, num_labels)

    def forward(self, input_ids, attention_mask):
        outputs = self.transformer(input_ids=input_ids, attention_mask=attention_mask)
        pooled = outputs.last_hidden_state[:, 0]  # CLS token
        return self.classifier(pooled)

def predict_keywords(text, model, tokenizer, keywords_list, device, threshold=0.4):
    model.eval()
    encoding = tokenizer(
        text,
        truncation=True,
        padding='max_length',
        max_length=512,
        return_tensors='pt'
    )

    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)

    with torch.no_grad():
        outputs = model(input_ids, attention_mask)
        probs = torch.sigmoid(outputs).cpu().numpy()[0]

    predictions = probs > threshold
    predicted_keywords = [keywords_list[i] for i in range(len(keywords_list)) if predictions[i]]
    selected_probs = [probs[i] for i in range(len(probs)) if predictions[i]]

    fallback_used = False
    if not predicted_keywords:
        top_idx = int(probs.argmax())
        predicted_keywords = [keywords_list[top_idx]]
        selected_probs = [probs[top_idx]]
        fallback_used = True

    max_prob = max(selected_probs) if selected_probs else 0.0
    return " | ".join(predicted_keywords), fallback_used, max_prob

def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = MultiLabelClassifier("distilroberta-base", num_labels=len(keywords_list))
    model.load_state_dict(torch.load(os.path.join(artifacts_path, "model_state_dict.pth"), map_location=device))
    model.to(device)
    model.eval()
    return model, tokenizer, keywords_list, mlb, device

def process_excel_streaming(df, model, tokenizer, keywords_list, device):
    total = len(df)

    # Detect actual column name for bid title
    bid_title_col = None
    for col in df.columns:
        if col.strip().lower().replace(" ", "") == "bidtitle":
            bid_title_col = col
            break

    if not bid_title_col:
        raise ValueError("'Bid Title' column not found in uploaded Excel.")

    for i, row in enumerate(df.iterrows(), 1):
        bid_title = row[1].get(bid_title_col, None)

        if pd.isna(bid_title):
            result = {
                "keywords": "",
                "fallback": False,
                "max_prob": 0.0
            }
        else:
            pred, fallback, max_prob = predict_keywords(str(bid_title), model, tokenizer, keywords_list, device)
            result = {
                "keywords": pred,
                "fallback": fallback,
                "max_prob": max_prob
            }
            
        yield i, total, result