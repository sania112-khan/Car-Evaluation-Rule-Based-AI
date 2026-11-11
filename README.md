# Car Evaluation Using Rule-Based AI Algorithms

## 1. Project Overview

This project focuses on designing and comparing two rule-based Artificial Intelligence (AI) algorithms for car evaluation.

The experiment uses the Car Evaluation Dataset to classify cars into four categories: unacceptable, acceptable, good and very good.

The project aims to compare the performance of two different rule-based approaches using Python.

## 2. Algorithms Used

**Algorithm 1: IF-THEN Rule-Based Algorithm**

This algorithm uses predefined IF-THEN conditions to classify cars based on their features, such as safety, passenger capacity, buying price and maintenance cost.

**Algorithm 2: Weighted Scoring Algorithm**

This algorithm assigns different points to car features. The total score determines the final car classification.

## 3. Dataset

The Car Evaluation Dataset was obtained from the UCI Machine Learning Repository.

It contains:
- 1,728 car records.
- Six input attributes.
- One classification attribute.
- Four output categories: unacc, acc, good and vgood.

## 4. Technologies Used

- Python
- Visual Studio Code
- Matplotlib
- CSV dataset

## 5. Project Files

- `main.py` – Main project file.
- `algorithm1.py` – IF-THEN rule-based algorithm.
- `algorithm2.py` – Weighted scoring algorithm.
- `evaluate_algorithm1.py` – Evaluates Algorithm 1.
- `evaluate_algorithm2.py` – Evaluates Algorithm 2.
- `confusion_matrix.py` – Generates confusion matrices.
- `comparison_graph.py` – Generates the performance comparison graph.
- `algorithm_comparison.png` – Saved comparison graph.
- `Data/car.data` – Dataset used in the experiment.

## 6. Performance Results

| Performance Measure | Algorithm 1 | Algorithm 2 |
|---|---:|---:|
| Accuracy | 71.88% | 42.71% |
| Macro Precision | 0.601 | 0.461 |
| Macro Recall | 0.396 | 0.551 |
| Macro F1-score | 0.411 | 0.414 |

Algorithm 1 achieved higher accuracy, while Algorithm 2 achieved slightly higher macro recall and macro F1-score.

## 7. How to Run the Project

1. Install Python.
2. Install Matplotlib using:

   `python -m pip install matplotlib`

3. Open the project folder in Visual Studio Code.
4. Run Algorithm 1:

   `python evaluate_algorithm1.py`

5. Run Algorithm 2:

   `python evaluate_algorithm2.py`

6. Generate confusion matrices:

   `python confusion_matrix.py`

7. Generate the comparison graph:

   `python comparison_graph.py`

## 8. Conclusion

This project demonstrates how two different rule-based AI approaches can be used for car classification. Their performance was evaluated and compared using accuracy, precision, recall, F1-score and confusion matrices.