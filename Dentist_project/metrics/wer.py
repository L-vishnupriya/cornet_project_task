from jiwer import wer
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

pairs = [
    ("Conversation1.txt", "transcript_conversation1.txt"),
    ("Conversation2.txt", "transcript_conversation2.txt")
]

for gt, pred in pairs:
    gt_path = os.path.join(BASE_DIR, "conversations", gt)
    pred_path = os.path.join(BASE_DIR, "transcripts", pred)

    with open(gt_path, "r", encoding="utf-8") as f:
        ground_truth = f.read()

    with open(pred_path, "r", encoding="utf-8") as f:
        prediction = f.read()

    score = wer(ground_truth, prediction)
    print(f"{gt} → WER: {score:.3f}")
