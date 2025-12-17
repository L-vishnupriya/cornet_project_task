# Dental Conversation Transcription & Evaluation

A comprehensive project for transcribing dental appointment conversations using Whisper v3 Large Turbo and evaluating transcription quality through multiple medical-domain-specific accuracy metrics.

## Project Overview

This project simulates doctor-patient dental appointment conversations, records them as audio, transcribes the audio using Groq's Whisper v3 Large Turbo model, and evaluates the transcription quality using various metrics tailored for medical/dental contexts.

The main goal is to evaluate the quality of automatic speech-to-text transcription in a medical/dental context, focusing on accuracy of medical terminology, medications, measurements, and other critical information.

## Features

- **Audio Transcription**: Transcribe dental conversation audio files using Whisper v3 Large Turbo via Groq API
- **Comprehensive Metrics**: Evaluate transcription quality using multiple domain-specific metrics:
  - Word Error Rate (WER)
  - Character Error Rate (CER)
  - Medical Terminology Error Rate
  - Medication & Dosage Accuracy
  - Numeric & Measurement Accuracy
  - Laterality & Directional Accuracy
  - Negation Detection Accuracy
  - Unit Accuracy
  - Sentence Count Difference

##  Project Structure

```
dentist_project/
│
├── audio/                      # Recorded audio files of conversations
│   ├── audio_conversation1.wav
│   └── audio_conversation2.wav
│
├── code/                       # Transcription scripts
│   └── transcribe_whisper.py   # Main transcription script using Groq API
│
├── conversations/              # Ground truth conversation text files
│   ├── Conversation1.txt
│   └── Conversation2.txt
│
├── transcripts/                # Generated transcripts from audio
│   ├── transcript_conversation1.txt
│   └── transcript_conversation2.txt
│
├── metrics/                    # Evaluation metric scripts
│   ├── cer.py                  # Character Error Rate
│   ├── wer.py                  # Word Error Rate
│   ├── medical_term_error_rate.py
│   ├── medication_dosage_accuracy.py
│   ├── numeric_accuracy.py
│   ├── laterality_accuracy.py
│   ├── negation_accuracy.py
│   ├── unit_accuracy.py
│   └── sentence_diff.py
│
└── README.md
```

   ```

## Usage

### Step 1: Prepare Conversations

Create or place your dental appointment conversation text files in the `conversations/` folder. These serve as the ground truth for evaluation.

### Step 2: Record Audio

Record audio files of the conversations (using TTS or reading aloud) and save them in the `audio/` folder as:
- `audio_conversation1.wav`
- `audio_conversation2.wav`

### Step 3: Transcribe Audio

Run the transcription script from the `code/` directory:

```bash
cd code
python transcribe_whisper.py
```

This will:
- Read audio files from `../audio/`
- Transcribe them using Whisper v3 Large Turbo
- Save transcripts to `../transcripts/`

**Note:** Make sure the `GROQ_API_KEY` environment variable is set before running.

### Step 4: Evaluate Transcripts

Run the evaluation metrics from the `metrics/` directory:

```bash
cd metrics
python wer.py                    # Word Error Rate
python cer.py                    # Character Error Rate
python medical_term_error_rate.py
python medication_dosage_accuracy.py
python numeric_accuracy.py
python laterality_accuracy.py
python negation_accuracy.py
python unit_accuracy.py
python sentence_diff.py
```

Or run all metrics at once:
```bash
python wer.py && python cer.py && python medical_term_error_rate.py && python medication_dosage_accuracy.py && python numeric_accuracy.py && python laterality_accuracy.py && python negation_accuracy.py && python unit_accuracy.py && python sentence_diff.py
```

## 📊 Metrics Explained

- **WER (Word Error Rate)**: Measures the percentage of words incorrectly transcribed
- **CER (Character Error Rate)**: Measures the percentage of characters incorrectly transcribed
- **Medical Terminology Error Rate**: Checks for missing or incorrect medical terms
- **Medication & Dosage Accuracy**: Validates correct transcription of medications and their dosages
- **Numeric Accuracy**: Ensures numbers are transcribed correctly
- **Laterality Accuracy**: Checks for correct transcription of directional terms (left/right)
- **Negation Accuracy**: Validates correct transcription of negation words
- **Unit Accuracy**: Ensures measurement units are transcribed correctly
- **Sentence Count Difference**: Compares the number of sentences between ground truth and transcript

