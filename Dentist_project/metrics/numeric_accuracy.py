import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def extract_numbers(text):
    return set(re.findall(r"\b\d+\b", text))

# Read files with utf-8 encoding
with open(os.path.join(BASE_DIR, "conversations", "Conversation1.txt"), encoding="utf-8") as f:
    gt = f.read()

with open(os.path.join(BASE_DIR, "transcripts", "transcript_conversation1.txt"), encoding="utf-8") as f:
    pred = f.read()

gt_nums = extract_numbers(gt)
pred_nums = extract_numbers(pred)

matched = gt_nums.intersection(pred_nums)
accuracy = len(matched) / len(gt_nums) if gt_nums else 1

print("Numeric & Measurement Accuracy:", round(accuracy, 2))
