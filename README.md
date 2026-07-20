# Decodeab-GenAi-Week2
# ✍️ Copywriter AI: Tone Transformer

An interactive, Streamlit-based web application that leverages the Google GenAI SDK to transform raw product technical specifications into highly engaging, platform-optimized marketing copy.

---

## 🚀 Features

* **Platform Optimization:** Tailors copy lengths, formatting, and styles specifically for Instagram, LinkedIn, Facebook, Email Campaigns, TikTok, or Google Ads.
* **Tone Control:** Dynamically adjusts the messaging voice (e.g., Witty, Professional, Visionary, Bold).
* **Advanced Model Tuning:** Exposes fine-grained control over `Temperature` (creativity) and `Top P` via expandable UI sliders.
* **Clean GUI Layout:** Uses multi-column layouts, intuitive text areas, and non-blocking session runs for an optimized desktop workflow.

---

## 🛠️ Tech Stack & Requirements

* **Python 3.10+**
* **Streamlit** (Web UI Framework)
* **google-genai** (Official Google AI SDK)
* **python-dotenv** (Environment variable management)

---

## 📦 Installation & Setup

### 1. Clone or Move to the Project Directory
Ensure you are operating inside your root project folder:

`cd Decodelabs`

### 2. Set Up a Virtual Environment (Recommended)

```
python -m venv venv
# Activate on Windows:
.\venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
Install the required packages using `pip`:

`pip install streamlit google-genai python-dotenv`

### 4. Environment Configuration
Create a `.env` file directly in the root directory. Add your Gemini API key precisely as follows:
`GEMINI_API_KEY=your_actual_api_key_here`


### 🖥️ Running the Application
Launch the interactive graphical interface by executing the following command in your activated terminal:

`streamlit run app.py`

Streamlit will spin up a local development server and automatically open the application interface in your default web browser (typically at `http://localhost:8501`).
