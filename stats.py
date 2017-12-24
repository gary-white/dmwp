from collections import Counter


def mean(dataset):
    return sum(dataset) / len(dataset)


def median(dataset):
    length = len(dataset)
    dataset.sort()

    if length % 2 == 1:
        return dataset[int(length / 2)]

    pair = [dataset[int(length / 2) - 1], dataset[int(length / 2)]]
    return mean(pair)


def mode(dataset):
    c = Counter(dataset)
    return c.most_common()[0][0]
