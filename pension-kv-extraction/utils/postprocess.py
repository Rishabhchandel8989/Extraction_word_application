def build_kv(tokens, labels):
    result = {}
    current_key = None

    for token, label in zip(tokens, labels):
        if label.startswith("B-"):
            current_key = label[2:]
            result[current_key] = token
        elif label.startswith("I-"):
            result[current_key] += " " + token

    return result
