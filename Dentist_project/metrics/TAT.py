from datetime import datetime

# Example timestamps (replace with real ones)
audio_start_time = datetime.strptime("10:00:00", "%H:%M:%S")
transcript_ready_time = datetime.strptime("10:07:30", "%H:%M:%S")

turnaround_time = (transcript_ready_time - audio_start_time).total_seconds()

print("Turnaround Time (seconds):", turnaround_time)
print("Turnaround Time (minutes):", round(turnaround_time / 60, 2))
