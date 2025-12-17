
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

audio_files = {
    "../audio/audio_conversation1.wav": "../transcripts/transcript_conversation1.txt",
    "../audio/audio_conversation2.wav": "../transcripts/transcript_conversation2.txt"
}

for audio_path, output_path in audio_files.items():
    with open(audio_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3-turbo"

        )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcription.text)

    print(f"Saved transcript: {output_path}")
