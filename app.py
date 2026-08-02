import streamlit as st
import re

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

from utils.pdf_reader import extract_text
import utils.gemini_api as gemini_api

# ================= Sidebar =================

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=100
    )

    st.title("AI Resume Analyzer")

    st.markdown("---")

    st.success("✔ Upload Resume")
    st.info("✔ ATS Analysis")
    st.warning("✔ Download ATS Report")

    st.markdown("---")

    st.write("### Tech Stack")
    st.write("🐍 Python")
    st.write("⚡ Streamlit")
    st.write("🤖 Groq Llama")
    st.write("📄 PyPDF2")

    st.markdown("---")

    st.caption("Developed by Sindhuja Gandreti")

# ================= Main =================

st.title("🤖 AI Resume Analyzer")
st.write("Upload your resume and get an AI-powered ATS analysis.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)
st.markdown("---")

job_description = st.text_area(
    "💼 Paste Job Description (Optional)",
    height=220,
    placeholder="Paste the job description here..."
)
if uploaded_file is not None:

    with st.spinner("Analyzing Resume..."):
        resume_text = extract_text(uploaded_file)
        result = gemini_api.analyze_resume(
    resume_text,
    job_description
)

    st.success("✅ Analysis Completed!")

    # -------- ATS Score --------

    match = re.search(r"ATS Score:\s*(\d+)", result)

    if match:
        score = int(match.group(1))
    else:
        score = 0

    st.subheader("📊 ATS Score")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.metric("Resume Score", f"{score}/100")

    with col2:
        st.progress(score / 100)

    if score >= 80:
        st.success("🟢 Excellent Resume")
    elif score >= 60:
        st.warning("🟡 Good Resume")
    else:
        st.error("🔴 Needs Improvement")

    st.markdown("---")

    st.subheader("📄 Detailed ATS Report")

    st.markdown(
        f"""
<div style="
padding:20px;
border-radius:15px;
background:#1f2937;
border-left:6px solid #4F8EF7;
box-shadow:0 4px 10px rgba(0,0,0,0.08);
white-space:pre-wrap;
font-size:16px;
color:white;
">

{result}

</div>
""",
        unsafe_allow_html=True
    )

    st.download_button(
        label="📥 Download ATS Report",
        data=result,
        file_name="ATS_Report.txt",
        mime="text/plain"
    )