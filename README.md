# Evolutionary Intrusion Detection System for Controller Area Networks

by Jared Clark for CSE 914 (An Automotice Cyber-Security Course)

The following provides an overview of this repo's contents and how to run important programs.

## Folders

- **data**: This folder contains all of the data that was used in evolutionary runs.  As my program changed through the course of the project, the way I used the data also changed, which is why there are so many versions of the same data.  The final datasets that I ended up using for my main results were DoS_test.pkl, DoS_trail.pkl, Fuzzy_train.pkl, and Fuzzy_test.pkl.  

- **latex_source**: My Latex source used to generate the final report.

- **logs**: Every run logged a lot of data.  These logs quickly started taking up a lot of space, so I added a function at the end of the runs to compress all the data into a giant compressed pickle.  Every run has their own folder in the logs foler, where the folder name starts with the current date and time to prevent collisions and is followed by a custom message about the run.  Within every run folder there should also be a graph that plots the maximum and average fitness values for every generation of the run, which is a nice way to quickly visualize how the run performed.  Running graph_generator.py will iterate through all of the logged runs and generate any missing graphs.  

## Non-Python files

- **April25-Clark-EvoIDS-v2.pdf**: A PDF version of my final presentation slides
- **CSE_914_FINAL_PAPER.pdf**: A PDF of my final paper

## Python file

Now, for what you've all been waiting for...my source code!  I used Python 3.5 to develop this project, and I cannot guarantee that this code will work for different versions of Python.
