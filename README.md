**Author**
Chandni Maithil
GitHub: @chandnimaithil207
# 👕 KidFit - Kids' Clothing Size Predictor

KidFit is a machine learning web application that predicts a child's clothing size based on their **height**, **weight**, **age**, and **gender**. Built using **Python**, **Flask**, and **SVM (Support Vector Machine)**, it provides an easy-to-use interface for parents or retailers to determine ideal clothing sizes for kids.

---

# Features

- Predicts clothing size based on input values
- User-friendly web interface using Flask
- Real-time prediction from a trained SVM model
- Includes basic data visualization and model evaluation

---

# Project Structure

kidfit_web/
├── app.py # Flask app backend
├── kidfit.py # Model training and evaluation script
├── kids_clothing_svm_model.pkl # Trained model file
├── templates/
│ └── index.html # Web page form
├── children_clothing_data.csv # Dataset (if included)
├── requirements.txt # Required Python packages
└── README.md


**📈 Model Info**
Algorithm: SVM (Support Vector Classifier)

Features used: height, weight, age, gender

Target: size

Preprocessing: Scaling (StandardScaler), One-hot encoding for gender
