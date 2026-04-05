# 🎥 YT Summarizer Pro

> Convert any YouTube video into a **professional article** and a **downloadable website** using AI 🚀

---

## 📌 Overview

**YT Summarizer Pro** is an AI-powered web application that takes a YouTube video URL as input and automatically:

* Extracts the video transcript
* Summarizes the content intelligently
* Generates a structured, professional article
* Converts the article into a fully functional website (HTML, CSS, JS)
* Allows users to download the website as a ZIP file

---

## ⚙️ Tech Stack

* **Frontend/UI**: Streamlit
* **Backend Logic**: Python
* **Framework**: LangChain
* **LLMs Used**:

  * ⚡ Groq (LLaMA 3.3) → Fast chunk summarization
  * ✨ Google Gemini → Article + Website generation
  * zipfile (for packaging website files)
  * dotenv (for secure API key management)

---

## 🧠 How It Works

```text
YouTube URL
   ↓
Transcript Extraction (LangChain YouTube Loader)
   ↓
Text Chunking (RecursiveCharacterTextSplitter)
   ↓
Groq LLM → Summarizes each chunk
   ↓
Combine summaries
   ↓
Gemini LLM →
   • Generate professional article
   • Generate HTML + CSS + JS
   ↓
Streamlit UI →
   • Display article
   • Download website as ZIP
```

---

## ✨ Features

* 🎯 One-click YouTube summarization
* 🌍 Supports **Hindi & English videos** (if captions available)
* 🧠 Intelligent chunk-based summarization
* 📝 Generates **Medium-style professional articles**
* 🌐 Converts content into **ready-to-use websites**
* 📦 Download complete webpage as ZIP
* ⚡ Fast processing using Groq

---

## 📂 Project Structure

```
yt-summarizer-pro/
├── .env.example
├── .gitignore
├── app.py
├── processor.py
├── requirements.txt
├── README.md
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

---

## 🛠️ Installation & Setup (Local Machine)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/yt-summarizer-pro.git
cd yt-summarizer-pro
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate Virtual Environment

#### Windows:

```bash
venv\Scripts\activate
```

#### Mac/Linux:

```bash
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

### 6️⃣ Open in Browser

Streamlit will automatically open:

```
http://localhost:8501
```

---

## 🚀 Usage

1. Paste a YouTube video URL
2. Click **"Generate Content"**
3. Wait for processing
4. View generated article
5. Download website ZIP

---

## ⚠️ Limitations

* ❌ Requires **YouTube captions (subtitles)**
* ❌ Will not work for videos without transcripts
* ⚠️ Output format depends on LLM consistency

---

## 🔥 Future Improvements

* 🎤 Add Whisper for videos without captions
* 🌐 Multi-language output support
* 🎨 Enhanced UI (Tailwind / modern design)
* ☁️ Deploy as SaaS product
* 📊 Add SEO optimization

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a PR.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* LangChain
* Groq
* Google Gemini
* Streamlit

---

## 👨‍💻 Author

**Aliasgar Alihusain Adamji**

---

> ⭐ If you found this project useful, don’t forget to star the repo!
