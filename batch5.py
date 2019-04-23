#!/usr/bin/python3

# This script is meant to do a bunch of evolutionary runs one after another

from EA import run

# run: pop_size, test_size, num_gens, log_freq, can_data_fname, mut_prob, keep_num

run_title = 'DoS-3k-keep5'

try:
    run(200, -1, 400, 20, 'DoS_synthetic_3000.pkl', 0.0625, 5, run_title)
except Exception as e:
    print(e)

try:
    run(200, -1, 400, 20, 'DoS_synthetic_3000.pkl', 0.0750, 5, run_title)
except Exception as e:
    print(e)

try:
    run(200, -1, 400, 20, 'DoS_synthetic_3000.pkl', 0.0875, 5, run_title)
except Exception as e:
    print(e)

try:
    run(200, -1, 400, 20, 'DoS_synthetic_3000.pkl', 0.0100, 5, run_title)
except Exception as e:
    print(e)
