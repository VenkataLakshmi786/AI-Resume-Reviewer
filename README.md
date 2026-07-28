# 📄 AI Resume Reviewer

An AI-powered Resume Reviewer that analyzes resumes using Large Language Models (LLMs), evaluates ATS compatibility, compares resumes across multiple job roles, and generates a downloadable PDF report with personalized feedback.

---

## 🚀 Features

- 📄 Upload Resume in PDF format
- 🤖 AI-powered Resume Analysis using Groq LLM
- 📊 ATS Skill Match Score
- 🎯 Compare Resume Across Multiple Job Roles
- ✅ Detect Matching Skills
- ❌ Identify Missing Skills
- 💡 Personalized Resume Improvement Suggestions
- 📥 Download ATS Analysis Report as PDF
- 🖥️ Simple and Interactive Streamlit Interface

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Framework
- Streamlit

### AI & LLM
- Groq API
- LangChain

### PDF Processing
- PyPDF2
- ReportLab

### Environment Management
- Python Dotenv

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```text
AI-Resume-Reviewer/
│
├── app.py                 # Streamlit Application
├── parser.py              # Extract Text from Resume PDF
├── llm.py                 # Groq LLM Integration
├── prompts.py             # AI Prompt Templates
├── ats.py                 # ATS Score & Skill Matching
├── skills.py              # Job Role Skills Database
├── pdf_report.py          # PDF Report Generator
├── requirements.txt
├── README.md
├── .env
├── .gitignore
└── assets/
    ├── home.png
    ├── analysis.png
    └── report.png
```

---

## 📊 Supported Job Roles

- AI Engineer
- Machine Learning Engineer
- Generative AI Engineer
- Data Scientist
- Data Analyst
- Python Developer

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Reviewer.git
```

Move into the project directory

```bash
cd AI-Resume-Reviewer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📖 How It Works

1. Upload your Resume (PDF).
2. Select your target job role.
3. Click **Analyze Resume**.
4. The application:
   - Extracts text from the resume
   - Calculates ATS Skill Match
   - Compares the resume across multiple job roles
   - Uses Groq LLM to generate detailed feedback
5. Download the complete ATS Analysis Report as a PDF.

---

## 📊 ATS Analysis Includes

- Resume Summary
- ATS Skill Match Score
- Skills Found
- Missing Skills
- Resume Match Across Different Roles
- Strengths
- Weaknesses
- Resume Improvement Suggestions

---

## 📸 Screenshots

### Home Page

```
<img width="457" height="470" alt="home" src="https://github.com/user-attachments/assets/e3bd7372-9a46-4a56-b120-ce62de506741" />

```

---

### Resume Analysis

```
<img width="459" height="494" alt="analysis" src="https://github.com/user-attachments/assets/ac4ef166-f953-4454-a51d-a08307a1f77b" />

```

---

### PDF Report

```
<img width="449" height="497" alt="report" src="https://github.com/user-attachments/assets/49c09a63-5aad-480a-b8bb-6596158d353e" />

```

---


## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Large Language Models (LLMs)
- Prompt Engineering
- ATS Resume Evaluation
- LangChain Integration
- Streamlit Development
- PDF Text Extraction
- PDF Report Generation
- Modular Python Project Development
