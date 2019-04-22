# definition of the individual for the EA

import random

# parameters about the genome/CAN specific parameters
ID_RANGE = 2**16
BYTE_SIZE = 2**8
SER_TESTED = 'tested'
SER_FITNESS = 'fitness'
SER_GENOME = 'genome'


class IndividualBinary:
    def __init__(self):
        self.tested = False  # signify that the individual has not been tested yet
        self.fitness = 0
        self.genome = []
        for i in range(8 * 10):  # 8 bits per byte * 10 bytes in a CAN message (ID + DATA field)
            # first binary value indicates if the bit is used
            # second binary value indicates what value to look for
            self.genome.append([random.random() > 0.5, random.random() > 0.5])

    def test(self, test_data):
        total_score = 0
        for sample in test_data:
            prediction = 0
            binary_string = '{0:016b}'.format(sample[0])
            for i in range(sample[1]):
                binary_string += '{0:08b}'.format(sample[i+2])
            for i, val in enumerate([x == '1' for x in binary_string]):
                if self.genome[i][0] and self.genome[i][1] == val:
                    prediction += 1

            if sample[-1] == 'T':
                total_score += prediction
            else:
                total_score -= prediction

        self.tested = True
        if total_score > 0:
            self.fitness = total_score
        else:
            self.fitness = 0
        return self.fitness

    def get_fitness(self):
        if self.tested:
            return self.fitness
        else:
            raise Exception("get_fitness was called when there was not a valid fitness value")

    def mutate(self, prob):
        for i in range(len(self.genome)):
            if random.random() < prob:
                self.genome[i][0] = not self.genome[i][0]
                self.tested = False
            if random.random() < prob:
                self.genome[i][1] = not self.genome[i][1]
                self.tested = False
        return None

    def cross(self, other):
        cross_point = random.randint(1, len(self.genome) - 1)
        temp = self.genome[cross_point:]
        self.genome[cross_point:] = other.genome[cross_point:]
        other.genome[cross_point:] = temp
        self.tested = False
        other.tested = False
        if len(self.genome) != 80 or len(other.genome) != 80:
            raise Exception("Genome is of invalid length!")
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

    def IDS_test(self, can_data):
        """
        Tests the genome performance by classifying CAN messages
        :param can_data: a list of CAN messages
        :return: accuracy percentage (float from 0-1)
        """
        # represent a prediction for every CAN message as a binary class label (True == injected)
        # and the integer value that the genome produces for it
        predictions = []

        # iterate over all CAN data messages
        for i, sample in enumerate(can_data):
            prediction = [False, 0]
            # update actual class label if necessary
            if sample[-1] == 'T':
                prediction[0] = True

            # run the message data against the genome
            binary_string = '{0:016b}'.format(sample[0])
            for j in range(sample[1]):
                binary_string += '{0:08b}'.format(sample[j+2])
            for j, val in enumerate([x == '1' for x in binary_string]):
                if self.genome[j][0] and self.genome[j][1] == val:
                    prediction[1] += 1
            predictions.append(prediction)

        # split the predictions into their respective classes and get the average prediction value
        injected_msgs = [p for p in predictions if p[0]]
        injected_avg = sum([p[1] for p in injected_msgs]) / len(injected_msgs)
        normal_msgs = [p for p in predictions if not p[0]]
        normal_avg = sum([p[1] for p in normal_msgs]) / len(normal_msgs)

        difference = injected_avg - normal_avg
        if difference < 0:
            raise Exception('Genome matches better with normal messages than injected messages! :(')

        # under the assumption that this difference must be positive (meaning that we assume the
        # injected messages have higher predictions than the normal messages...which they should)
        # messages with predictions higher than the difference are classified as injected
        correct = 0
        for p in predictions:
            if p[1] >= difference and p[0]:
                # message classified as injected and it is actually an injected message
                correct += 1
            elif p[1] < difference and not p[0]:
                # message classified as normal and it is actually a normal message
                correct += 1

        return correct / len(predictions)
