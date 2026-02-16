# Concept Learning — Spam Classification

## Concept Learning for Spam Email Classification

### Overview
This project demonstrates how a machine learning system can classify emails as **Spam** or **Not Spam** using **Concept Learning**. The system learns patterns from labeled examples and builds a hypothesis that can be used to classify new emails.

### What is Concept Learning?
Concept Learning is a machine learning approach where a system learns a general rule (called a hypothesis) from training examples. The goal is to identify patterns that distinguish one class from another.

In this project, the concept being learned is:  
**"Whether an email is Spam or Not Spam."**

The system analyzes features such as promotional words, suspicious links, sender information, and use of capital letters to learn the classification rule.

### Dataset Description
The dataset consists of email samples with the following binary attributes:

| Attribute | Description | Possible Values |
| :--- | :--- | :--- |
| **Promotional Words** | Does the email contain words like "Win", "Free"? | Yes / No |
| **Suspicious Links** | Does the email contain unknown links? | Yes / No |
| **Known Sender** | Is the sender in the contact list? | Yes / No |
| **All Caps** | Is the subject/body written in capital letters? | Yes / No |

### Learning Approach — Find-S Algorithm
The **Find-S (Find-Specific)** algorithm is used to find the most specific hypothesis that fits all positive examples (Spam).

#### Steps:
1.  Initialize the hypothesis to the most specific value: `['0', '0', '0', '0']`.
2.  Iterate through each **positive** training example (Spam emails).
3.  For each attribute, if the hypothesis value matches the example, keep it.
4.  If it doesn't match, replace it with a generic value `?` (accepts any value).
5.  Negative examples (Not Spam) are ignored in Find-S.

### Learned Hypothesis
After processing the training data, the algorithm produces a specific hypothesis.

**Example Hypothesis:**
```python
['Yes', '?', '?', '?']
```
*Meaning: If "Promotional Words" are "Yes", it is Spam, regardless of other attributes.*

### How the System Learns from Examples

#### Positive Examples (Spam)
- Emails marked as "Spam" are used to generalize the hypothesis.
- Example: If one spam email has "Suspicious Links" = Yes and another has "No", the system learns that this feature is not a deciding factor (becomes `?`).

#### Negative Examples (Not Spam)
- Used to verify consistency but heavily relied upon by more advanced algorithms (like Candidate-Elimination). In Find-S, they are implicitly treated as "not matching the specific hypothesis".

### Classification Process
1.  **Input:** A new email with extracted features.
2.  **Comparison:** The system compares the email features against the learned hypothesis.
3.  **Result:**
    - If it matches the hypothesis patterns -> **Classified as Spam**.
    - Otherwise -> **Classified as Not Spam**.
