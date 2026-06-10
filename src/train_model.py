import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import json
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

# Extract normalized weights
raw_weights = model.coef_[0]
total = sum(abs(raw_weights))
normalized = {
    "technical":     float(round(abs(raw_weights[0]) / total, 2)),
    "communication": float(round(abs(raw_weights[1]) / total, 2)),
    "soft_skills":   float(round(abs(raw_weights[2]) / total, 2)),
    "experience":    float(round(abs(raw_weights[3]) / total, 2)),
}

print("Learned weights:", normalized)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1:", f1_score(y_test, y_pred))

# Save to a JSON file
with open("src/ml_weights.json", "w") as f:
    json.dump(normalized, f, indent=2)

print("Saved to src/ml_weights.json")