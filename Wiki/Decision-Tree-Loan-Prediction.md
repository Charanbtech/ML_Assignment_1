# Decision Tree — Loan Default Prediction

## Decision Tree for Loan Default Prediction

### Overview
This section details the implementation of a **Decision Tree** classifier to predict whether a customer will default on a loan. The model uses continuous attributes and splits them based on **Information Gain**.

### What is a Decision Tree?
A Decision Tree is a flowchart-like structure where each internal node represents a test on an attribute, each branch represents the outcome of the test, and each leaf node represents a class label.

In this project, the goal is to predict:
**"Will the customer default on the loan? (Yes/No)"**

### Dataset Description
The dataset contains financial information about customers.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| **Annual Income** | Continuous | The customer's total yearly income (in Lakhs). |
| **Credit Score** | Continuous | A numeric representation of creditworthiness (300-900). |
| **Defaulted** | Target | The class label: **Yes** (Defaulted) or **No** (Did not default). |

### Learning Approach — ID3 with Continuous Splits
Standard ID3 handles categorical data. For continuous data (like Income), we must find the best **split point** (threshold).

#### Steps:
1.  **Sort the data** based on the continuous attribute.
2.  **Identify split points** (midpoints between adjacent values).
3.  **Calculate Information Gain** for each split point.
    - Compute Entropy of the parent set.
    - Compute Weighted Entropy of the children sets (Left < Threshold, Right > Threshold).
    - `Gain = Entropy(Parent) - Weighted_Entropy(Children)`
4.  **Select the Best Split:** The threshold with the highest Information Gain is chosen as the root node.

### Core Concepts

#### Entropy
A measure of impurity or randomness in the data.
- **High Entropy:** Mix of Yes/No (Hard to predict).
- **Low Entropy:** Mostly Yes or Mostly No (Easy to predict).

#### Information Gain
Measures how much "information" a feature gives us about the class. We always choose the feature that gives the **highest information gain**.

### Result
The algorithm constructs a tree with rules like:

```text
IF Income <= 3.25 Lakhs:
    AND Credit Score <= 590 -> Default: Yes
    AND Credit Score > 590  -> Default: Yes
IF Income > 3.25 Lakhs -> Default: No
```

This provides a clear, interpretable set of rules for loan approval.
