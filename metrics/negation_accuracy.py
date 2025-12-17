import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

NEGATIONS = ["no", "not", "never", "without"]

# Read files with utf-8 encoding
with open(os.path.join(BASE_DIR, "conversations", "Conversation1.txt"), encoding="utf-8") as f:
    gt = f.read().lower()

with open(os.path.join(BASE_DIR, "transcripts", "transcript_conversation1.txt"), encoding="utf-8") as f:
    pred = f.read().lower()

# Extract negations present in ground truth and prediction
gt_neg = [n for n in NEGATIONS if n in gt]
pred_neg = [n for n in NEGATIONS if n in pred]

# Compute accuracy
correct = len(set(gt_neg).intersection(set(pred_neg)))
accuracy = correct / len(gt_neg) if gt_neg else 1

print("Negation Detection Accuracy:", round(accuracy, 2))
