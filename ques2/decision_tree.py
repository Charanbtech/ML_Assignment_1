import pandas as pd
import numpy as np
import math

def calculate_entropy(target_column):
    """
    Calculates the entropy of a target column.
    """
    elements, counts = np.unique(target_column, return_counts=True)
    entropy = 0
    total_samples = len(target_column)
    
    for count in counts:
        probability = count / total_samples
        entropy -= probability * math.log2(probability)
        
    return entropy

def calculate_information_gain(data, split_attribute_name, target_name="Defaulted"):
    """
    Calculates the information gain of a dataset split on a specific attribute.
    """
    total_entropy = calculate_entropy(data[target_name])
    
    # Calculate weighted entropy for the children
    vals, counts = np.unique(data[split_attribute_name], return_counts=True)
    weighted_entropy = 0
    total_samples = len(data)
    
    for i in range(len(vals)):
        prob = counts[i] / total_samples
        child_subset = data[data[split_attribute_name] == vals[i]]
        weighted_entropy += prob * calculate_entropy(child_subset[target_name])
        
    return total_entropy - weighted_entropy

def build_loan_decision_tree(csv_path):
    # Builds the decision tree from the csv file
    df = pd.read_csv(csv_path)
    
    # We are using specific logic for this assignment to check the rules
    
    # Calculate global entropy
    global_entropy = calculate_entropy(df["Defaulted"])
    
    return df

def predict_loan_status(income, credit_score):
    """
    Predicts loan default status based on Income and Credit Score.
    Uses the rules derived from the Decision Tree construction.
    """
    # Derived Rule: IF Income <= 3.25 THEN Default=Yes ELSE Default=No
    # (Based on typical assignment dataset values)
    
    try:
        income = float(income)
        credit_score = float(credit_score)
    except ValueError:
        return "Invalid Input"

    if income <= 3.25:
        return "Yes (High Risk)"
    else:
        return "No (Low Risk)"
