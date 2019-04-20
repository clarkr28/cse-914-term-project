#!/usr/bin/python3

import gzip
import pickle
import os
import matplotlib.pyplot as plt

LOG_DIR = './logs/'
RUN_PARAMS_FNAME = 'run_params.pkl'
COMPRESSED_LOG_FNAME = 'compressed_log_data.pkl'
FIG_NAME = 'fitness_figure.png'

if __name__ == '__main__':

    # get log folder names
    folders = os.listdir(LOG_DIR)
    folders.sort()
    for folder in folders:
        if COMPRESSED_LOG_FNAME in os.listdir(LOG_DIR + folder) and \
                FIG_NAME not in os.listdir(LOG_DIR + folder):

            f = gzip.open(LOG_DIR + folder + '/' + COMPRESSED_LOG_FNAME)
            data = pickle.load(f)
            f.close()
            avg_fitnesses = []
            max_fitnesses = []
            x_values = []
            for i in data['logs']:
                avg_fitnesses.append(data['logs'][i]['avg_fitness'])
                max_fitnesses.append(data['logs'][i]['max_fitness'])
                x_values.append(i)

            plt.figure()
            plt.plot(x_values, avg_fitnesses)
            plt.plot(x_values, max_fitnesses)
            plt.ylabel('Fitness (max: {})'.format(max(max_fitnesses)))
            plt.xlabel('Generation')
            plt.title('Data: {}, Pop: {},\n Test Size: {}, Mutation: {}, Keep Best: {}'.format(
                data['can_data_fname'], data['pop_size'], data['test_size'], data['mut_prob'],
                data['keep_num']
            ))
            plt.savefig(LOG_DIR + folder + '/' + FIG_NAME)
            plt.close()

