# 👕 KidFit - Kids' Clothing Size Predictor

## 📘 Project Overview

**KidFit** is a machine learning web application that predicts a child's clothing size based on their height, weight, age, and gender. Built using **Python**, **Flask**, and **SVM (Support Vector Machine)**, it provides an easy-to-use interface for parents or retailers to determine ideal clothing sizes for kids.

---

## ✅ Features

- Predicts clothing size based on user input
- Real-time prediction using a trained SVM model
- Web interface developed using Flask and HTML
- Basic data visualization and model evaluation
- User-friendly form for input and instant output

---

## 🧠 Model Information

- **Algorithm**: SVM (Support Vector Classifier)
- **Input Features**: Height, Weight, Age, Gender
- **Target Variable**: Clothing Size
- **Preprocessing**:
  - Feature Scaling with `StandardScaler`
  - One-hot encoding for categorical feature (Gender)

---

## 🛠️ Technologies Used

| Component       | Description                  |
|----------------|------------------------------|
| Language        | Python                       |
| Web Framework   | Flask                        |
| ML Model        | Scikit-learn (SVM)           |
| Frontend        | HTML                         |
| Preprocessing   | Pandas, Scikit-learn         |
| Hosting         | Localhost / Flask Dev Server |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x
- pip (Python package installer)

### 📦 Installation

```bash
git clone https://github.com/chandnimaithil207/kidfit_web.git
cd kidfit_web
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` in your browser to access the web app.

---

## 📂 Project Structure

```
kidfit_web/
├── app.py                 # Main Flask application
├── index.html             # Frontend form interface
├── model.pkl              # Trained SVM model (optional)
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignored files
└── README.md              # Project description
```

---

## 👩‍💻 Author

**Chandni Maithil**  
GitHub: [@chandnimaithil207](https://github.com/chandnimaithil207)

---
