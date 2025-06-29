# NLP Projects – Visual Infomedia  
**Internship Project by Shruti Sivakumar**  
**Duration:** 6 Weeks | **Domain:** NLP, Applied Machine Learning  
**Organization:** Visual Infomedia

---

## 🔍 Overview

This repository contains two NLP automation tools developed during a 6-week internship. The solutions address document parsing and keyword classification tasks and are deployed in a Streamlit web app.

---

## 🧠 Projects

### 📄 1. Automated Data Extraction from Business Memos  
Fine-tuned a GPT-4o-mini model to convert unstructured memo text into structured fields (e.g., title, agency, deadline). Includes dual-model versioning, schema validation, and Excel I/O.

- **Models**: GPT-4o-mini (v1, v2)  
- **Validation**: Pydantic schemas  
- **Accuracy**: 94.2% field extraction, 99.1% schema compliance

### 🏷️ 2. Multi-Label Keyword Classification System  
Trained a DistilRoBERTa model to tag 95,000+ bid titles with relevant keywords from a 4,000+ class vocabulary. Integrated confidence scoring and Excel-based output.

- **Architecture**: DistilRoBERTa  
- **Metrics**: Hamming Loss: 0.0004 · F1-Score (Micro): 0.356  
- **Inference**: Color-coded prediction with fallback logic

---

## 💻 Application Architecture

Multi-page Streamlit app with:
- Upload → Process → Download flow  
- Real-time progress tracking  
- Error handling and Excel export

> ⚠️ This repo contains a demonstration version. Proprietary model weights and business data are excluded.

---

## 📁 Project Structure

```
streamlit-nlp/
├── main.py
├── pages/
├── model_artifacts/
├── memo_parser.py
├── keyword_tagger.py
├── requirements.txt
├── .streamlit/secrets
└── README.md
```

---

## ⚙️ Local Setup

```bash
git clone https://github.com/shruti-sivakumar/streamlit-nlp.git
cd streamlit-nlp
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Edit `.streamlit/secrets` to include API keys.

---

## 🧰 Tech Stack  
Python · Streamlit · OpenAI API · HuggingFace Transformers · Pydantic · Scikit-learn · PyTorch · OpenPyXL

---

## 👩🏻‍💻 Author  
**Shruti Sivakumar**  
B.Tech CSE (AI), Amrita Vishwa Vidyapeetham  
📧 shruti.cbe@gmail.com  
🔗 [GitHub](https://github.com/shruti-sivakumar)  
💼 [LinkedIn](https://linkedin.com/in/shrutisivakumar25)

---

## 🛡️ Legal & Ethical Notes

- This repo is a sanitized version of the internship deliverables.  
- All sensitive data and proprietary models are excluded.  
- Commercial use requires separate licensing from Visual Infomedia.  
