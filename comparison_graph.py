
import matplotlib.pyplot as plt

# Performance results of both algorithms
metrics = ["Accuracy", "Macro Precision", "Macro Recall", "Macro F1-score"]

algorithm1 = [71.88, 60.1, 39.6, 41.1]
algorithm2 = [42.71, 46.1, 55.1, 41.4]

# Create the graph
x = range(len(metrics))
width = 0.35

plt.figure(figsize=(10, 6))

plt.bar([i - width/2 for i in x], algorithm1,
        width, label="Algorithm 1")

plt.bar([i + width/2 for i in x], algorithm2,
        width, label="Algorithm 2")

plt.xlabel("Performance Metrics")
plt.ylabel("Score (%)")
plt.title("Comparison of Rule-Based AI Algorithms")
plt.xticks(list(x), metrics)
plt.ylim(0, 100)
plt.legend()

plt.tight_layout()

# Save the graph
plt.savefig("algorithm_comparison.png")

plt.show()

