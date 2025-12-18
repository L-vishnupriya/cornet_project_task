import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CLINICAL_FLOW = [
    "pain",
    "diagnosis",
    "treatment",
    "medication",
    "follow up"
]

with open(os.path.join(BASE_DIR, "conversations", "Conversation1.txt"), encoding="utf-8") as f:
    gt = f.read().lower()

with open(os.path.join(BASE_DIR, "transcripts", "transcript_conversation1.txt"), encoding="utf-8") as f:
    pred = f.read().lower()

gt_steps = [step for step in CLINICAL_FLOW if step in gt]
pred_steps = [step for step in CLINICAL_FLOW if step in pred]

score = len(set(gt_steps) & set(pred_steps)) / len(gt_steps) if gt_steps else 1

print("Clinical Coherence Score:", round(score, 2))
