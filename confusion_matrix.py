
import csv
from pathlib import Path

from algorithm1 import classify_car as algorithm1
from algorithm2 import classify_car as algorithm2

file_path = Path(__file__).parent / "Data" / "car.data"

with open(file_path, "r") as file:
    data = list(csv.reader(file))

classes = ["unacc", "acc", "good", "vgood"]

def create_matrix(algorithm):

    matrix = [[0 for _ in classes] for _ in classes]

    for row in data:

        if len(row) != 7:
            continue

        actual = row[6]
        predicted = algorithm(*row[:6])

        actual_index = classes.index(actual)
        predicted_index = classes.index(predicted)

        matrix[actual_index][predicted_index] += 1

    return matrix


def display_matrix(matrix, name):

    print("\n", name)
    print("Rows = Actual, Columns = Predicted")
    print()

    print("Actual/Pred", *classes, sep="\t")

    for i, row in enumerate(matrix):
        print(classes[i], *row, sep="\t")


matrix1 = create_matrix(algorithm1)
matrix2 = create_matrix(algorithm2)

display_matrix(matrix1, "ALGORITHM 1 CONFUSION MATRIX")
display_matrix(matrix2, "ALGORITHM 2 CONFUSION MATRIX")
