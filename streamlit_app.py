import streamlit as st
import requests
import replicate
import os

# 🔹 PUT YOUR REPLICATE TOKEN HERE
os.environ["REPLICATE_API_TOKEN"] = "PASTE_YOUR_REPLICATE_TOKEN_HERE"

st.set_page_config(page_title="BuildAI Pro", layout="wide")

st.title("🏗 BuildAI Pro – AI Construction Intelligence")

# ---------------- TEXT GENERATION ---------------- #

st.subheader("Construction Planning AI")

user_input = st.text_input("Enter construction planning query")

if st.button("Generate Plan"):
    if user_input:
        with st.spinner("Generating plan..."):

            prompt = f"""
You are a professional construction planning AI.

STRICT RULES:
- Only bullet points.
- Each line must start with "•"
- No paragraphs.
- Keep points short and clean.

FORMAT:

🏗 PROJECT OVERVIEW
• ...
• ...

👷 WORKERS
• ...
• ...

💰 COST
• ...
• ...

📦 MATERIALS
• ...
• ...

📅 TIMELINE
• Week 1-2:
• Week 3-4:

⚠ RISKS
• ...
• ...

User Query:
{user_input}
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
            reply = result.get("response", "Error generating response.")

            st.markdown(reply)

# ---------------- IMAGE GENERATION ---------------- #

st.subheader("AI Building Visualization")

image_prompt = st.text_input("Describe building (e.g., Modern G+2 villa)")

if st.button("Generate Image"):
    if image_prompt:
        with st.spinner("Generating image..."):
            try:
                output = replicate.run(
                    "stability-ai/sdxl:da77bc59ee60423279fd632efb4795ab731d9e3ca9705ef3341091fb989b7eaf",
                    input={
                        "prompt": image_prompt,
                        "width": 768,
                        "height": 768
                    }
                )

                image_url = output[0]
                st.image(image_url)

            except Exception as e:
                st.error(str(e))