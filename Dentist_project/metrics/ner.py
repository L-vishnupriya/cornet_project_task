import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Dental domain entities (dictionary-based NER)
ENTITIES = [
    "tooth",
    "teeth",
    "gum",
    "gums",
    "abscess",
    "root canal",
    "cavity",
    "infection",
    "ibuprofen",
    "amoxicillin",
    "anesthesia"
]

# Read files safely with utf-8 encoding
with open(os.path.join(BASE_DIR, "conversations", "Conversation1.txt"), encoding="utf-8") as f:
    gt = f.read().lower()

with open(os.path.join(BASE_DIR, "transcripts", "transcript_conversation1.txt"), encoding="utf-8") as f:
    pred = f.read().lower()

# Extract entities
gt_entities = {e for e in ENTITIES if e in gt}
pred_entities = {e for e in ENTITIES if e in pred}

# True Positives, False Positives, False Negatives
tp = len(gt_entities & pred_entities)
fp = len(pred_entities - gt_entities)
fn = len(gt_entities - pred_entities)

# Precision, Recall, F1
precision = tp / (tp + fp) if (tp + fp) else 0
recall = tp / (tp + fn) if (tp + fn) else 0
f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0

print("NER Precision:", round(precision, 2))
print("NER Recall:", round(recall, 2))
print("NER F1 Score:", round(f1_score, 2))
