from random import shuffle


class Repository:
    def __init__(self, filename):
        self.data = {}

        self.__load_data_from_file(filename)

    def __load_data_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip("\n").split(",")

                if not line[-1] in self.data:
                    self.data[line[-1]] = []

                self.data[line[-1]].append([float(x) for x in line[:-1]])

    def shuffle(self):
        # Shuffles the data set
        [shuffle(self.data[key]) for key in self.data]