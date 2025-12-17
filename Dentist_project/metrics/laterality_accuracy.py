import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DIRECTIONS = ["left", "right", "upper", "lower"]

# Read files with utf-8 encoding
with open(os.path.join(BASE_DIR, "conversations", "Conversation1.txt"), encoding="utf-8") as f:
    gt = f.read().lower()

with open(os.path.join(BASE_DIR, "transcripts", "transcript_conversation1.txt"), encoding="utf-8") as f:
    pred = f.read().lower()

gt_dir = [d for d in DIRECTIONS if d in gt]
pred_dir = [d for d in DIRECTIONS if d in pred]

correct = len(set(gt_dir).intersection(set(pred_dir)))
accuracy = correct / len(gt_dir) if gt_dir else 1

print("Laterality & Directional Accuracy:", round(accuracy, 2))
