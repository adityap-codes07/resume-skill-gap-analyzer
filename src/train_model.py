import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import json

np.random.seed(42)

# Generate synthetic dataset (like your Image 3)
data = []
for _ in range(500):  # More data = better weights
    tech = np.random.randint(1, 11)
    comm = np.random.randint(1, 11)
    soft = np.random.randint(1, 11)
    exp  = np.random.randint(0, 6)

    score = 0.5*tech + 0.2*comm + 0.2*soft + 0.1*exp
    selected = 1 if score > 6 else 0
    data.append([tech, comm, soft, exp, selected])

df = pd.DataFrame(data, columns=["technical","communication","soft_skills","experience","selected"])

X = df[["technical","communication","soft_skills","experience"]].values
y = df["selected"].values

model = LogisticRegression()
model.fit(X, y)

# Extract normalized weights
raw_weights = model.coef_[0]
total = sum(abs(raw_weights))
normalized = {
    "technical":     round(abs(raw_weights[0]) / total, 2),
    "communication": round(abs(raw_weights[1]) / total, 2),
    "soft_skills":   round(abs(raw_weights[2]) / total, 2),
    "experience":    round(abs(raw_weights[3]) / total, 2),
}

print("Learned weights:", normalized)

# Save to a JSON file
with open("src/ml_weights.json", "w") as f:
    json.dump(normalized, f, indent=2)

print("Saved to src/ml_weights.json")