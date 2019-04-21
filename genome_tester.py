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

    print()
    print(' --- Run Parameters --- ')
    print('Data: {}, Mutation: {}, Keep Best: {}'.format(
        data['can_data_fname'], data['mut_prob'], data['keep_num']
    ))
    print('Population: {}, Test Size: {}, Generations: {}'.format(
        data['pop_size'], data['test_size'], data['num_gens']
    ))
    print()

    data_files = os.listdir(CAN_DATA_DIR)
    data_files.sort()
    for i, data_file in enumerate(data_files):
        print('{:02d}...{}'.format(i, data_file))

    print()
    data_file_num = -1
    while data_file_num < 0 or data_file_num >= len(data_files):
        data_file_num = int(input('Pick a data file by number: '))
    data_file_name = data_files[data_file_num]

    f = open(CAN_DATA_DIR + data_file_name, 'rb')
    test_data = pickle.load(f)
    f.close()
