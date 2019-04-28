#!/usr/bin/python3

# This script is meant to do a bunch of evolutionary runs one after another

from EA import run

# run: pop_size, test_size, num_gens, log_freq, can_data_fname, mut_prob, keep_num

run_title_base = 'Fuzzy-3k-keep3-mut'
muts = [0.00625, 0.0125, 0.025, 0.05, 0.075, 0.1, 0.15]

for m in muts:
    run_title = run_title_base + str(m).split('.')[1]
    try:
        run(500, 500, 1000, 100, 'Fuzzy_train.pkl', m, 3, run_title)
    except Exception as e:
        print(e)

