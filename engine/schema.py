from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
import json

class JobDescriptionSchema(BaseModel):
    job_title: Optional[str] = Field(None, description="Official title of the position")
    company_name: Optional[str] = Field(None, description="Name of the hiring organization")
    location: Optional[str] = Field(None, description="Work location (e.g., Remote, On-site, Hybrid)")
    experience_level: Optional[str] = Field(None, description="Required experience (e.g., Junior, Senior, Intern)")
    compensation: Optional[str] = Field(None, description="Salary or stipend information")
    responsibilities: List[str] = Field(default_factory=list, description="List of key job responsibilities")
    must_have_skills: List[str] = Field(default_factory=list, description="Must-have technical or soft skills")
    bonus_points: List[str] = Field(default_factory=list, description="Preferred but not required skills")
    contact_emails: List[str] = Field(default_factory=list, description="Email addresses for application/queries")
    confidence_score: float = Field(0.0, ge=0.0, le=1.0, description="AI confidence in extraction quality")

    class Config:
        json_schema_extra = {
            "example": {
                "job_title": "Intern – JavaScript, Data Validation & AI-Assisted Development",
                "company_name": "Panthera Infotech",
                "location": "Remote / Work From Home",
                "experience_level": "Final-year student / 0–1 year experience",
                "compensation": "Competitive internship stipend",
                "responsibilities": ["Perform data validation", "Write automation scripts"],
                "must_have_skills": ["JavaScript", "React", "JSON"],
                "bonus_points": ["Node.js", "Git"],
                "contact_emails": ["admin@pantherainfotech.com"],
                "confidence_score": 0.95
            }
        }

class ExtractionResult(BaseModel):
    success: bool
    data: Optional[JobDescriptionSchema] = None
    error: Optional[str] = None
