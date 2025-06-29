# NLP Projects – Visual Infomedia
**Internship Project by Shruti Sivakumar**  
**Duration:** 6 Weeks | **Domain:** Natural Language Processing (NLP), Applied Machine Learning  
**Organization:** Visual Infomedia

---

## 🔍 Overview

This repository contains two end-to-end NLP projects developed during a 6-week internship at Visual Infomedia. The projects address real-world text processing challenges using applied machine learning techniques and are deployed through an interactive web application built with **Streamlit**.

---

## 🧠 Projects

### 📄 1. Automated Data Extraction from Business Memos

An intelligent document processing system that transforms unstructured business memo text into structured data fields using fine-tuned language models. This system significantly improves business efficiency by automating manual data entry tasks and reducing processing time for document analysis workflows.

**Key Features:**
- Fine-tuned GPT-4o-mini with Pydantic schema validation
- Dual-model architecture with version-specific optimizations
- Streaming batch processing with Excel I/O integration
- Real-time progress tracking and comprehensive error handling
- Adaptive model selection based on processing requirements

**Technical Implementation:**
- **Models**: Fine-tuned GPT-4o-mini (Version 1 & 2)
- **Validation**: Pydantic models for data integrity
- **Processing**: Streaming architecture for large datasets
- **Output**: Structured Excel with 14 standardized fields

**Training Configuration:**
- **Epochs**: 4 | **Batch Size**: 8 | **Learning Rate Multiplier**: 0.07 | **Training Seed**: 37081049

**Model Performance:**
- **Version 1**: Optimized for general extraction tasks (final training loss: 0.058)
- **Version 2**: Enhanced for detailed field extraction with improved nuance handling
- **Field Extraction Accuracy**: 94.2%
- **Schema Compliance**: 99.1%

### 🏷️ 2. Multi-Label Keyword Classification System

A transformer-based classification system that automatically assigns relevant keywords to text from a comprehensive controlled vocabulary. This solution streamlines content categorization processes and enhances searchability across large document repositories.

**Key Features:**
- Custom DistilRoBERTa model trained on 95,000+ text samples
- Multi-label classification across 4,000+ keyword categories
- Advanced training techniques: weighted loss functions and label smoothing
- Confidence-based predictions with visual feedback
- Fallback mechanisms for edge cases

**Technical Implementation:**
- **Architecture**: DistilRoBERTa with custom classification head
- **Training**: Multi-label binary cross-entropy with class weighting
- **Inference**: Confidence thresholding with fallback to top prediction
- **Visualization**: Color-coded confidence levels (Green/Yellow/Red)

**Performance Metrics:**
- **Hamming Loss**: 0.0004 (excellent multi-label performance)
- **Jaccard Score**: 0.305 | **F1-Score (Micro)**: 0.356 | **F1-Score (Weighted)**: 0.251
- **Precision (Micro)**: 0.415 | **Recall (Micro)**: 0.312
- **Coverage Rate**: 98.3%

---

## 💻 Application Architecture

The system is deployed as a multi-page Streamlit application providing comprehensive document processing capabilities:

**User Experience Design:**
- **Streamlined Workflow**: Upload → Configure → Process → Download with intuitive progress tracking
- **Real-time Monitoring**: Dynamic progress indicators with detailed status updates
- **Input Validation**: Multi-stage format verification with error reporting
- **Professional Output**: Formatted Excel exports with preserved styling

**Technical Infrastructure:**
- **Modular Design**: Separate processing engines for each task
- **Memory Optimization**: Streaming processing architecture for large datasets
- **Error Resilience**: Comprehensive exception handling with graceful degradation
- **API Integration**: Seamless integration with rate limiting and retry mechanisms

> **Note**: Due to proprietary model weights and API dependencies, the application is configured for internal deployment. This repository contains a demonstration version with abstracted components.

---

## 📁 Project Structure

```
streamlit-nlp/
│
├── model_artifacts/               # Trained model files for multi-label classification
├── main.py                        # Streamlit application entry point
├── pages/
│   ├── data_extraction.py         # Memo parsing interface
│   └── keyword_tagging.py         # Keyword classification interface
│
├── memo_parser.py                 # Core memo extraction logic
├── keyword_tagger.py              # Multi-label classification engine
├── requirements.txt               # Python dependencies
├── .streamlit/secrets             # API keys and sensitive configuration
├── .gitignore                     # Version control exclusions
└── README.md                      # Project documentation
```

**Excluded Components:**
- model_artifacts/ - Proprietary trained model files
- .streamlit/secrets - API keys and sensitive configuration
- data/ - Training datasets and business data

---

## ⚙️ Local Development Setup

### Prerequisites
- Python 3.8+
- OpenAI API access
- 4GB+ RAM for model inference

### Installation Steps

1. **Clone Repository**
   ```bash
   git clone https://github.com/shruti-sivakumar/streamlit-nlp.git
   cd streamlit-nlp
   ```

2. **Environment Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   ```bash
   cp .streamlit/secrets
   # Edit .streamlit/secrets with required API keys and configurations
   ```

5. **Launch Application**
   ```bash
   streamlit run main.py
   ```

---

## 📦 Technology Stack

### Core Technologies
- **Python 3.10+** - Primary development language
- **Streamlit** - Web application framework
- **OpenAI GPT-4o-mini** - Language model fine-tuning and inference
- **HuggingFace Transformers** - DistilRoBERTa implementation

### Supporting Libraries
- **Pydantic** - Data validation and schema enforcement
- **Pandas** - Data manipulation and analysis
- **PyTorch** - Deep learning framework
- **Scikit-learn** - Machine learning utilities
- **OpenPyXL** - Excel file processing

---

## 🔄 Development Workflow

### Model Training Pipeline
1. **Data Preprocessing** - Text cleaning and normalization with domain-specific preprocessing
2. **Fine-tuning** - Custom training loops with validation and checkpointing
3. **Hyperparameter Optimization** - Learning rate scheduling and batch size tuning
4. **Performance Monitoring** - Real-time loss and accuracy tracking
5. **Model Evaluation** - Comprehensive metric analysis across multiple versions
6. **Deployment** - Model serialization and integration

### Quality Assurance
- Input validation and sanitization with comprehensive error handling
- Processing reliability with fallback mechanisms
- Performance monitoring and logging
- A/B testing between model versions
- User acceptance testing with iterative improvements

---

## 👩🏻‍💻 Author

**Shruti Sivakumar**  
B.Tech Computer Science & Engineering (Artificial Intelligence)  
Amrita Vishwa Vidyapeetham, Coimbatore

📧 **Email**: shruti.cbe@gmail.com  
🔗 **GitHub**: [@shruti-sivakumar](https://github.com/shruti-sivakumar)  
💼 **LinkedIn**: [shruti-sivakumar](https://linkedin.com/in/shrutisivakumar25)

---

## 🛡️ Legal & Ethical Considerations

### Data Privacy
- All training data has been anonymized and sanitized
- No personally identifiable information is retained
- Compliance with organizational data governance policies

### Intellectual Property
- This repository represents a demonstration version of the original work
- Proprietary model weights and training data are excluded
- Commercial applications require separate licensing agreements

### Disclaimer
This repository contains a sanitized version of the original internship deliverable. Components have been modified or mocked to prevent disclosure of proprietary information, including but not limited to:
- Internal model architectures and weights
- Training datasets and business logic
- API configurations and access credentials
- Organizational data and processes

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Note**: This license applies only to the demonstration code. Proprietary components and business logic remain under the intellectual property of Visual Infomedia.
