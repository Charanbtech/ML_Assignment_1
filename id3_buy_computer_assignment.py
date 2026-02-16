import math
from collections import Counter

data = [
    ["<=30", "high", "no", "fair", "no"],
    ["<=30", "high", "no", "excellent", "no"],
    ["31-40", "high", "no", "fair", "yes"],
    [">40", "medium", "no", "fair", "yes"],
    [">40", "low", "yes", "fair", "yes"],
    [">40", "low", "yes", "excellent", "no"],
    ["31-40", "low", "yes", "excellent", "yes"],
    ["<=30", "medium", "no", "fair", "no"],
    ["<=30", "low", "yes", "fair", "yes"],
    [">40", "medium", "yes", "fair", "yes"],
    ["<=30", "medium", "yes", "excellent", "yes"],
    ["31-40", "medium", "no", "excellent", "yes"],
    ["31-40", "high", "yes", "fair", "yes"],
    [">40", "medium", "no", "excellent", "no"]
]

attributes = ["age", "income", "student", "credit_rating"]


def entropy(rows):
    labels = [row[-1] for row in rows]
    counts = Counter(labels)
    total = len(rows)

    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent


def info_gain(rows, attr_index):
    total_ent = entropy(rows)
    total = len(rows)
    values = set(row[attr_index] for row in rows)

    weighted_ent = 0
    for v in values:
        subset = [r for r in rows if r[attr_index] == v]
        weighted_ent += (len(subset) / total) * entropy(subset)

    return total_ent - weighted_ent


def id3(rows, attrs):
    labels = [r[-1] for r in rows]
    if labels.count(labels[0]) == len(labels):
        return labels[0]

    if not attrs:
        return Counter(labels).most_common(1)[0][0]

    gains = [info_gain(rows, attributes.index(a)) for a in attrs]
    best_attr = attrs[gains.index(max(gains))]
    best_index = attributes.index(best_attr)

    tree = {best_attr: {}}
    values = set(r[best_index] for r in rows)

    for v in values:
        subset = [r for r in rows if r[best_index] == v]
        remaining = [a for a in attrs if a != best_attr]
        tree[best_attr][v] = id3(subset, remaining)

    return tree


tree = id3(data, attributes.copy())

print("\nDecision Tree:")
print(tree)


def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree

    attr = next(iter(tree))
    index = attributes.index(attr)
    value = sample[index]

    if value in tree[attr]:
        return predict(tree[attr][value], sample)
    else:
        return "Unknown"


new_example = ["<=30", "medium", "yes", "fair"]
prediction = predict(tree, new_example)

print("\nNew Example:", new_example)
print("Buys Computer Prediction:", prediction)
