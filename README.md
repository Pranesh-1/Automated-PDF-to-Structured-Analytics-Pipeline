# AI JD Extractor & Validation Pipeline

A professional-grade, automated pipeline designed to transform unstructured PDF job descriptions into clean, structured, and validated datasets. Leveraging the power of **Groq (Llama-3.3-70b)** and **FastAPI**, this tool provides high-speed extraction with a modern **Human-in-the-Loop** validation interface.

## Key Features

- **Sub-Second Extraction**: Powered by Groq's high-performance AI models via LiteLLM.
- **Intelligent Schema Mapping**: Automatically identifies Job Titles, Companies, Salaries, Skills, and Responsibilities.
- **Glassmorphic UI**: A modern dashboard for reviewing extracted data side-by-side with the source document.
- **Data Validation**: Built-in Pydantic validation to ensure high-fidelity datasets (Emails, Lists, etc.).
- **Export Ready**: One-click export to CSV for downstream analytics and reporting.

---

## Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **AI Engine**: [Groq](https://groq.com/) (Llama-3.3-70b-versatile) via [LiteLLM](https://github.com/BerriAI/litellm)
- **PDF Parser**: [PyMuPDF (Fitz)](https://pymupdf.readthedocs.io/en/latest/)
- **Validation**: [Pydantic v2](https://docs.pydantic.dev/latest/)
- **Frontend**: Vanilla JavaScript + modern CSS (Glassmorphism)

---

## Getting Started

### 1. Prerequisites
- Python 3.9+
- A Groq API Key

### 2. Installation
```bash
git clone https://github.com/Pranesh-1/Automated-PDF-to-Structured-Analytics-Pipeline.git
cd Automated-PDF-to-Structured-Analytics-Pipeline
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_gsk_key_here
```

### 4. Run the Application
```bash
python app.py
```
Open **http://localhost:8000** in your browser to start extracting.

---

## Project Structure

```text
├── engine/                # Core Extraction Logic
│   ├── parser.py          # PDF Text Extraction
│   ├── schema.py          # Pydantic JD Models
│   └── ai_extractor.py    # AI Integration Layer
├── static/                # Modern Frontend
│   ├── index.html         # Dashboard
│   ├── styles.css         # Styling
│   └── app.js             # Logic
├── uploads/               # Temporary file storage
└── app.py                 # FastAPI Entry Point
```

---

## License
Distributed under the MIT License. See `LICENSE` for more information.

---

## Contact
Shahrukh - [shahrukh@pantherainfotech.com](mailto:shahrukh@pantherainfotech.com)  
Admin - [admin@pantherainfotech.com](mailto:admin@pantherainfotech.com)
