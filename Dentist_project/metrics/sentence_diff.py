import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def count_sentences(text):
    # Count sentences based on '.', '!', or '?'
    return len(re.findall(r"[.!?]", text))

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

    diff = abs(count_sentences(gt_text) - count_sentences(pred_text))
    print(f"{gt_file} → Sentence Count Difference: {diff}")
