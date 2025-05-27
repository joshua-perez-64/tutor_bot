import streamlit as st
import whisper
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.effects import normalize
import ollama
import os
import tempfile
import shutil

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "transcript" not in st.session_state:
    st.session_state.transcript = ""
if "transcription_complete" not in st.session_state:
    st.session_state.transcription_complete = False

# Streamlit app title
st.title("Lecture Transcription and Tutoring Chatbot")

# File uploader for MP3
uploaded_file = st.file_uploader("Upload an MP3 file", type=["mp3"])

# Function to check if FFmpeg is installed
def check_ffmpeg():
    return shutil.which("ffmpeg") is not None

# Function to convert MP3 to WAV and preprocess
def mp3_to_wav(mp3_file, status_placeholder):
    try:
        # Validate file size
        if mp3_file.size > 5 * 1024 * 1024 * 1024:  # 5GB limit
            st.error("File exceeds 5GB limit.")
            return None
        # Update status
        status_placeholder.text(f"Processing file: {mp3_file.name}, Size: {mp3_file.size} bytes")
        # Save MP3 to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_mp3:
            temp_mp3.write(mp3_file.read())
            temp_mp3_path = temp_mp3.name
            status_placeholder.text(f"Saved temp MP3: {temp_mp3_path}")
        # Check for FFmpeg
        if not check_ffmpeg():
            st.error("FFmpeg not found. Please install FFmpeg and ensure it's in your system PATH.")
            return None
        # Convert and preprocess audio
        status_placeholder.text("Converting MP3 to WAV...")
        audio = AudioSegment.from_mp3(temp_mp3_path)
        audio = audio.set_channels(1).set_frame_rate(16000)  # Mono, 16kHz
        audio = normalize(audio)  # Normalize volume
        wav_path = temp_mp3_path.replace(".mp3", ".wav")
        audio.export(wav_path, format="wav")
        status_placeholder.text(f"Converted to WAV: {wav_path}")
        # Clean up temporary MP3
        os.unlink(temp_mp3_path)
        return wav_path
    except Exception as e:
        st.error(f"Error converting MP3 to WAV: {str(e)}")
        return None

# Function to transcribe audio with Whisper
def transcribe_audio(wav_path, status_placeholder, progress_bar):
    try:
        model = whisper.load_model("base")  # Options: tiny, base, small, medium, large
        audio = AudioSegment.from_file(wav_path)
        # Chunk if audio >10 minutes
        if len(audio) > 10 * 60 * 1000:  # 10 minutes in milliseconds
            status_placeholder.text("Audio exceeds 10 minutes, splitting into chunks...")
            chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-40)
            transcript = ""
            total_chunks = len(chunks)
            for i, chunk in enumerate(chunks):
                chunk_path = f"temp_chunk_{i}.wav"
                chunk.export(chunk_path, format="wav")
                status_placeholder.text(f"Transcribing chunk {i+1}/{total_chunks}")
                progress_bar.progress((i + 1) / total_chunks)
                result = model.transcribe(chunk_path, language="en", suppress_tokens="")  # Enforce English
                transcript += result["text"] + " "
                os.unlink(chunk_path)
            return transcript.strip()
        else:
            status_placeholder.text("Transcribing audio...")
            progress_bar.progress(0.5)  # Halfway through single file
            result = model.transcribe(wav_path, language="en", suppress_tokens="")
            progress_bar.progress(1.0)
            return result["text"]
    except Exception as e:
        st.error(f"Whisper transcription error: {str(e)}")
        return f"Transcription failed: {str(e)}"

# Process uploaded file
if uploaded_file:
    with st.spinner("Processing MP3..."):
        # Create placeholders for status and progress
        status_placeholder = st.empty()
        progress_bar = st.progress(0)
        # Convert and transcribe
        wav_path = mp3_to_wav(uploaded_file, status_placeholder)
        if wav_path:
            transcript = transcribe_audio(wav_path, status_placeholder, progress_bar)
            st.session_state.transcript = transcript
            os.unlink(wav_path)
            # Clear placeholders
            status_placeholder.empty()
            progress_bar.empty()
            if not transcript.startswith("Transcription failed"):
                st.success("Transcription complete!")
                st.session_state.transcription_complete = True
                st.subheader("Transcript")
                st.write(transcript)
                # Save transcript to file with UTF-8 encoding
                with open("transcript.txt", "w", encoding="utf-8") as f:
                    f.write(transcript)
            else:
                st.error(transcript)
                st.session_state.transcription_complete = False

# Chat interface for tutoring
st.subheader("Tutoring Chat")
if not st.session_state.transcription_complete:
    st.info("Please upload and transcribe an MP3 file before asking questions.")
    user_input = None
else:
    user_input = st.text_input("Ask a question about the lecture content:")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Prepare system prompt with transcript
    system_prompt = (
        "You are a tutoring assistant for a lecture. The lecture transcript is provided below. "
        "Answer the user's question based on the transcript. If the question is not covered by the transcript, "
        "say: 'The transcript does not contain information relevant to this question.' "
        "Keep answers clear, concise, and accurate.\n\n"
        "Transcript:\n"
        f"{st.session_state.transcript}\n"
    )
    # Log system prompt for debugging
    print("System Prompt:\n", system_prompt)
    # Prepare messages for Ollama
    messages = [
        {"role": "system", "content": system_prompt},
        *st.session_state.messages
    ]
    try:
        # Call Ollama LLM
        with st.spinner("Generating response..."):
            response = ollama.chat(model="llama3:latest", messages=messages)
            assistant_response = response["message"]["content"]
            # Append assistant response
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    except Exception as e:
        st.error(f"Error with LLM: {str(e)}")
        assistant_response = "Sorry, I couldn't process your request."
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])