from collections import Counter

import numpy


class Controller:
    def __init__(self, repository):
        self.repository = repository

    def algorithm(self, data, predict, k=3):
        # Check if k has the right value
        if len(data) >= k:
            print("K must be > than total voting groups!")
            return None

        distances = []
        for group in data:
            for features in data[group]:
                euclidian = numpy.linalg.norm(numpy.array(features) - numpy.array(predict))
                distances.append([euclidian, group])

        votes = [i[1] for i in sorted(distances)[:k]]
        result = Counter(votes).most_common(1)[0][0]

        return result

    def run(self, test_size=0.2):
        # Shuffle data in repo
        self.repository.shuffle()

        # Pick cut position based on test_size
        pos = int(test_size * sum(len(self.repository.data[value]) for value in self.repository.data))

        # Init the sets
        train_set = {}
        test_set = {}
        for cls in self.repository.data:
            train_set[cls] = []
            test_set[cls] = []

        # Get the data from the repo
        full_data = []
        [full_data.extend([(val, value) for val in self.repository.data[value]]) for value in self.repository.data]
        train_data = full_data[:-pos]
        test_data = full_data[-pos:]

        # Fill in the sets
        for element in train_data:
            train_set[element[-1]].append(element[:-1])
        for element in test_data:
            test_set[element[-1]].append(element[:-1])

        # Learn and test
        correct = 0
        total = 0

        for group in test_set:
            for data in test_set[group]:
                vote = self.algorithm(train_set, data, k=5)
                if group == vote:
                    correct += 1
                total += 1

        return correct/total
