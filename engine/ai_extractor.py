import os
from litellm import completion
from engine.schema import JobDescriptionSchema
import json

def get_job_description_from_text(text: str, model: str = "groq/llama-3.3-70b-versatile") -> JobDescriptionSchema:
    """Uses LLM (Default: Groq) to extract structured Job Description data from raw text."""
    
    if not text or len(text.strip()) < 10:
        raise ValueError("The extracted PDF text is too short or empty. The file might be a scanned image or corrupted.")
    
    prompt = f"""
    Extract the following information from the provided job description text.
    Return ONLY a JSON object that matches this schema:
    {{
        "job_title": "string",
        "company_name": "string",
        "location": "string",
        "experience_level": "string",
        "compensation": "string",
        "responsibilities": ["string"],
        "must_have_skills": ["string"],
        "bonus_points": ["string"],
        "contact_emails": ["string"],
        "confidence_score": 0.0 (float between 0 and 1)
    }}

    Rules:
    - If a field is not found, use null (for strings) or an empty list (for arrays).
    - For confidence_score, estimate how certain you are of the overall extraction.
    - Clean and normalize the data where possible.

    Job Description Text:
    ---
    {text}
    ---
    """

    try:
        # Groq specific configuration for LiteLLM
        response = completion(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        data = json.loads(response.choices[0].message.content)
        return JobDescriptionSchema(**data)
    except Exception as e:
        print(f"Error in AI extraction: {e}")
        # Return a shell or raise error depending on app logic
        raise

if __name__ == "__main__":
    # Test extraction with the Panthera JD snippet
    sample_text = """
    Job Title: Intern - JavaScript, Data Validation & AI-Assisted Development
    Location: Remote / Work From Home
    Experience: Final-year student / 0–1 year experience
    Compensation: Competitive internship stipend
    About the Role
    At Panthera Infotech, our products run on large...
    """
    try:
        result = get_job_description_from_text(sample_text)
        print(result.json(indent=2))
    except Exception:
        print("Set OPENAI_API_KEY to test.")
