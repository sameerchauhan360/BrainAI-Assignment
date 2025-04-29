# ✨ AI-Powered Mental Health Assessment & Recommendation System

## 📌 Project Overview

This project is an AI/ML-powered backend API designed to assess a user's mental health status using standardized psychological questionnaires and provide tailored recommendations based on predicted results. Built with Django and Django REST Framework, the API is part of a full-stack application that evaluates user responses and feeds insights to a frontend system responsible for personalized content delivery.

The system incorporates machine learning models trained to analyze user responses from assessments like PHQ-9 (Depression) and GAD-7 (Anxiety), offering a seamless mental health screening experience.

**Key Features:**
- RESTful APIs for receiving questionnaire inputs and returning predictions.
- ML-based classification for mental health status.
- Modular design to integrate easily with frontend recommendation engines.
- Scalable architecture for adding new assessments in the future.

**Technologies Used:**
- Python, Django, Django REST Framework
- scikit-learn, pandas, numpy
- Railway (for deployment)

> 🚀 **Live API URL**: [_[Add your deployed Railway URL here]_](https://brainai-project.up.railway.app/api/predict/)

> 🧠 Note: Recommendation logic is handled in the frontend. This repository is limited to ML-based prediction and API delivery.

## 🛠️ Setup Instructions

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/<your-username>/brainai-assignment.git](https://github.com/sameerchauhan360/BrainAI-Assignment.git)
cd brainai-assignment
```
### 2. Create and Activate a Virtual Environment
# On Windows
```
python -m venv venv
venv\Scripts\activate
```
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run Database Migrations
python manage.py migrate

### 5. Run the Server
python manage.py runserver

🧪 Notes:
This project uses SQLite3 as the default database.

ML model files (mental_health_model.pkl, label_encoder.pkl) are pre-trained and loaded during API calls.

The project is deployed via Railway [(add the live link if available).](https://brainai-project.up.railway.app/api/predict/)

## 📡 API Documentation

### 📍 Base URL
All endpoints are prefixed with:

http://<your-domain>/api/


### 🔮 `POST /api/predict/`

**Description:**  
Accepts user questionnaire responses and returns a predicted mental health status.

**Method:** `POST`  
**Content-Type:** `application/json`

**Request Body:**
```json
{
  "responses": [3, 2, 0, 1, 4, 2, 1, 3, 0, 2, 1, 0, 4, 3, 1, 2]
}
- responses: A list of 16 integer values representing answers to PHQ-9 and GAD-7 questions combined.

###Response:
{
    "mental_health_status": "Severe"
}

### Validation Errors:
{
  "error": "Invalid no. of responses. Expected 16."
}
🛑 Authentication
- No authentication is required for this endpoint.

🗂 Additional Notes:
- Predictions are based on a pre-trained ML model (mental_health_model.pkl) and use a label encoder (label_encoder.pkl).
- All responses are saved in the database via the AssessmentResponse model.
- Recommendations based on the prediction are handled by the frontend application, not this API.

## 🔐 Environment Variables

The project uses environment variables for configuration. Create a `.env` file in the root directory and add the following:

```env
SECRET_KEY=your-secret-key-here

## 🧠 ML Model Development & Training

The system uses a machine learning classification model to predict a user's mental health status based on their responses to 16 standardized questionnaire items (PHQ-9 + GAD-7).

### 🗂 Dataset

A synthetic dataset was created using NumPy for simulation purposes:

- **File:** `datasets/create_dataset.py`
- **Samples:** 200 simulated users
- **Features:** 16 questionnaire responses (`Q1` to `Q16`)
- **Labels:** One of `["Normal", "Mild", "Moderate", "Severe"]`

Output is saved in `datasets/mental_health_dummy_data.csv`.

---

### 🧪 Model Training

- **Algorithm Used:** Logistic Regression
- **Training Script:** `datasets/train_model.py`
- **Preprocessing:**
  - Label encoding (`LabelEncoder`) for categorical output
  - Train-test split (80/20)

```python
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
