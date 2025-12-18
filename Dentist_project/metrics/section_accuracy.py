import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECTION_HEADINGS = [
    "chief complaint",
    "diagnosis",
    "treatment plan",
    "prescription",
    "follow up"
]

with open(os.path.join(BASE_DIR, "conversations", "Conversation1.txt"), encoding="utf-8") as f:
    gt = f.read().lower()

with open(os.path.join(BASE_DIR, "transcripts", "transcript_conversation1.txt"), encoding="utf-8") as f:
    pred = f.read().lower()

gt_sections = [s for s in SECTION_HEADINGS if s in gt]
pred_sections = [s for s in SECTION_HEADINGS if s in pred]

correct = len(set(gt_sections) & set(pred_sections))
accuracy = correct / len(gt_sections) if gt_sections else 1

print("Section Heading Accuracy:", round(accuracy, 2))
