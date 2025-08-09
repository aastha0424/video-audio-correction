# AI-Powered Video Audio Correction Pipeline

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated pipeline that extracts audio from a video, corrects the transcription using AI, generates new audio, and syncs it back to the video.

## 🌟 Overview

This project provides a complete solution to fix or replace imperfect audio in video files. If a video has background noise, mumbled speech, or grammatical errors in its narration, this tool can automatically generate a clean, studio-quality audio track and seamlessly merge it with the original video frames.

The core workflow is:
**Extract -> Transcribe -> Correct -> Generate -> Sync**

## ✨ Features

- **Audio Extraction**: Automatically separates the audio track from any input video file (`.mp4`).
- **AI Transcription**: Utilizes a speech-to-text model to convert spoken audio into a text script.
- **Text Correction**: (Optional but powerful) Cleans up the transcribed text, fixing grammar and punctuation.
- **Text-to-Speech (TTS)**: Generates a high-quality, clear voice-over from the corrected text.
- **Video-Audio Synchronization**: Replaces the original audio track with the newly generated one, creating a final, polished video.

## ⚙️ How It Works

The project is orchestrated by `main.py` and uses a series of modular scripts to perform each step of the pipeline:

1.  **`extract_audio.py`**: Takes `input_video.mp4` and extracts the audio, saving it as a separate file (e.g., `audio.wav`).
2.  **`transcribe_audio.py`**: Feeds the extracted audio into a speech-to-text model (like OpenAI's Whisper) to get a raw text transcription.
3.  **`correct_transcription.py`**: Takes the raw text and uses a language model (like GPT) to correct any errors, improving clarity and flow.
4.  **`generate_audio.py`**: Uses a Text-to-Speech (TTS) engine (like gTTS or ElevenLabs) to convert the corrected text back into an audio file.
5.  **`sync_audio_video.py`**: Takes the original video (without its audio) and the newly generated audio track and merges them into a final output video (`output_video.mp4`).
