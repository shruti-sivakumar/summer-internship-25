# NLP Projects – Visual Infomedia

**Internship Project by Shruti Sivakumar**  
**Duration:** 6 Weeks | **Domain:** Natural Language Processing (NLP), Applied Machine Learning  
**Organization:** Visual Infomedia

---

## 🔍 Overview

This repository contains two end-to-end NLP projects developed during a 6-week internship at Visual Infomedia. The projects were built to solve real-world text processing problems using applied machine learning and deployed in an interactive web application using **Streamlit**.

---

## 🧠 Projects

### 📄 1. Data Extraction from Business Memos

A GPT-based system that extracts structured fields (e.g. bid title, agency, deadlines) from unstructured memo text.

- ✅ Fine-tuned GPT-4o-mini with schema validation (Pydantic)
- ✅ Two rounds of fine-tuning for improved accuracy on production data
- ✅ Batch processing of memos with Excel input/output
- ✅ Integrated into a user-friendly Streamlit UI

### 🏷️ 2. Multi-Label Keyword Classification

A transformer-based model that classifies bid titles into multiple relevant keywords from a large controlled vocabulary.

- ✅ Trained DistilRoBERTa on 95,000+ titles and 4,000+ keywords
- ✅ Weighted loss function + label smoothing
- ✅ Confidence scoring and color-coded keyword predictions
- ✅ Excel input/output with batch processing

---

## 💻 Application Demo (Streamlit)

The app provides a simple two-section interface:
- Upload Excel → Process → Download Results  
- Real-time progress indicator and preview

> 🔐 Note: Due to proprietary models and APIs, the app is not deployed publicly.  
> This repo contains a mock/demo version for demonstration purposes.

---

## 📁 Directory Structure

```
streamlit-nlp/
│
├── main.py                        # Streamlit entry (Home page)
├── pages/
│   ├── data_extraction.py        # Streamlit page: Memo Parsing
│   └── keyword_tagging.py        # Streamlit page: Keyword Classification
│
├── memo_parser.py                # GPT-4o-mini based memo extraction logic
├── keyword_tagger.py             # Multi-label keyword classification logic
├── requirements.txt
├── .gitignore
└── README.md
```
⚠️ Note: model_artifacts/ and .env are excluded from this repository due to proprietary model files and API keys.

---

## ⚙️ How to Run Locally

1. Clone the repo
   ```bash
   git clone https://github.com/yourusername/nlp-internship-projects.git
   cd nlp-internship-projects
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app
   ```bash
   streamlit run main.py
   ```

---

## 📦 Tech Stack

- Python 3.10+
- Streamlit
- OpenAI GPT-4o-mini (via API)
- HuggingFace Transformers (DistilRoBERTa)
- Pydantic, Pandas, Scikit-learn

---

## 👩🏻‍💻 Author

**Shruti Sivakumar**  
B.Tech CSE (AI) @ Amrita Vishwa Vidyapeetham, Coimbatore
Email: shruti.cbe@gmail.com  
GitHub: shruti-sivakumar

---

## 🛡️ Disclaimer

This repository is a sanitized version of the original internship deliverable. Some components are mocked or simplified to avoid disclosure of proprietary data, model weights, or internal configurations.
