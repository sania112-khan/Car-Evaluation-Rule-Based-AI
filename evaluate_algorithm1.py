
import csv
from pathlib import Path
from algorithm1 import classify_car

# Load the dataset
file_path = Path(__file__).parent / "data" / "car.data"

with open(file_path, "r") as file:
    data = list(csv.reader(file))

# Define the four categories
classes = ["unacc", "acc", "good", "vgood"]

correct = 0
predictions = []

# Test all 1728 cars
for row in data:

    if len(row) != 7:
        continue

    # Get the actual classification
    actual = row[6]

    # Predict using Algorithm 1
    predicted = classify_car(*row[:6])

    predictions.append((actual, predicted))

    if actual == predicted:
        correct += 1

# Calculate accuracy
total = len(predictions)
incorrect = total - correct
accuracy = (correct / total) * 100

print("ALGORITHM 1 - PERFORMANCE RESULTS")
print("---------------------------------")
print("Total cars tested:", total)
print("Correct predictions:", correct)
print("Incorrect predictions:", incorrect)
print("Accuracy:", round(accuracy, 2), "%")

# Calculate precision, recall and F1-score
all_precision = []
all_recall = []
all_f1 = []

print("\nCLASSIFICATION METRICS")
print("---------------------------------")

for category in classes:

    tp = sum(1 for a, p in predictions
             if a == category and p == category)

    fp = sum(1 for a, p in predictions
             if a != category and p == category)

    fn = sum(1 for a, p in predictions
             if a == category and p != category)

    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0

    f1 = (2 * precision * recall / (precision + recall)
          if precision + recall else 0)

    all_precision.append(precision)
    all_recall.append(recall)
    all_f1.append(f1)

    print("\nCategory:", category)
    print("Precision:", round(precision, 3))
    print("Recall:", round(recall, 3))
    print("F1-score:", round(f1, 3))

# Calculate macro averages
print("\nMACRO AVERAGES")
print("---------------------------------")

print("Precision:",
      round(sum(all_precision) / len(classes), 3))

print("Recall:",
      round(sum(all_recall) / len(classes), 3))

print("F1-score:",
      round(sum(all_f1) / len(classes), 3))
