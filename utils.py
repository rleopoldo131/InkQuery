def load_labels(filepath):
    with open(filepath, 'r') as file:
        labels = [line.strip() for line in file]
    return labels
