# Machine Learning Assignment - 1

This repository contains my solutions for the first Machine Learning assignment. I have implemented three different algorithms using Python and Flask to create simple web interfaces for testing them.

## Overview
The assignment covers:
1.  **Concept Learning** (Spam Classification)
2.  **Decision Trees** (Loan Default Prediction)
3.  **ID3 Algorithm** (Buy Computer Prediction)

Instead of just running scripts in the terminal, I built a small web page for each question so you can easily enter values and see the predicted output.

---

## Question 1: Spam Classification
**Path:** `ques1/`

For this problem, I used the **Find-S** algorithm to determine if an email is "Spam" or "Not Spam".
The model looks at four features:
*   Promotional Words (like "Win", "Free")
*   Suspicious Links
*   Known Sender
*   All Caps Subject

**How to run:**
```bash
cd ques1
python app.py
```

---

## Question 2: Loan Default Prediction
**Path:** `ques2/`

Here, I implemented a basic decision tree logic to check if a person might default on a loan. It uses **Entropy** and **Information Gain** concepts to make decisions based on:
*   Annual Income
*   Credit Score

**How to run:**
```bash
cd ques2
python app.py
```

---

## Question 3: Buy Computer (ID3 Algorithm)
**Path:** `ques3/`

This captures the logic of the **ID3 Algorithm** to predict if a customer will buy a computer. It takes into account:
*   Age
*   Income
*   Student Status
*   Credit Rating

**How to run:**
```bash
cd ques3
python app.py
```

---

## Documentation
I have also updated the [Wiki](https://github.com/Charanbtech/ML_Assignment_1/wiki) with more details about how these algorithms work and the datasets I used.
