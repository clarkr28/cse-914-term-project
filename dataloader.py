#!/usr/bin/python3.5

from os import listdir
import csv
import pickle

DATA_PATH = './data/'
PICKLE_EXTENSION = '.pkl'
CSV_DATA_SIZE_INDEX = 2
CAN_DATA_PADDER = '--'

if __name__ == '__main__':

    # get a filename to open
    filenames = listdir(DATA_PATH)
    for i, name in enumerate(filenames):
        print('{}: {}'.format(i, name))
    filenum = -1
    while filenum < 0 or filenum >= len(filenames):
        filenum = int(input('Choose file by number: '))
    filename = filenames[filenum]

    if '.txt' in filename:
        # process the file as a text file
        pass

    elif '.csv' in filename:
        # process the file as a csv file
        all_data = []
        with open(DATA_PATH + filename, newline='') as f:
            file_reader = csv.reader(f, delimiter=',')
            for i, row in enumerate(file_reader):
                # quit after a certain amount of time because the files are huge
                if i >= 350000:
                    break

                # special handling for can messages that are less than 8 bytes in length
                row[CSV_DATA_SIZE_INDEX] = int(row[CSV_DATA_SIZE_INDEX])
                while row[CSV_DATA_SIZE_INDEX] < 8:
                    row.insert(len(row) - 1, CAN_DATA_PADDER)
                    row[CSV_DATA_SIZE_INDEX] += 1
                all_data.append(row)

        # save the data to a pickle file with the same name but pickle extension
        output_filename = (DATA_PATH + filename).split('.csv')[0] + PICKLE_EXTENSION
        with open(output_filename, 'wb') as f:
            pickle.dump(all_data, f)
