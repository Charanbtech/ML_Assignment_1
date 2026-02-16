# 🧠 Interactive Machine Learning Suite

> **A modern collection of web-based machine learning demonstrations.**
> Explore fundamental algorithms through clean, interactive interfaces.

---

## 🚀 Project Overview

This repository transforms traditional machine learning assignments into **interactive web applications**. instead of running scripts in a terminal, you can interact with the algorithms via a user-friendly dashboard.

The suite covers three core ML concepts:
1.  **📧 Spam Detective** (Concept Learning)
2.  **💸 Loan Risk Evaluator** (Decision Trees)
3.  **💻 Sales Predictor** (ID3 Algorithm)

---

## 📂 Application Modules

### 1. Spam Detective (Concept Learning)
**Algorithm:** Find-S  
**Goal:** Identifying spam emails based on patterns.  
**Features:**
- Train on a dataset of email features (Promotional words, Links, etc.).
- Interactive form to test new email characteristics.
- Visual feedback on classification.

### 2. Loan Risk Evaluator (Decision Tree)
**Algorithm:** Decision Tree with Information Gain  
**Goal:** Assessing credit risk for loan applicants.  
**Features:**
- Uses continuous attributes (Income, Credit Score).
- Implements Entropy and Information Gain logic.
- Instant "High Risk" vs. "Low Risk" prediction.

### 3. Sales Predictor (ID3)
**Algorithm:** ID3 (Iterative Dichotomiser 3)  
**Goal:** Predicting customer purchase behavior.  
**Features:**
- Analyzes demographics (Age, Income, Student Status).
- Traversable decision tree logic.
- Clean, responsive UI for testing scenarios.

---

## 🛠️ Tech Stack

- **Python 3.x**: Core logic and algorithm implementation.
- **Flask**: Lightweight web server for serving the apps.
- **Pandas/NumPy**: Data manipulation and entropy calculations.
- **HTML5/CSS3**: Modern, responsive user interfaces.

---

## 💻 How to Run

Each module runs as a separate Flask application.

### Prerequisites
```bash
pip install flask pandas numpy
```

### Running the Apps

**1. Start Spam Detective:**
```bash
cd ques1
python app.py
# Access at http://127.0.0.1:5001
```

**2. Start Loan Risk Evaluator:**
```bash
cd ques2
python app.py
# Access at http://127.0.0.1:5002
```

**3. Start Sales Predictor:**
```bash
cd ques3
python app.py
# Access at http://127.0.0.1:5003
```

---

## 📚 Documentation

For deep dives into the theory behind these algorithms, check out the [Wiki](https://github.com/MathiarasiE/ML_Assignment_1/wiki).

---
*Created as part of the Machine Learning coursework.*
