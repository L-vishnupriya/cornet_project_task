# Example metric scores (replace with actual outputs)
medical_term_accuracy = 0.80
ner_f1 = 0.75
numeric_accuracy = 0.90
negation_accuracy = 0.85

confidence_score = (
    medical_term_accuracy +
    ner_f1 +
    numeric_accuracy +
    negation_accuracy
) / 4

flag = "HIGH CONFIDENCE" if confidence_score >= 0.80 else "REVIEW REQUIRED"

print("Confidence Score:", round(confidence_score, 2))
print("Transcript Flag:", flag)
