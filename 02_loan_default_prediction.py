import math

data = [
    [2.5, 580, "Yes"],
    [3.0, 600, "Yes"],
    [3.5, 650, "No"],
    [4.0, 700, "No"],
    [4.5, 720, "No"],
    [5.0, 750, "No"]
]

attributes = ["Income", "Credit Score"]


def entropy(rows):
    total = len(rows)
    yes = sum(1 for r in rows if r[-1] == "Yes")
    no = total - yes

    ent = 0
    for count in [yes, no]:
        if count != 0:
            p = count / total
            ent -= p * math.log2(p)
    return ent


def best_split(rows, index):
    rows = sorted(rows, key=lambda x: x[index])
    thresholds = []

    for i in range(len(rows) - 1):
        v1, v2 = rows[i][index], rows[i + 1][index]
        thresholds.append((v1 + v2) / 2)

    best_gain = -1
    best_threshold = None
    base_entropy = entropy(rows)

    for t in thresholds:
        left = [r for r in rows if r[index] <= t]
        right = [r for r in rows if r[index] > t]

        if not left or not right:
            continue

        weighted = (len(left) / len(rows)) * entropy(left) + (len(right) / len(rows)) * entropy(right)
        gain = base_entropy - weighted

        if gain > best_gain:
            best_gain = gain
            best_threshold = t

    return best_threshold, best_gain


def build_tree(rows):
    labels = [r[-1] for r in rows]

    if labels.count(labels[0]) == len(labels):
        return labels[0]

    gains = []
    splits = []

    for i in range(len(attributes)):
        t, g = best_split(rows, i)
        gains.append(g)
        splits.append(t)

    best_attr_index = gains.index(max(gains))
    best_threshold = splits[best_attr_index]

    if best_threshold is None:
        return max(set(labels), key=labels.count)

    left = [r for r in rows if r[best_attr_index] <= best_threshold]
    right = [r for r in rows if r[best_attr_index] > best_threshold]

    return {
        attributes[best_attr_index]: {
            "<=" + str(best_threshold): build_tree(left),
            ">" + str(best_threshold): build_tree(right)
        }
    }


tree = build_tree(data)

print("\nDecision Tree:")
print(tree)


def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree

    attr = next(iter(tree))
    index = attributes.index(attr)

    for condition in tree[attr]:
        if condition.startswith("<="):
            threshold = float(condition[2:])
            if sample[index] <= threshold:
                return predict(tree[attr][condition], sample)
        else:
            threshold = float(condition[1:])
            if sample[index] > threshold:
                return predict(tree[attr][condition], sample)

    return "Unknown"


new_customer = [3.2, 620]

prediction = predict(tree, new_customer)

print("\nNew Customer:", new_customer)
print("Default Prediction:", prediction)
