#!/usr/bin/python3

# This script is meant to do a bunch of evolutionary runs one after another

from EA import run

# run: pop_size, test_size, num_gens, log_freq, can_data_fname, mut_prob, keep_num

try:
    run(300, -1, 500, 10, 'Fuzzy_3000.pkl', 0.025, 5)
except Exception as e:
    print(e)

try:
    run(300, -1, 500, 10, 'Fuzzy_3000.pkl', 0.050, 5)
except Exception as e:
    print(e)

try:
    run(300, -1, 500, 10, 'Fuzzy_3000.pkl', 0.075, 5)
except Exception as e:
    print(e)

try:
    run(300, -1, 500, 10, 'Fuzzy_3000.pkl', 0.100, 5)
except Exception as e:
    print(e)

try:
    run(300, -1, 500, 10, 'Fuzzy_3000.pkl', 0.025, 15)
except Exception as e:
    print(e)

try:
    run(300, -1, 500, 10, 'Fuzzy_3000.pkl', 0.050, 15)
except Exception as e:
    print(e)

try:
    run(300, -1, 500, 10, 'Fuzzy_3000.pkl', 0.075, 15)
except Exception as e:
    print(e)

try:
    run(300, -1, 500, 10, 'Fuzzy_3000.pkl', 0.100, 15)
except Exception as e:
    print(e)

try:
    run(300, -1, 500, 10, 'Fuzzy_3000.pkl', 0.025, 30)
except Exception as e:
    print(e)

try:
    run(300, -1, 500, 10, 'Fuzzy_3000.pkl', 0.050, 30)
except Exception as e:
    print(e)

try:
    run(300, -1, 500, 10, 'Fuzzy_3000.pkl', 0.075, 30)
except Exception as e:
    print(e)

try:
    run(300, -1, 500, 10, 'Fuzzy_3000.pkl', 0.100, 30)
except Exception as e:
    print(e)
