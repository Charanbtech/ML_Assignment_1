# Machine Learning Assignment 1

## Overview
This repository presents solutions to three foundational machine learning problems focusing on:
- **Concept Learning**
- **Decision Trees with Continuous Attributes**
- **ID3 Algorithm Implementation**

The assignment combines theoretical understanding, manual algorithm implementation in Python, and practical prediction tasks without using external ML libraries.

## Repository Structure

```
ML-Assignment-1/
│
├── 01_concept_learning_spam.py          # Question 1: Spam Email Classification
├── 02_loan_default_prediction.py        # Question 2: Loan Default Prediction
├── 03_id3_buy_computer.py               # Question 3: Buy Computer Prediction
├── README.md                            # Project Documentation
└── Wiki/                                # Detailed documentation
```

## Question 1: Concept Learning (Spam Email Classification)
### Problem Statement
Design a learning system that classifies emails as **Spam** or **Not Spam** using labeled training examples and identifying common feature patterns.

### Methodology
- Applied the **Find-S algorithm** to learn the most specific hypothesis from positive examples.
- Considered features:
    - Promotional words
    - Suspicious links
    - Known sender
    - Use of capital letters
- Built a rule-based classifier to predict new emails.

### Core Concepts
- Hypothesis space
- Positive vs. negative examples
- Generalization from data
- Rule-based classification

### Result
The learned hypothesis successfully distinguishes spam emails using shared attribute patterns.

## Question 2: Decision Tree with Continuous Attributes (Loan Default Prediction)
### Problem Statement
Predict whether a customer will default on a loan using continuous attributes:
- **Annual Income (₹ Lakhs)**
- **Credit Score**

### Methodology
1. Computed dataset entropy.
2. Generated candidate threshold splits for income.
3. Calculated information gain for each threshold.
4. Selected the best split and formed a decision rule.

### Core Concepts
- Entropy and impurity measurement
- Continuous attribute thresholding
- Information gain maximization
- Interpretable decision tree rules

### Result
The optimal threshold cleanly separates defaulters from non-defaulters, producing a simple and interpretable model.

## Question 3: ID3 Algorithm (Buy Computer Dataset)
### Problem Statement
Construct a decision tree using the **ID3 algorithm** to predict whether a customer will buy a computer based on demographic attributes.

### Methodology
1. Implemented ID3 from scratch in Python.
2. Calculated entropy and information gain for each attribute.
3. Recursively built the decision tree structure.
4. Predicted the class label for a new customer instance.

### Core Concepts
- Recursive tree construction
- Attribute selection using information gain
- Entropy reduction
- Classification prediction

### Result
The trained decision tree correctly predicts the purchasing decision for the test example.

## Tools and Technologies
- **Language:** Python 3
- **Libraries:** Built-in data structures and math functions only (No external ML libraries)
- **Version Control:** GitHub

## Learning Outcomes
This assignment helped develop:
- Strong understanding of **supervised learning fundamentals**.
- Ability to **implement ML algorithms manually**.
- Skills in **decision tree interpretation and evaluation**.
- Analytical reasoning for model behavior.
- Professional technical documentation practices.

## How to Run
To run the assignments, execute the Python scripts via terminal:

```bash
# Question 1: Run Concept Learning Spam Classifier
python 01_concept_learning_spam.py

# Question 2: Run Loan Default Decision Tree
python 02_loan_default_prediction.py

# Question 3: Run ID3 Algorithm
python 03_id3_buy_computer.py
```