from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import shutil
import uuid
from dotenv import load_dotenv
from engine.parser import extract_text_from_pdf
from engine.ai_extractor import get_job_description_from_text
from engine.schema import ExtractionResult, JobDescriptionSchema

# Load Environment Variables
load_dotenv()

app = FastAPI(title="AI JD Extractor & Validator")

# Directories
UPLOADS_DIR = "uploads"
STATIC_DIR = "static"
os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)

# Mount static files for the frontend
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serves the main frontend page."""
    with open(os.path.join(STATIC_DIR, "index.html"), "r") as f:
        return f.read()

@app.post("/extract", response_model=ExtractionResult)
async def extract_job_description(file: UploadFile = File(...)):
    """Uploads a PDF, extracts text, and parses it into a structured JD."""
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOADS_DIR, f"{file_id}_{file.filename}")
    
    try:
        # Save the uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Extract raw text
        raw_text = extract_text_from_pdf(file_path)
        
        # AI Extraction
        # Priority: Groq (using provided key) -> OpenAI -> Fallback
        has_api_key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
        
        if not has_api_key:
            print("WARNING: No API key set. Using dummy data for demonstration.")
            return ExtractionResult(
                success=True,
                data=JobDescriptionSchema(
                    job_title="Sample: " + file.filename,
                    company_name="Extractor Demo",
                    location="Remote",
                    experience_level="0-1 year",
                    compensation="Competitive",
                    responsibilities=["Extracting data", "Validating fields"],
                    must_have_skills=["JavaScript", "React"],
                    bonus_points=["Git"],
                    contact_emails=["demo@example.com"],
                    confidence_score=0.8
                )
            )

        extracted_jd = get_job_description_from_text(raw_text)
        
        return ExtractionResult(success=True, data=extracted_jd)
        
    except Exception as e:
        print(f"Extraction failed: {e}")
        return ExtractionResult(
            success=False,
            error=str(e)
        )
    finally:
        # Keep file for now or delete if needed
        # os.remove(file_path) 
        pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
