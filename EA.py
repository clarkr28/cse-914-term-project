# purpose of this file is to run an EA to evolve an IDS for a can network
# written by Jared Clark for CSE 914

# notes:
#   data labels: 'R' means normal, 'T' means injected

import random
import pickle # CAN data was saved in pkl format
from ea_individual import Individual
from ea_individual_binary import IndividualBinary
from datetime import datetime
import os

# parameters about the EA
POP_SIZE = 25
TESTS_PER_GENOME = 10
KEEP_BEST = 3
LOG_DIR = './logs/'
CAN_DATA_DIR = './data/'
RUN_PARAMS_FNAME = 'run_params.pkl'
LOG_FNAME = 'log_gen_'


def logger(fname, pop, avg_fitness, max_fitness, min_fitness, generation):
    log_data = {}
    log_data['avg_fitness'] = avg_fitness
    log_data['max_fitness'] = max_fitness
    log_data['min_fitness'] = min_fitness
    log_data['individuals'] = [p.serialize() for p in pop]
    log_data['generation'] = generation
    f = open(fname, 'wb')
    pickle.dump(log_data, f)
    f.close()


def run(pop_size, test_size, num_gens, log_freq, can_data_fname, mut_prob, keep_num):
    """
    run the EA with the specified parameters
    :param pop_size: population size to use
    :param test_size: number of CAN messages to test for every individual
    :param num_gens: number of generations to run
    :param log_freq: how frequently to save the population and their fitness values
    :param can_data_fname: the filename of the can data to use
    :return:
    """

    run_name = str(datetime.now()).split('.')[0]
    run_dir = LOG_DIR + run_name + '/'
    os.mkdir(run_dir)

    # save params to file
    run_params = {}
    run_params['pop_size'] = pop_size
    run_params['test_size'] = test_size
    run_params['num_gens'] = num_gens
    run_params['log_freq'] = log_freq
    run_params['can_data_fname'] = can_data_fname
    run_params['mut_prob'] = mut_prob
    run_params['keep_num'] = keep_num
    f = open(run_dir + RUN_PARAMS_FNAME, 'wb')
    pickle.dump(run_params, f)
    f.close()

    # generate an initial population
    pop = []
    for i in range(pop_size):
        pop.append(IndividualBinary())

    # load the testing data
    f = open(CAN_DATA_DIR + can_data_fname, 'rb')
    can_data = pickle.load(f)
    f.close()

    for i in range(num_gens):
        """
        evaluate individuals
        """
        # get subset of data to test with (all the test data would be too slow)
        test_inds = []
        while len(test_inds) < test_size:
            ind = random.randint(0, len(can_data) - 1)
            if ind not in test_inds:
                test_inds.append(ind)
        test_data_subset = [can_data[i] for i in test_inds]

        # run fitness test on all individuals because the data is random every round
        fitnesses = []
        for p in pop:
            fitnesses.append(p.test(test_data_subset))

        max_fitness = max(fitnesses)
        avg_fitness = sum(fitnesses) / len(pop)
        print('gen {} fitnesses - max: {}, avg: {}'.format(i, max_fitness, avg_fitness))

        # get the n best individuals
        # start with the first n and sort them
        n_best = pop[0:keep_num]
        n_best.sort(key=lambda x: x.get_fitness(), reverse=True)
        # filter through the rest and swap up
        for i, p in enumerate(pop[keep_num:]):
            if p.get_fitness() > n_best[-1].get_fitness():
                n_best[-1] = p
                index = len(n_best) - 2
                while index >= 0 and n_best[index].get_fitness() < n_best[index+1].get_fitness():
                    temp = n_best[index]
                    n_best[index] = n_best[index+1]
                    n_best[index+1] = temp
                    index -= 1


        """
        log data
        """
        if i % log_freq == 0 or i == num_gens - 1:
            logger(run_dir + LOG_FNAME + str(i) + '.pkl',
                   pop, avg_fitness, max_fitness, min(fitnesses), i)

        # select individuals for next generation
        next_gen = n_best
        for p in pop:
            if random.random() < p.get_fitness() / max_fitness:
                next_gen.append(p)

        # crossover
        for j in range(keep_num, len(next_gen), 2):
            if j+1 < len(next_gen):
                next_gen[j].cross(next_gen[j+1])

        # mutate offspring
        for p in next_gen:
            p.mutate(mut_prob)

        # create new individuals
        while len(next_gen) < pop_size:
            next_gen.append(Individual())

        pop = next_gen

