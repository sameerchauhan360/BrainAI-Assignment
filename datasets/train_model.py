from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib
import pandas as pd
import os

# Load data
path = os.path.dirname(os.path.abspath(__file__))

data = pd.read_csv(os.path.join(path, "mental_health_dummy_data.csv"))

X = data.drop("Label", axis=1)
y = data["Label"]

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# Save model and label encoder
joblib.dump(model, os.path.join(path, "mental_health_model.pkl"))
joblib.dump(le, os.path.join(path, "label_encoder.pkl"))

print("Model trained and saved!")
