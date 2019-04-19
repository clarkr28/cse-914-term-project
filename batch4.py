#!/usr/bin/python3

# This script is meant to do a bunch of evolutionary runs one after another

from EA import run

# run: pop_size, test_size, num_gens, log_freq, can_data_fname, mut_prob, keep_num

try:
    run(200, -1, 400, 10, 'Fuzzy_3000.pkl', 0.025, 30)
except Exception as e:
    print(e)

try:
    run(200, -1, 400, 10, 'Fuzzy_3000.pkl', 0.050, 30)
except Exception as e:
    print(e)

try:
    run(200, -1, 400, 10, 'Fuzzy_3000.pkl', 0.075, 30)
except Exception as e:
    print(e)

try:
    run(200, -1, 400, 10, 'Fuzzy_3000.pkl', 0.100, 30)
except Exception as e:
    print(e)
