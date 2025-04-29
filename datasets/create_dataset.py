import pandas as pd
import numpy as np
import os

# Create dummy data
np.random.seed(42)

# 200 fake users
X = np.random.randint(0, 4, size=(200, 16))  # Answers: 0 to 3
y = np.random.choice(["Normal", "Mild", "Moderate", "Severe"], size=200)

# Create DataFrame
data = pd.DataFrame(X, columns=[f"Q{i+1}" for i in range(16)])
data["Label"] = y

# Save it
data.to_csv(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "mental_health_dummy_data.csv"
    ),
    index=False,
)
print("Dummy dataset created!")
