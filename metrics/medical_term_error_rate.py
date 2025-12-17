import os

# Get the base directory (two levels up from this file)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# List of medical terms to check
MEDICAL_TERMS = [
    "abscess", "infection", "root canal",
    "periodontitis", "gingivitis",
    "pulp", "necrotic", "anesthesia"
]

# Read the ground truth and predicted transcript files with utf-8 encoding
with open(os.path.join(BASE_DIR, "conversations", "Conversation1.txt"), encoding="utf-8") as f:
    gt = f.read().lower()

with open(os.path.join(BASE_DIR, "transcripts", "transcript_conversation1.txt"), encoding="utf-8") as f:
    pred = f.read().lower()

# Find medical terms that are present in ground truth but missing in prediction
missing = [term for term in MEDICAL_TERMS if term in gt and term not in pred]

# Calculate error rate
error_rate = len(missing) / len(MEDICAL_TERMS)

print("Medical Terminology Error Rate:", round(error_rate, 2))
print("Missing Terms:", missing)
