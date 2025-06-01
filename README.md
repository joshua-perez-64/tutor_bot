# TutorBot

TutorBot is a Streamlit-based application that converts audio files (MP3) into transcripts using Whisper and enables interactive tutoring conversations based on the transcribed content using Ollama.

## Overview

TutorBot processes MP3 audio inputs, generates accurate English transcripts, and provides a chat interface to ask questions about the transcribed content. It’s ideal for educational purposes, such as transcribing lectures and engaging in Q&A sessions, as well as for note-taking or analyzing spoken content interactively.

## Prerequisites

To run TutorBot, ensure the following are installed:

- **Python 3.8+**: Required for the application (Python 3.10 recommended for compatibility).
- **Conda**: For managing the Python environment. Install from [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- **Ollama**: Install Ollama with the `llama3:latest` model. See [Ollama documentation](https://ollama.ai/) for setup.
- **FFmpeg**: Required for audio processing. Ensure FFmpeg is in your system PATH:
  - **Windows**: Download from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) (e.g., `ffmpeg-release-essentials.zip`). Extract to `C:\ffmpeg` and add `C:\ffmpeg\bin` to system PATH. Verify: `ffmpeg -version`.
  - **macOS**: Install via Homebrew: `brew install ffmpeg`. Verify: `ffmpeg -version`.
  - **Linux**: Install via package manager, e.g., `sudo apt update && sudo apt install ffmpeg` (Ubuntu/Debian). Verify: `ffmpeg -version`.

## Installation

1. **Clone the Repository** (optional, if using a Git repository):
   ```bash
   git clone https://github.com/joshua-perez-64/tutor_bot.git
   cd tutor_bot
   ```
   Alternatively, save `tutorbot.py` and `requirements.txt` in a project directory.

2. **Create and Activate a Conda Environment**:
   Create a Conda environment named `tutorbot` with Python 3.10:
   ```bash
   conda create -n tutorbot python=3.10
   ```
   Activate the environment:
   ```bash
   conda activate tutorbot
   ```

3. **Install Python Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   streamlit
   openai-whisper
   pydub
   ollama
   numpy
   torch
   ```
   Save it in the project directory and install:
   ```bash
   pip install -r requirements.txt
   ```
   Alternatively, install dependencies directly:
   ```bash
   pip install streamlit openai-whisper pydub ollama numpy torch
   ```

4. **Install FFmpeg**:
   - **Windows**:
     1. Download FFmpeg from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
     2. Extract to a folder, e.g., `C:\ffmpeg`.
     3. Add `C:\ffmpeg\bin` to system PATH:
         - Open the Start menu, search for "Environment Variables," and select "Edit the system environment variables."
         - In the "System Properties" window, click "Environment Variables."
         - Under "System variables," find and edit `Path`, adding `C:\ffmpeg\bin`.
         - Click OK to save changes.
     4. Verify: `ffmpeg -version`.
   - **macOS**:
     Install Homebrew if not already installed:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
     Install FFmpeg:
     ```bash
     brew install ffmpeg
     ```
     Verify: `ffmpeg -version`.
   - **Linux (Ubuntu/Debian)**:
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```
     Verify: `ffmpeg -version`.
     For other Linux distributions, use the appropriate package manager (e.g., `yum` for CentOS, `dnf` for Fedora).

5. **Set Up Ollama**:
   Pull the `llama3:latest` model:
   ```bash
   ollama pull llama3:latest
   ```
   Start the Ollama server in a separate terminal (keep it running):
   ```bash
   ollama serve
   ```
   Verify the model is available:
   ```bash
   ollama list
   ```

## Usage

1. Ensure the Conda environment is activated:
   ```bash
<<<<<<< HEAD
   conda activate tutorbot
=======
   streamlit run tutorbot.py
>>>>>>> 1df0d5cb4469444302ffb30610a55cbb0f22d6d2
   ```
2. Run the Streamlit app from the project directory:
   ```bash
   streamlit run tutorbot.py
   ```
   To suppress optional `torch.classes` warnings in the terminal:
   ```bash
   streamlit run tutorbot.py --server.fileWatcherType=none
   ```
3. Open the provided URL (e.g., `http://localhost:8501`) in your browser.
4. Upload an MP3 file (up to 5GB) to transcribe.
5. Wait for the "Transcription complete!" message, then view the transcript.
6. Ask questions about the transcript in the tutoring chat interface (e.g., “What are the main topics discussed in the lecture?”).

## Project Structure

<<<<<<< HEAD
- `tutorbot.py`: Main application script containing the Streamlit interface, audio processing with Whisper, and tutoring logic with Ollama.
=======
- `tutorbot.py`: Main application script containing the Streamlit interface, audio processing, and tutoring logic.
>>>>>>> 1df0d5cb4469444302ffb30610a55cbb0f22d6d2
- `requirements.txt`: Lists Python dependencies for easy installation.
- `.gitignore`: Ignores large files and folders (e.g., FFmpeg builds, `.conda`, temporary audio files).

## Notes

- **Whisper Model**: The app uses the `base` Whisper model for transcription. For better accuracy, edit `tutorbot.py` to use `small` or `medium` models (requires more memory, e.g., 2GB+ for `small`).
- **System Requirements**: Ensure at least 4GB RAM for the `base` Whisper model and `llama3:latest`. More RAM (8GB+) is recommended for longer audio files or larger models.
- **Ollama Model**: The `llama3:latest` model requires the Ollama server to be running (`ollama serve`). Long transcripts may exceed the model’s token limit; consider shorter audio files for testing.
- **FFmpeg**: The app checks for FFmpeg in the system PATH using `shutil.which`. Ensure FFmpeg is installed correctly to avoid errors during MP3 processing.
- **Transcription**: The app enforces English-only transcription with noise reduction. For noisy audio, results may vary; test with clear recordings.

## Troubleshooting

<<<<<<< HEAD
- **FFmpeg Not Found**:
  - Verify FFmpeg is in your PATH: `ffmpeg -version`.
  - Reinstall FFmpeg and ensure the `bin` folder is added to PATH.
  - On Windows, restart your terminal or computer after updating PATH.
- **Ollama Errors**:
  - Ensure Ollama is running: `ollama serve`.
  - Verify `llama3:latest` is pulled: `ollama list`.
  - Check for sufficient RAM (4GB+ for `llama3:latest`).
- **Conda Environment Issues**:
  - Recreate the environment if dependencies fail:
    ```bash
    conda env remove -n tutorbot
    conda create -n tutorbot python=3.10
    pip install -r requirements.txt
    ```
  - Ensure the environment is activated: `conda activate tutorbot`.
- **Transcription Errors**:
  - Check MP3 file size (<5GB) and audio quality.
  - Test with a short, clear MP3 (e.g., 1-2 minutes).
  - If transcription fails, try a smaller Whisper model in `tutorbot.py`:
    ```python
    model = whisper.load_model("tiny")
    ```
- **LLM Not Using Transcript**:
  - Ensure transcription is complete before asking questions (wait for “Transcription complete!”).
  - If the LLM responds with “no lecture received,” check the terminal for the system prompt output.
  - For long transcripts, edit `tutorbot.py` to truncate:
    ```python
    truncated_transcript = st.session_state.transcript[:10000]
    ```
- **Streamlit Errors**:
  - Run with full traceback for debugging:
    ```bash
    python -m streamlit run tutorbot.py
    ```
  - Update Streamlit: `pip install --upgrade streamlit`.

## Future Updates

- Support for additional audio formats (e.g., WAV, M4A).
- Integration with other language models or cloud-based LLMs.
- Advanced audio preprocessing for noisy or low-quality inputs.
- Enhanced tutoring with context-aware responses and transcript search.

## Contributing

Contributions are welcome! Please submit issues or pull requests to the [GitHub repository](https://github.com/joshua-perez-64/tutor_bot). For major changes, open an issue first to discuss.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
=======
- **FFmpeg Not Found**: Ensure FFmpeg is installed and in your system PATH. Run `ffmpeg -version` to verify.
- **Ollama Errors**: Confirm Ollama is running and the `llama3:latest` model is pulled.
- **Large File Issues**: If you encounter GitHub push errors, ensure no large files (e.g., `ffmpeg` binaries) are tracked. The `.gitignore` file prevents this.
>>>>>>> 1df0d5cb4469444302ffb30610a55cbb0f22d6d2
