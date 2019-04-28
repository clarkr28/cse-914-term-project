#!/usr/bin/python3

# This script is meant to do a bunch of evolutionary runs one after another

from EA import run

# run: pop_size, test_size, num_gens, log_freq, can_data_fname, mut_prob, keep_num

run_title = 'Fuzzy-3k-keep3-parallel'

try:
    run(200, 1000, 30, 50, 'Fuzzy_h_dataset.pkl', 0.0125, 3, run_title)
except Exception as e:
    print(e)

