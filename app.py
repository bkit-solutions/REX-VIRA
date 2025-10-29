import streamlit as st
import requests
import json
import re # Keep re for consistency, though less critical now

st.set_page_config(
    page_title="Fake News Fact-Checker",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for website-style layout and animations
st.markdown(
    """
    <style>
    /* General body & background */
    .block-container {
        padding: 2rem 3rem 4rem 3rem;
        max-width: 900px;
        margin: auto;
        background: linear-gradient(135deg, #232631 0%, #1a1f2d 100%);
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(75, 225, 236, 0.15);
        color: #e5e6e7;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Header styling */
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 3rem;
        border-bottom: 1px solid #323642;
        padding-bottom: 1rem;
    }
    header h1 {
        font-size: 2.7rem;
        color: #4be1ec;
        margin: 0;
    }
    /* Nav links */
    nav a {
        color: #4be1ec;
        margin-left: 2rem;
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s ease;
    }
    nav a:hover {
        color: #67fff9;
    }
    /* Hero section */
    .hero {
        text-align: center;
        margin-bottom: 3rem;
        animation: fadeIn 1s ease forwards;
    }
    .hero h2 {
        font-size: 1.9rem;
        margin-bottom: 0.2rem;
    }
    .hero p {
        font-size: 1.15rem;
        color: #b0beca;
    }
    /* Input Card */
    .input-card {
        background: #2d3242;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 0 8px rgba(75, 225, 236, 0.25);
        margin-bottom: 2rem;
    }
    textarea.css-1cpxqw2 {
        background-color: #1d2333 !important;
        color: #e0e0e0 !important;
        border-radius: 10px !important;
    }
    /* Button styling */
    .stButton button {
        background-color: #4be1ec;
        color: #0c0c0c;
        font-weight: 700;
        padding: 0.5rem 1.3rem;
        border-radius: 12px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #67fff9;
    }
    /* Result section (updated styling to look clean with st.markdown) */
    .result-content {
        background: #1c2233;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: inset 0 0 15px #4be1ec5e;
        white-space: pre-wrap;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Footer styling */
    footer {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #505f79;
        border-top: 1px solid #323642;
        padding-top: 1rem;
    }
    /* FadeIn Animation */
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header (custom html)
st.markdown(
    """
    <header>
        <h1>Fake News <span style='color:#67fff9;'>Fact-Checker</span></h1>
        <nav>
            <a href='#'>Home</a>
            <a href='#about'>About</a>
            <a href='#contact'>Contact</a>
        </nav>
    </header>
    """,
    unsafe_allow_html=True,
)

# Hero section
st.markdown(
    """
    <section class='hero'>
        <h2>Your real-time news fact-checking companion</h2>
        <p>Powered by Gemini AI and Google Search for accurate misinformation detection</p>
    </section>
    """,
    unsafe_allow_html=True,
)

# API config
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
GEMINI_API_KEY = "AIzaSyBk-4WTw4txv44GCXhfY4Hbp2OEMgbsRaU"

def call_gemini_api(text):
    """
    Calls the Gemini API, ensuring the response is structured using Markdown 
    for easy display as points in Streamlit.
    """
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY
    }
    
    # MODIFIED: Updated the prompt to explicitly ask for a list/points using Markdown
    prompt_instruction = (
        "Analyze the following text for factual accuracy and potential misinformation. "
        "Identify the key claim and use Google Search to verify it. "
        "Your response MUST be formatted using Markdown headings (**Key Claim:**, **Fact Check:**, **Conclusion:**) and bullet points (*) for all explanations and details. "
        f"Text to analyze: {text}"
    )
    
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt_instruction # Use the structured prompt
                    }
                ]
            }
        ],
        "tools": [
            {
                "google_search": {}
            }
        ]
    }
    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=data, timeout=20)
        response.raise_for_status()
        resp_json = response.json()
        
        # Get the raw text response
        reply_text = resp_json.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        
        return reply_text
    except Exception as e:
        return f"❌ Error: Unable to contact Gemini API. Details: {e}"

# Input section
st.markdown("<div class='input-card'>", unsafe_allow_html=True)
st.markdown("#### Enter news headline or snippet for fact-checking:")
user_input = st.text_area("", height=130, placeholder="Paste news snippet here")

if st.button("Fact-Check Now 🕵️‍♂️"):
    if user_input.strip():
        with st.spinner("Fact-checking with Gemini AI..."):
            gemini_reply = call_gemini_api(user_input)
            
        st.markdown("---")
        st.markdown("<h3 style='color:#67fff9;'>Gemini Fact-Check Result:</h3>", unsafe_allow_html=True)
        
        # MODIFIED: Display the result using st.markdown inside a custom div.
        # This will interpret the Markdown (bolding, bullet points) generated by Gemini.
        st.markdown(f"<div class='result-content'>{gemini_reply}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter text to fact-check.", icon="⚠️")
        
st.markdown("</div>", unsafe_allow_html=True)

# About section
st.markdown(
    """
    <section id='about' style='margin-top: 3rem;'>
        <h2>About This Project</h2>
        <p>This web app uses the powerful Gemini AI language model combined with Google Search to detect fake news in real-time with detailed explanations and reliable fact-checking. Built using Python, Streamlit, and cutting-edge Google AI services.</p>
        <ul>
            <li><b>Real-time:</b> No static datasets, fact checks live.</li>
            <li><b>Explainable:</b> Receives detailed textual justification.</li>
            <li><b>Interactive UI:</b> Simple, modern, and responsive.</li>
            <li><b>Final Year Project:</b> Showcase your skills with this advanced app.</li>
        </ul>
    </section>
    """,
    unsafe_allow_html=True,
)

# Contact/ Footer
st.markdown(
    """
    <footer id='contact' style='margin-top: 3rem;'>
      <hr>
      <p>Developed &copy; 2025 | Contact: <a href='mailto:your.email@example.com'>your.email@example.com</a></p>
      <p>GitHub: <a href='https://github.com/yourusername/fake-news-fact-checker' target='_blank'>fake-news-fact-checker</a></p>
    </footer>
    """,
    unsafe_allow_html=True,
)