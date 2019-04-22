#!/usr/bin/python3
# The goal of this script is to test genomes as if it were an IDS

import os
import gzip
import pickle
from ea_individual_binary import IndividualBinary

# constants
LOG_DIR = './logs/'
CAN_DATA_DIR = './data/'
COMPRESSED_LOG_FNAME = 'compressed_log_data.pkl'


def run_test(log_data, train_data, test_data):
    # get the oldest genome from the run
    max_gen = max(log_data['logs'])
    if 'individuals' not in log_data['logs'][max_gen]:
        raise Exception('Serialized population not found in last generation!')

    # take the serialized individuals and load them into the IndividualBinary class
    pop = []
    for serialized_data in log_data['logs'][max_gen]['individuals']:
        individual = IndividualBinary()
        individual.load(serialized_data)
        pop.append(individual)

    # select the n best individuals based on their final fitness value
    keep_individuals = 10
    pop = sorted(pop, key= lambda x: x.get_fitness(), reverse=True)[0:keep_individuals]

    train_accuracies = [p.IDS_test(train_data) for p in pop]
    test_accuracies = [p.IDS_test(test_data) for p in pop]

    return train_accuracies, test_accuracies


if __name__ == '__main__':
    # get a listing of log folders then prompt the user to pick one
    folders = os.listdir(LOG_DIR)
    folders.sort()
    for i, folder in enumerate(folders):
        print('{:02d}...{}'.format(i, folder))

    print()
    folder_num = -1
    while folder_num < 0 or folder_num >= len(folders):
        folder_num = int(input('Pick a folder by number: '))
    folder_name = folders[folder_num]

    # open the compressed log
    f = gzip.open(LOG_DIR + folder_name + '/' + COMPRESSED_LOG_FNAME)
    data = pickle.load(f)
    f.close()

    # open the training data
    f = open(CAN_DATA_DIR + data['can_data_fname'], 'rb')
    train_data = pickle.load(f)
    f.close()

    print()
    print(' --- Run Parameters --- ')
    print('Data: {}, Mutation: {}, Keep Best: {}'.format(
        data['can_data_fname'], data['mut_prob'], data['keep_num']
    ))
    print('Population: {}, Test Size: {}, Generations: {}'.format(
        data['pop_size'], data['test_size'], data['num_gens']
    ))
    print()

    # print all the data files so the user knows the options
    data_files = os.listdir(CAN_DATA_DIR)
    data_files.sort()
    for i, data_file in enumerate(data_files):
        print('{:02d}...{}'.format(i, data_file))

    # prompt the user to pick a test dataset
    print()
    data_file_num = -1
    while data_file_num < 0 or data_file_num >= len(data_files):
        data_file_num = int(input('Pick a data file by number: '))
    data_file_name = data_files[data_file_num]

    f = open(CAN_DATA_DIR + data_file_name, 'rb')
    test_data = pickle.load(f)
    f.close()

    train_accuracies, test_accuracies = run_test(data, train_data, test_data)

    # print results
    print('test   train')
    for [train, test] in zip(train_accuracies, test_accuracies):
        print('{:.3f}  {:.3f}'.format(train, test))

    # save results to file
