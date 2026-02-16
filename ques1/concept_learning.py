import pandas as pd

def train_spam_filter(csv_path):
    # Function to train the model using Find-S algorithm
    
    # Read the dataset
    df = pd.read_csv(csv_path)

    # The last column is the target label (Spam/Not Spam)
    target_column = df.columns[-1]
    
    # All other columns are features
    feature_names = df.columns[:-1]

    # Initialize hypothesis with a specific value (indicating no knowledge yet)
    # We use '0' to represent the most specific hypothesis
    specific_hypothesis = ['0'] * len(feature_names)

    # Iterate through each record in the dataset
    for index, row in df.iterrows():
        # We only learn from positive examples (Spam) in Find-S
        if row[target_column] == "Spam":
            for i, feature in enumerate(feature_names):
                # If this is the first positive example, adopt its features
                if specific_hypothesis[i] == '0':
                    specific_hypothesis[i] = row[feature]
                # If the feature value differs from the hypothesis, generalize it
                elif specific_hypothesis[i] != row[feature]:
                    specific_hypothesis[i] = '?'

    return specific_hypothesis, list(feature_names)


def classify_email(hypothesis, feature_names, input_features):
    """
    Classifies an email based on the learned hypothesis.
    """
    for i in range(len(hypothesis)):
        constraint = hypothesis[i]
        
        # If the constraint is general ('?'), any value is acceptable
        if constraint == '?':
            continue
            
        # If the specific constraint does not match the input, it's not Spam
        if constraint != input_features[i]:
            return "Not Spam"
            
    # If all constraints match
    return "Spam"
