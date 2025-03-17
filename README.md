# Twilio Call Transcription & Summarization

## 📌 Overview
This project demonstrates a Python-based implementation for:
- Making an outbound call using Twilio.
- Recording the conversation.
- Transcribing the audio using OpenAI Whisper and vosk model.
  **Note: if you want to use vosk mode, you will have to download it first "vosk-model-small-en-us-0.15".
- Summarizing the transcription using Google Gemini AI.

## 🛠 Features
✅ Twilio API integration for making calls and recording audio.  
✅ Transcription using OpenAI Whisper.  
✅ AI-powered summarization using Google's Gemini API.  
✅ Simple setup and easy-to-use script.  

---

## 🚀 Getting Started

### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Twilio API credentials
- OpenAI Whisper
- Google Gemini API key
- FFmpeg (for Whisper)

### 2️⃣ Installation

Clone the repository:

```sh
git clone https://github.com/your-username/twilio-call-transcription.git
cd twilio-call-transcription

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the requirments:

```sh
pip install -r requirements.txt
```

### Project Structure
📁 twilio-call-transcription

 ┣ 📜 main.py
 
 ┣ 📜 .env
 
 ┣ 📜 requirements.txt
 
 ┣ 📜 README.md
 
 ┗ 📜 summary.json
