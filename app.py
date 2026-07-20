import os
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

# RULE #1 FOR STREAMLIT: This MUST be the very first Streamlit command called!
st.set_page_config(
    page_title="Copywriter AI", 
    page_icon="✍️", 
    layout="centered"
)

# Load variables
load_dotenv()

# Check for API Key AFTER setting up the page configs safely
if not os.environ.get("GEMINI_API_KEY"):
    st.error("❌ GEMINI_API_KEY could not be found in your .env file.")
    st.stop()

# Initialize API Client safely
client = genai.Client()

# Header details
st.title("✍️ Copywriting & Tone Transformer")
st.caption("Transform raw product descriptions into high-converting marketing copy.")
st.markdown("---")

def generate_marketing_copy(product_name, platform, tone, raw_description, temperature, top_p):
    prompt = f"""
    You are an expert copywriter. Take the following raw product details 
    and transform them into highly engaging marketing copy optimized for the target platform.

    ---
    Product Name: {product_name}
    Target Platform: {platform}
    Desired Tone: {tone}
    Raw Description: {raw_description}
    ---

    Requirements:
    - Adhere strictly to the style norms, length limits, and features typical of {platform}.
    - Ensure the text perfectly reflects a {tone} voice.
    """

    config = types.GenerateContentConfig(
        temperature=temperature,
        top_p=top_p,
    )

    try:
        # 🔄 UPDATE THIS LINE TO THE CURRENT STABLE MODEL
        response = client.models.generate_content(
            model='gemini-3.5-flash',  
            contents=prompt,
            config=config
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# --- GUI INPUT SECTION ---
st.subheader("1. Campaign Details")
col1, col2 = st.columns(2)

with col1:
    product_name = st.text_input("Product Name", placeholder="e.g., CloudBreeze Everyday Tee")
    platform = st.selectbox(
        "Target Platform", 
        ["Instagram", "LinkedIn", "Facebook", "Email Campaign", "TikTok", "Google Ads"]
    )

with col2:
    tone = st.text_input("Desired Tone", placeholder="e.g., Witty, Professional, Bold")

raw_description = st.text_area(
    "Raw Product Description", 
    placeholder="Paste material specs, pricing, fit details, or features here...",
    height=150
)

st.markdown(" ")
with st.expander("⚙️ Advanced Model Tuning"):
    temperature = st.slider("Temperature (Creativity)", min_value=0.0, max_value=1.0, value=0.7, step=0.05)
    top_p = st.slider("Top P (Nucleus Sampling)", min_value=0.0, max_value=1.0, value=0.95, step=0.05)

st.markdown("---")

# --- EXECUTION SECTION ---
if st.button("🚀 Generate Marketing Copy", type="primary"):
    if not product_name or not raw_description:
        st.warning("⚠️ Please provide at least a Product Name and a Product Description.")
    else:
        with st.spinner("Analyzing parameters and writing copy..."):
            output_copy = generate_marketing_copy(
                product_name=product_name,
                platform=platform,
                tone=tone,
                raw_description=raw_description,
                temperature=temperature,
                top_p=top_p
            )
        
        st.subheader("✨ Generated Copy")
        st.info("You can copy the generated text directly below:")
        st.text_area("Output", value=output_copy, height=250)