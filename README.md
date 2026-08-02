# 🤖 AI Resume Analyzer

An AI-powered ATS Resume Analyzer that evaluates resumes against job descriptions and provides intelligent feedback to improve resume quality and job matching.

## 📌 Overview

AI Resume Analyzer is a web application that uses Generative AI to analyze resumes. Users can upload their resume PDF and provide a job description to receive an ATS score, matching skills, missing keywords, improvement suggestions, and suitable job role recommendations.

## 🚀 Features

- 📄 Upload resume in PDF format
- 🔍 Extract text from resumes automatically
- 💼 Compare resume with job descriptions
- 📊 Generate ATS compatibility score
- 🧩 Identify matching skills and missing keywords
- 💡 Provide AI-powered resume improvement suggestions
- 🎯 Recommend suitable job roles
- ⚡ Interactive Streamlit-based interface

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend Framework:** Streamlit
- **AI Integration:** Groq Generative AI API
- **PDF Processing:** PyPDF
- **Environment Management:** python-dotenv
- **Version Control:** Git & GitHub

## 📂 Project Structure

```text
AI_Resume_Analyzer/
│
├── app.py                    # Main Streamlit application
├── requirements.txt          # Required Python packages
├── README.md                 # Project documentation
├── .gitignore                # Ignored files
│
├── assets/
│   └── resume_analyzer.png   # Application screenshot
│
└── utils/
    ├── __init__.py
    ├── pdf_reader.py         # PDF text extraction logic
    └── gemini_api.py         # AI analysis logic
```

# ⚙️ Installation & Setup

Follow these steps to run the project locally.

## 1. Clone the Repository

```bash
git clone https://github.com/Sindhupatnaik-2505/AI-Resume-Analyzer.git
```

## 2. Navigate to Project Folder

```bash
cd AI-Resume-Analyzer
```

## 3. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

## 4. Install Required Dependencies

```bash
python -m pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create a file named:

```
.env
```

inside the project folder.

Add your API key:

```env
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Groq API key.

## 6. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

## 🔄 How It Works

1. User uploads a resume PDF.
2. The application extracts text from the resume.
3. User provides a target job description.
4. AI analyzes the resume against job requirements.
5. The system generates:
   - ATS Resume Score
   - Matching Skills
   - Missing Keywords
   - Improvement Suggestions
   - Recommended Job Roles

## 📸 Application Screenshot

<img width="1527" height="504" alt="Screenshot 2026-08-02 150444" src="https://github.com/user-attachments/assets/738def2f-c91f-49af-bad5-4c2bff78c0e4" />

## 🎯 Future Enhancements

- Export ATS analysis report as PDF
- Add resume section-wise scoring
- Support multiple resume comparisons
- Improve keyword matching accuracy
- Add user authentication

## 👩‍💻 Author

**Sindhuja Gandreti**

GitHub:
https://github.com/Sindhupatnaik-2505
