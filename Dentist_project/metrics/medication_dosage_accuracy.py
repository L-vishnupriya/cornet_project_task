import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MEDICATIONS = [
    ("amoxicillin", "500"),
    ("ibuprofen", "600"),
    ("acetaminophen", "500")
]

# Read files with utf-8 encoding
with open(os.path.join(BASE_DIR, "conversations", "Conversation1.txt"), encoding="utf-8") as f:
    gt = f.read().lower()

with open(os.path.join(BASE_DIR, "transcripts", "transcript_conversation1.txt"), encoding="utf-8") as f:
    pred = f.read().lower()

correct = 0
for med, dose in MEDICATIONS:
    if med in gt and med in pred and dose in pred:
        correct += 1

accuracy = correct / len(MEDICATIONS)

print("Medication & Dosage Accuracy:", round(accuracy, 2))
