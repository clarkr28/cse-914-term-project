#!/usr/bin/python3.5

from os import listdir
import csv

DATAPATH = './data'

if __name__ == '__main__':
    filenames = listdir(DATAPATH)
    for i, name in enumerate(filenames):
        print('{}: {}'.format(i, name))
    filenum = -1
    while filenum < 0 or filenum >= len(filenames):
        filenum = int(input('Choose file by number: '))
    print(filenames[filenum])

