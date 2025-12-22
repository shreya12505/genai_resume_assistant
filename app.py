import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="GenAI Resume Assistant", layout="wide")

st.title("🚀 GenAI Resume Assistant")

# API key check
if os.getenv("OPENAI_API_KEY"):
    st.success("API Key loaded successfully ✅")
else:
    st.error("API Key not found ❌")
    st.stop()

# ----------------------------
# INPUT SECTION
# ----------------------------
st.header("📄 Resume Input")
resume_text = st.text_area("Paste your Resume here", height=250)

st.header("💼 Job Description Input")
jd_text = st.text_area("Paste Job Description here", height=250)

# ----------------------------
# ANALYSIS BUTTON
# ----------------------------
if st.button("Analyze Resume vs Job Description"):
    if resume_text.strip() == "" or jd_text.strip() == "":
        st.warning("Please paste both Resume and Job Description.")
    else:
        with st.spinner("Analyzing... Please wait ⏳"):
            prompt = f"""
You are an expert ATS resume evaluator.

Compare the following RESUME with the JOB DESCRIPTION.

Tasks:
1. Give Skill Match Percentage
2. List Missing Skills
3. Give 5 Resume Improvement Suggestions

RESUME:
{resume_text}

JOB DESCRIPTION:
{jd_text}

Output format:
Skill Match Percentage:
Missing Skills:
Resume Improvement Suggestions:
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )

            st.subheader("📊 Analysis Result")
            st.write(response.choices[0].message.content)