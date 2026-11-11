
import csv
from pathlib import Path
from collections import Counter

# Load the dataset
file_path = Path(__file__).parent / "data" / "car.data"

with open(file_path, "r") as file:
    reader = csv.reader(file)
    data = list(reader)

# Give names to the columns
columns = [
    "Buying",
    "Maintenance",
    "Doors",
    "Persons",
    "Luggage",
    "Safety",
    "Evaluation"
]

# Count each car classification
categories = Counter(row[6] for row in data if len(row) == 7)

# Display the results
print("DATASET INFORMATION")
print("-------------------")

print("Total cars:", len(data))

print("\nCar classifications:")

for category, count in categories.items():
    percentage = (count / len(data)) * 100

    print(category, ":", count, "cars",
          "-", round(percentage, 2), "%")
