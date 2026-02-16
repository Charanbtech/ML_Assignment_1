# ID3 Buying Computer Analysis

## ID3 Algorithm for Consumer Behavior Prediction

### Overview
This project predicts whether a customer will buy a computer based on their demographic profile using the **ID3 (Iterative Dichotomiser 3)** algorithm.

### What is the ID3 Algorithm?
ID3 is a classic decision tree algorithm that uses **Entropy** and **Information Gain** to build a decision tree top-down. It recursively partitions the data into smaller subsets until all examples in a subset belong to the same class.

### Dataset Description
The dataset includes demographic attributes of potential customers.

| Attribute | Values | Description |
| :--- | :--- | :--- |
| **Age** | `<=30`, `31-40`, `>40` | Age group of the customer. |
| **Income** | `High`, `Medium`, `Low` | Income level. |
| **Student** | `Yes`, `No` | Is the customer a student? |
| **Credit Rating** | `Fair`, `Excellent` | Credit history status. |
| **Buys Computer** | `Yes`, `No` | Target variable. |

### Learning Approach
The ID3 algorithm builds the tree recursively.

#### Steps:
1.  **Calculate Global Entropy:** Determine the impurity of the entire dataset.
2.  **Calculate Information Gain for Each Attribute:**
    - For each attribute (e.g., Age), split the data into groups.
    - Calculate the entropy of each group.
    - Compute the weighted average entropy.
    - Subtract from Global Entropy to get Information Gain.
3.  **Choose the Best Attribute:** The attribute with the highest gain becomes the root node.
4.  **Recurse:** Repeat the process for each branch (subset of data) until:
    - All instances are the same class.
    - No attributes are left.

### Example Analysis
**Root Node Selection:**
- **Age** typically has the highest information gain in this dataset.
- If `Age = <=30`: The `Student` attribute becomes the next deciding factor.
- If `Age = 31-40`: They almost always buy (Leaf Node: Yes).
- If `Age = >40`: The `Credit Rating` typically decides.

### Classification Process
The final tree allows us to classify new customers:

**New Customer:**
- **Age:** `<=30`
- **Income:** `Medium`
- **Student:** `Yes`
- **Credit Rating:** `Fair`

**Prediction Path:**
1. Check **Age** (`<=30`) -> Go to "Student" branch.
2. Check **Student** (`Yes`) -> **Prediction: Yes**.
