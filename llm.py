import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from prompts import RESUME_REVIEW_PROMPT
from skills import JOB_SKILLS


# Load environment variables
load_dotenv()

# Create Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name=os.getenv("MODEL_NAME"),
    temperature=0.3
)

def ask_llm(prompt):
    """
    Send a prompt to the LLM and return the response.
    """
    response = llm.invoke(prompt)
    return response.content

def review_resume(resume_text, job_role):
    """
    Review the uploaded resume using the predefined prompt.
    """
    required_skills = JOB_SKILLS[job_role]

    prompt = RESUME_REVIEW_PROMPT.format(
    resume=resume_text,
    job_role=job_role,
    required_skills=", ".join(required_skills)
)

    response = llm.invoke(prompt)

    return response.content