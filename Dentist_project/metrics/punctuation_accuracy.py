import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def extract_end_punct(text):
    return re.findall(r"[.!?]", text)

with open(os.path.join(BASE_DIR, "conversations", "Conversation1.txt"), encoding="utf-8") as f:
    gt = f.read()

with open(os.path.join(BASE_DIR, "transcripts", "transcript_conversation1.txt"), encoding="utf-8") as f:
    pred = f.read()

gt_punct = extract_end_punct(gt)
pred_punct = extract_end_punct(pred)

matched = min(len(gt_punct), len(pred_punct))
accuracy = matched / len(gt_punct) if gt_punct else 1

print("Punctuation Accuracy (Critical Contexts):", round(accuracy, 2))
