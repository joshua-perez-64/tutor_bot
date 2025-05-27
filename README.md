# TutorBot

TutorBot is a Streamlit-based application that converts audio files (MP3) into transcripts using Whisper and enables interactive tutoring conversations based on the transcribed content using Ollama.

## Overview

TutorBot processes audio inputs, generates accurate transcripts, and provides a chat interface to ask questions about the content. It’s ideal for educational purposes, such as transcribing lectures and engaging in Q&A sessions, as well as for note-taking or analyzing spoken content interactively.

## Prerequisites

To run TutorBot, ensure the following are installed:

- **Python 3.8+**: Required for running the application.
- **Ollama**: Install Ollama with the `llama3:latest` model. See [Ollama documentation](https://ollama.ai/) for setup. Note: This dependency may be updated in future releases.
- **FFmpeg**: Required for audio processing. Install FFmpeg and ensure it’s in your system PATH:
  - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) or [gyan.dev](https://www.gyan.dev/ffmpeg/builds/). Extract the archive and add the `bin` folder (containing `ffmpeg.exe`) to your system PATH. Verify with: `ffmpeg -version`.
  - **macOS**: Install via Homebrew: `brew install ffmpeg`.
  - **Linux**: Install via your package manager, e.g., `sudo apt update && sudo apt install ffmpeg` (Ubuntu/Debian). Verify with: `ffmpeg -version`.
- **Python Dependencies**: Install required packages listed in `requirements.txt`:
  ```bash
  pip install streamlit openai-whisper pydub ollama
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/joshua-perez-64/tutor_bot.git
   cd tutor_bot
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Ollama and pull the `llama3:latest` model:
   ```bash
   ollama pull llama3:latest
   ```
4. Ensure FFmpeg is installed and accessible in your system PATH (see Prerequisites).

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run tutorbot.py
   ```
2. Open the provided local URL (e.g., `http://localhost:8501`) in your browser.
3. Upload an MP3 file to transcribe.
4. View the transcript and ask questions about the content in the tutoring chat interface.

## Project Structure

- `tutorbot.py`: Main application script containing the Streamlit interface, audio processing, and tutoring logic.
- `requirements.txt`: Lists Python dependencies for easy installation.
- `.gitignore`: Ignores large files and folders (e.g., `ffmpeg` builds, `.conda`).

## Future Updates

- Support for additional language models or replacement of `llama3:latest`.
- Enhanced audio processing features, such as support for more audio formats.
- Improved conversation capabilities, including context-aware responses.

## Troubleshooting

- **FFmpeg Not Found**: Ensure FFmpeg is installed and in your system PATH. Run `ffmpeg -version` to verify.
- **Ollama Errors**: Confirm Ollama is running and the `llama3:latest` model is pulled.
- **Large File Issues**: If you encounter GitHub push errors, ensure no large files (e.g., `ffmpeg` binaries) are tracked. The `.gitignore` file prevents this.
