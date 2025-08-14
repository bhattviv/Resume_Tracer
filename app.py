import streamlit as st
import pdfplumber
import os
from dotenv import load_dotenv
import google.generativeai as genai
from fpdf import FPDF

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")




st.markdown("---")
st.caption("💬 Powered by Google Gemini AI | Designed with ❤️ using Streamlit")

st.title("📄 AI Resume Analyzer")


# Extract Text from PDF 
def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def create_pdf(analysis, filename="resume_analysis.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, analysis)
    pdf.output(filename)

def analyze_resume(resume_text, job_desc):
    prompt = f"""
 You are an experienced HR with tech experience in field of any one job role from data science or data analytics or  devops or AI/ML or
Full stack or big data engineering,cyber security etc,your task is to review the provided resume against
the job description for these profiles 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
 You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of any one job role from data science,
data analytics, devops,AI/ML, and ATS functionality, Full stack,big data engineering,cyber security and deep 
ATS Functionality
your task is to evaluate the resume against the provided job description. give me the percentage of match if 
the resume matches
the job description. First the output should come as percentage and then keywords missing and last final  
thoughts.

Resume:
{resume_text}

Job Description:
{job_desc}

Provide:
- Matching Probability (%)
- Missing or related skills
- Project feedback and suggestions
- Resume improvement tips
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error during analysis: {e}"

# Form for Input 
with st.form("analyzer_form"):
    uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])
    job_description = st.text_area("Paste the Job Description here")
    submitted = st.form_submit_button("🔍 Start Analysis")

if submitted and uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("🔍 AI Analysis")
    with st.spinner("Analyzing resume with AI..."):
        analysis = analyze_resume(resume_text, job_description)
        st.markdown("### 📋 Analysis Result")
        st.markdown(analysis, unsafe_allow_html=True)

    # Download as .txt
    st.download_button("📥 Download as .txt", data=analysis, file_name="analysis.txt")

    # Download as PDF
    if st.button("📄 Download PDF Report"):
        create_pdf(analysis)
        with open("resume_analysis.pdf", "rb") as file:
            st.download_button("Download PDF", file, "resume_analysis.pdf", "application/pdf")
else:
    st.info("Please upload a resume and paste a job description to begin analysis.")

