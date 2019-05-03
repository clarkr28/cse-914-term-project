# Evolutionary Intrusion Detection System for Controller Area Networks

by Jared Clark for CSE 914 (An Automotive Cyber-Security Course)

The following provides an overview of this repo's contents and how to run important programs.

## Folders

- **data**: This folder contains all of the CAN data that was used in evolutionary runs.  As my program changed through the course of the project, the way I used the data also changed, which is why there are so many versions of the same data.  The final datasets that I ended up using for my main results were DoS_test.pkl, DoS_train.pkl, Fuzzy_train.pkl, and Fuzzy_test.pkl.  

- **latex_source**: My Latex source used to generate the final report.

- **logs**: Every run logged a lot of data.  These logs quickly started taking up a lot of space, so I added a function at the end of the runs to compress all the data into a giant compressed pickle.  Every run has their own folder in the logs foler, where the folder name starts with the current date and time to prevent collisions and is followed by a custom message about the run.  Within every run folder there should also be a graph that plots the maximum and average fitness values for every generation of the run, which is a nice way to quickly visualize how the run performed.  Running graph_generator.py will iterate through all of the logged runs and generate any missing graphs, so long as it finds a compressed pickle with all the logged data.  

## Non-Python files

- **April25-Clark-EvoIDS-v2.pdf**: A PDF version of my final presentation slides
- **CSE_914_FINAL_PAPER.pdf**: A PDF of my final paper.

## Python files

Now, for what you've all been waiting for...my source code!  I used Python 3.5 to develop this project, and I cannot guarantee that this code will work for different versions of Python.  However, I do not believe I used any packages that are not included in Python 3.5, so you should be able to run everything as long as you have Python 3.5.

- **batch_Fuzzy.py** and **batch_DoS_1.py**: These are the files to run and/or modify if you want to replicate my results.  These files essentially do a bunch of evolutionary runs, one right after the next, for fuzzy and denial of service attacks, respectively.  One thing to note is that at the time I am turning this in, everything is setup to use the integer-based genome that got better results for denial of service attacks.  Changing this back to the pure-binary genome is not difficult, but it requires a few modifications in EA.py.  However, before you decide to do a batch of runs, go to line 23 of EA.py (where CPUS is defined) and changed the number to however many cores your CPU has, or something smaller than that if you don't want your machine to get bogged down.  These batches take a long time to run, but the programs print an update for every generation, so you will know how fast it is progressing.

- **dataloader.py**: This is a script to process the raw CSV data that I got from [this source](http://ocslab.hksecurity.net/Datasets/CAN-intrusion-dataset).  The raw data is not included in the repository, as it was not needed after being processed and pickled.  

- **ea_individual.py** and **ea_individual_binary.py**: These files each define a class that represents an individual.  The first file defines the individual with the integer-based genome, and the second file defines the individual with the pure-binary genome.  The two classes all have the same functions, and can be swapped out in EA.py easily by simply changing which class is used to initialize a population and add more individuals (there are two instances where individuals are created in EA.py, so make sure to search for both of them).

- **EA.py**: This is where the magic happens.  EA.py defines a run function that runs a simulation when you give it all the parameters it needs (which are numerous), as well as functions to log data and other things needed for the evolutionary runs.  

- **graph_generator.py**: This script parses through all of the log files searching for runs that do not have fitness graphs generated.  When it finds a run without a graph, it automatically generates the graph.  Generating the graphs can take a second because it has to extract the compressed logs and then parse through all the generations to get the max and average fitness values.

- **genome_tester.py**: This is a script to generate training and testing accuracies.  When you run it, it prints all the logged runs that it has data for, and prompts the user to pick one to process.  It then displays a summary of the parameters used for then run, and prompts the user to pick a testing dataset.  It then displays the training and testing accuracies for the 10 individuals that had the highest fitness values in the last generation.  This can take a second to run because it tests the genomes against all of the training data, which is usually quite large.
