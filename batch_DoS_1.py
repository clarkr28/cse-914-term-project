#!/usr/bin/python3

# This script is meant to do a bunch of evolutionary runs one after another

from EA import run

# run: pop_size, test_size, num_gens, log_freq, can_data_fname, mut_prob, keep_num

run_title_base = 'DoS-keep3-mut'
muts = [0.025]

for m in muts:
    run_title = run_title_base + str(m).split('.')[1]
    try:
        run(1000, 500, 50, 100, 'DoS_train.pkl', m, 3, run_title)
    except Exception as e:
        print(e)

