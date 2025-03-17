import os
import requests
from twilio.rest import Client
import google.generativeai as genai
from vosk import Model, KaldiRecognizer
import wave
import json
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
google_api_key = os.getenv("GOOGLE_API_KEY")

print("Account SID:", account_sid)
print("Auth Token:", auth_token)


twilio_client = Client(account_sid, auth_token)

# Google Generative AI
genai.configure(api_key=google_api_key)

# Mocking the call recording
def mock_call_recording():
    audio_file_path = "output.wav"
    return audio_file_path

# Transcribing
def transcribe_with_vosk(audio_file_path):
    # Using the Vosk model for 
    model_path = "vosk-model-small-en-us-0.15"  
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Vosk model not found at {model_path}. Please download and extract the model.")

    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    wf = wave.open(audio_file_path, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
        raise ValueError("Audio file must be WAV format, mono, 16-bit, and 16kHz.")

    transcript = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            transcript += result.get("text", "") + " "

    result = json.loads(recognizer.FinalResult())
    transcript += result.get("text", "")
    return transcript.strip()



# Summarizing the transcript using Google Generative AI
def summarize_call(transcript):
    # Initialize the Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # prompt template
    prompt = f"""
    You are a patient care AI. Summarize the call. 
    Provide the patient's name if mentioned, the reason for the call, 
    and any next steps. Return JSON with keys: patient_name, reason, next_steps.

    Transcript: {transcript}
    """

    response = model.generate_content(prompt)
    return response.text

def main():
    
    audio_file_path = mock_call_recording()


    transcript = transcribe_with_vosk(audio_file_path)
    print("Transcript:", transcript)

    summary = summarize_call(transcript)
    print("Summary:", summary)

    # Saving the summary to a file
    with open("summary.json", "w") as f:
        json.dump(summary, f, indent=4)
    print("Summary saved to 'summary.json'.")

if __name__ == "__main__":
    main()