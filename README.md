# Automated PDF-to-Structured-Analytics Pipeline

A high-performance, automated data engine designed to transform unstructured PDF documents into professionally structured, validated datasets. This pipeline integrates precisely with **PDFMiner** for extraction and **Pandas** for transformation, ensuring data integrity at every stage of the lifecycle.

## Fundamental Core Idea

This project provides a robust pipeline for:
- Converting unstructured PDF documents into structured datasets.
- Implementing advanced parsing and transformation using **Python (PDFMiner, Pandas)**.
- Extracting critical fields such as **Roles, Salaries, and Qualifications**.
- Designing and executing **Data Validation & Quality Checks**.
- Generating clean, production-ready **CSV, JSON, and Excel (Spreadsheet)** outputs for downstream analytics and reporting.

---

## Key Features & Capabilities

### 🛡️ Data Validation & Quality Checks
Every extraction is subject to a rigorous validation layer. The system performs:
- **Dataset Integrity Checks**: Verifies schema consistency and data types.
- **Pattern Matching**: Regex-based validation for emails, currency, and date formats.
- **AI-Assisted Quality Scoring**: Estimates confidence levels for every extracted field to flag potential manual reviews.

### 📜 Structured Specifications
Maintain and organize datasets using strictly defined specifications:
- **Standardized Formats**: Export data in perfectly formatted JSON, CSV, and Excel.
- **Enterprise Ready**: Designed for seamless integration with HRIS or BI tools.
- **Clear Documentation**: Every data point is mapped to a structured specification for traceability.

### 🤖 Automation & Developer Tools
Built for modern developers and analysts:
- **JavaScript/TypeScript Automation Scripts**: The pipeline generates ready-to-use scripts to automate common data cleaning, ingestion, and mapping tasks.
- **AI-Assisted Development**: Optimized for interoperability with AI development environments and modern IDEs.
- **Dataset Maintenance**: Tools to organize and maintain large-scale structured datasets over time.

---

## Tech Stack

- **Extraction Engine**: [PDFMiner.six](https://github.com/pdfminer/pdfminer.six)
- **Transformation Layer**: [Pandas](https://pandas.pydata.org/)
- **API Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Validation**: [Pydantic v2](https://docs.pydantic.dev/latest/)
- **Frontend**: Vanilla JavaScript / TypeScript (Modern Glassmorphic Dashboard)

---

## Getting Started

### 1. Prerequisites
- Python 3.10+
- Node.js (Optional, for Automation Scripts)
- A Groq API Key (for the AI extraction layer)

### 2. Installation
```bash
git clone https://github.com/Pranesh-1/Automated-PDF-to-Structured-Analytics-Pipeline.git
cd Automated-PDF-to-Structured-Analytics-Pipeline
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```
Open **http://localhost:8000** to access the dashboard and start the pipeline.

---

## Project Structure

```text
├── engine/                # Structured Extraction & Validation
│   ├── parser.py          # PDFMiner Integration
│   ├── schema.py          # Data Specifications
│   └── ai_extractor.py    # AI Transformation
├── static/                # Analytics Dashboard
│   ├── index.html         # Pipeline Interface
│   ├── styles.css         # Professional Styling
│   └── app.js             # Automation Script logic
├── app.py                 # API Entry Point
└── requirements.txt       # Dependencies
```
