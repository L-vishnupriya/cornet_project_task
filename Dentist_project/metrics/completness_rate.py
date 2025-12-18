import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

with open(os.path.join(BASE_DIR, "conversations", "Conversation1.txt"), encoding="utf-8") as f:
    gt_words = set(f.read().lower().split())

with open(os.path.join(BASE_DIR, "transcripts", "transcript_conversation1.txt"), encoding="utf-8") as f:
    pred_words = set(f.read().lower().split())

common = gt_words & pred_words
completeness = len(common) / len(gt_words) if gt_words else 1

print("Completeness Rate:", round(completeness, 2))
