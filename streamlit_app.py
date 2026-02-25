import streamlit as st
import requests

st.set_page_config(page_title="BuildAI Pro", layout="wide")

st.title("🏗 BuildAI Pro – AI Construction Intelligence")

query = st.text_input("Enter Construction Planning Query")

if st.button("Generate Professional Report"):

    prompt = f"""
You are a senior civil engineer and project consultant.

Generate a professional construction planning report.

STRICT RULES:
- Use bullet points only.
- Each line must start with "•"
- No paragraphs.
- Use section headings clearly.
- Make output technical and professional.
- Keep formatting clean.

STRUCTURE:

📌 PROJECT SUMMARY
• 

👷 MANPOWER REQUIREMENT
• 

💰 COST ESTIMATION
• 

📦 MATERIAL SPECIFICATIONS
• 

📅 EXECUTION TIMELINE
• 

⚠ RISK ANALYSIS
• 

📊 ROI & VALUE ANALYSIS
• 

User Request:
{query}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    output = result.get("response", "Error generating report.")

    st.markdown(output)