# definition of the individual for the EA

import random

# parameters about the genome/CAN specific parameters
ID_RANGE = 2**16
BYTE_SIZE = 2**8
SER_TESTED = 'tested'
SER_FITNESS = 'fitness'
SER_GENOME = 'genome'


class Individual:
    def __init__(self):
        self.tested = False  # signify that the individual has not been tested yet
        self.fitness = 0
        self.genome = [[random.random() > 0.5, random.randint(0, ID_RANGE)]]
        for i in range(8):
            self.genome.append([random.random() > 0.5, random.randint(0, BYTE_SIZE)])

    def test(self, test_data):
        total_score = 0
        for sample in test_data:
            prediction = 0
            if self.genome[0][0] and self.genome[0][1] == sample[0]:
                prediction += 1
            for j in range(sample[1]):
                if self.genome[j+1][0] and self.genome[j+1][1] == sample[j+2]:
                    prediction += 1

            if sample[-1] == 'T':
                total_score += prediction

        self.tested = True
        self.fitness = total_score
        return self.fitness

    def get_fitness(self):
        if self.tested:
            return self.fitness
        else:
            raise Exception("get_fitness was called when there was not a valid fitness value")

    def mutate(self, prob):
        if random.random() < prob:
            self.genome[0][0] = not self.genome[0][0]  # invert the ignore probability
            self.tested = False
        if random.random() < prob:
            self.genome[0][1] = random.randint(0, ID_RANGE)  # random new CAN ID value
            self.tested = False

        for i in range(1, 9):
            if random.random() < prob:
                self.genome[i][0] = not self.genome[i][0]
                self.tested = False
            if random.random() < prob:
                self.genome[i][1] = random.randint(0, BYTE_SIZE)
                self.tested = False
        return None

    def cross(self, other):
        cross_point = random.randint(1,8)
        temp = self.genome[cross_point:]
        self.genome[cross_point:] = other.genome[cross_point:]
        other.genome[cross_point:] = temp
        self.tested = False
        self.tested = False
        return None

    def serialize(self):
        data = {}
        data[SER_TESTED] = self.tested
        data[SER_FITNESS] = self.fitness
        data[SER_GENOME] = self.genome
        return data

    def load(self, data):
        self.genome = data[SER_GENOME]
        self.fitness = data[SER_FITNESS]
        self.tested = data[SER_TESTED]
        return None
