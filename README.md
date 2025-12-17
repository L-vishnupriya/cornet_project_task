Dental Conversation Transcription & Evaluation
Project Overview:

This project focuses on generating, transcribing, and analyzing dental appointment conversations. It simulates a doctor-patient role play, records audio, transcribes it using Whisper v3 Large Turbo, and calculates various accuracy metrics on the transcripts.

The main goal is to evaluate the quality of automatic speech-to-text transcription in a medical/dental context using multiple metrics.

Project Structure
dentist_project/
│
├── audio/               # Recorded audio files of conversations
│   ├── audio_conversation1.wav
│   └── audio_conversation2.wav
├── code/          #convert conversation and audio into transcripts│           ├── transcribe_whisper.py
├── conversations/             # Generated dummy conversations
│   ├── Conversation1.txt
│   └── Conversation2.txt
│
├── transcripts/              # Transcripts generated from audio
│   ├── transcript_conversation1.txt
│   └── transcript_conversation2.txt
│
├── metrics/                 # calculate evaluation metrics
│   ├── medical_term_error_rate.py
│   ├── medication_dosage_accuracy.py
│   ├── numeric_accuracy.py
│   ├── wer.py
│   ├── negation_accuracy.py
│   ├── unit_accuracy.py
│   ├── sentence_diff.py
│   └── laterality_accuracy.py  
|   |___ cer.py
|
└── README.md                  

Steps:
1. Generate Conversations

Create dummy dental appointment conversations simulating a patient and doctor role-play.

Save the text files in the conversations/ folder.

2. Record Audio

Use TTS or read aloud the conversation.

Save the audio files in the audio/ folder.

3. Transcribe Audio

Use Whisper v3 Large Turbo (from Groq) to transcribe the recorded audio.

Save the transcripts in the transcripts/ folder.

4. Evaluate Transcripts

Run the Python scripts in the metrics/ folder to calculate:

Medical Terminology Error Rate

Medication & Dosage Accuracy

Numeric & Measurement Accuracy

Laterality & Directional Accuracy

Negation Detection Accuracy

Unit Accuracy

Sentence Count Difference

wer

cer

