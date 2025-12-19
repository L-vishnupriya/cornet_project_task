import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Error categories with weights
ERROR_WEIGHTS = {
    "medication": 10,
    "dosage": 8,
    "medical_term": 5,
    "number": 3,
    "punctuation": 1
}

# Example detected error counts
error_counts = {
    "medication": 1,
    "dosage": 0,
    "medical_term": 2,
    "number": 1,
    "punctuation": 3
}

weighted_error_sum = sum(
    ERROR_WEIGHTS[err] * error_counts.get(err, 0)
    for err in ERROR_WEIGHTS
)

total_possible_weight = sum(ERROR_WEIGHTS.values())

weighted_error_rate = weighted_error_sum / total_possible_weight

print("Weighted Error Rate:", round(weighted_error_rate, 2))
