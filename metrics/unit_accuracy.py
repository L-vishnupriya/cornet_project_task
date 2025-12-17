import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def extract_units(text):
    # Extract numbers with units like mg, milligrams, hours, days
    return set(re.findall(r"\b\d+\s?(mg|milligrams|hours|days)\b", text.lower()))

# List of file pairs (ground truth, predicted transcript)
pairs = [
    ("Conversation1.txt", "transcript_conversation1.txt"),
    ("Conversation2.txt", "transcript_conversation2.txt")
]

for gt_file, pred_file in pairs:
    # Read files with utf-8 encoding
    with open(os.path.join(BASE_DIR, "conversations", gt_file), encoding="utf-8") as f:
        gt_text = f.read()
    with open(os.path.join(BASE_DIR, "transcripts", pred_file), encoding="utf-8") as f:
        pred_text = f.read()

    gt_units = extract_units(gt_text)
    pred_units = extract_units(pred_text)

    accuracy = len(gt_units & pred_units) / len(gt_units) if gt_units else 1
    print(f"{gt_file} → Unit Accuracy: {accuracy:.2f}")
