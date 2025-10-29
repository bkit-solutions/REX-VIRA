# 📰 Real-Time Explainable Fact Verification using Generative AI and Retrieval Augmentation (Powered by Gemini AI)

This is a real-time web application built with **Python** and **Streamlit** that utilizes the **Google Gemini API** and the integrated **Google Search Tool** for instant, evidence-based fact-checking of news snippets and headlines.

The goal of this project is to provide users with a quick, explainable verification of information by leveraging the power of large language models for complex analysis and real-time internet search for factual grounding.

---

## ✨ Features

* **Real-time Fact-Checking:** Verifies claims against the latest information available via Google Search.
* **Explainable Results:** Provides a detailed analysis of the claim, the evidence found, and a clear conclusion.
* **Structured Output:** Results are displayed in a clean, point-by-point format for easy reading.
* **Modern Web UI:** Built with Streamlit and custom CSS for a professional, dark-mode interface.
* **Tech Stack:** Python, Streamlit, `requests` library, and the Google Gemini API (`gemini-2.5-flash`).

---

## 🚀 Local Setup and Installation

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites

You'll need Python 3.9+ installed on your system.

### 2. Get Your Gemini API Key ⚠️

**This step is crucial.** The application will not work without a valid API key.

1.  Go to the **Google AI Studio** API Key Management page: [ai.google.dev/gemini-api/docs/api-key](https://ai.google.dev/gemini-api/docs/api-key)
2.  Click **"Create API Key"** and copy the generated key string.
3.  ***Important Security Note:*** **Do not** commit your API key directly to version control (like Git/GitHub).

### 3. Clone the Repository

```bash
git clone <your_repository_url>
cd fake_news_nlp
```

### 4. Create and Activate a Virtual Environment

It's best practice to use a virtual environment.

```bash
# Create the environment
python -m venv venv

# Activate the environment (on Windows)
.env\Scriptsctivate

# Activate the environment (on macOS/Linux)
source venv/bin/activate
```

### 5. Install Dependencies

You only need a few packages to run the app:

```bash
pip install streamlit requests
```

### 6. Configure the API Key

Open the main application file (e.g., `app.py`) and replace the placeholder key with your actual Gemini API Key from Step 2:

```python
GEMINI_API_KEY = "YOUR_PASTED_API_KEY_HERE"  # <-- REPLACE THIS VALUE
```

### 7. Run the Application

Execute the Streamlit app from your terminal:

```bash
streamlit run app.py
```

The app will launch in your web browser at [http://localhost:8501](http://localhost:8501).

---

## 🛑 API Key Safety Warning

For **final year projects** or **public repositories**, it is **HIGHLY RECOMMENDED** that you use environment variables or Streamlit Secrets instead of hardcoding the API key.

### Recommended Best Practice (Streamlit Secrets)

1. Create a file named `.streamlit/secrets.toml` in your project root directory.
2. Add your API key to that file:

```toml
# .streamlit/secrets.toml
GEMINI_API_KEY = "YOUR_PASTED_API_KEY_HERE"
```

3. In your Python code (`app.py`), change the key fetching logic to:

```python
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
```

4. Add `.streamlit/secrets.toml` to your `.gitignore` file to ensure it is never committed to GitHub.

---

## ⚙️ Project Files

| File/Folder | Description |
|--------------|-------------|
| `app.py` | The main Streamlit application script containing the UI and API logic. |
| `venv/` | Python Virtual Environment (contains project dependencies). |
| `app/` | (Optional) Folder containing modular app components. |
| `fake_news_nlp/` | (Optional) Jupyter Notebook or model files used for NLP experimentation. |
| `.git/` | Git version control directory. |
| `*.joblib` | Serialized Python objects (e.g., trained NLP models or vectorizers). |

---

👩‍💻 **Developed By:** Caleb (B.Tech Final Year - Data Science Specialization)
