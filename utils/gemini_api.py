import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

print("✅ NEW gemini_api.py LOADED")
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume(resume_text, job_description=""):
    print("Job Description received:", job_description[:50])

    prompt = f"""
You are an expert ATS (Applicant Tracking System) Resume Analyzer.

Analyze the following resume.

Return your response in exactly this format:

ATS Score: <number out of 100>

Strengths:
- ...

Missing Skills:
- ...

Suggestions:
- ...

Recommended Job Roles:
- ...

Resume:

{resume_text}
"""

    # If a Job Description is provided
    if job_description.strip():

        prompt += f"""

Now compare the resume with the following Job Description.

Job Description:

{job_description}

Also include these sections:

Resume Match Score: <percentage>

Matching Skills:
- ...

Missing Keywords:
- ...

Final Recommendation:
- ...
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content