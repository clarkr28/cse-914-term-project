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

    # process the file as a csv file
    unique_data = []
    with open(DATA_PATH + filename, newline='') as f:
        file_reader = csv.reader(f, delimiter=',')
        for i, row in enumerate(file_reader):
            # quit after a certain amount of time because the files are huge
            if i >= 350000:
                break

            """
            # special handling for can messages that are less than 8 bytes in length
            row[CSV_DATA_SIZE_INDEX] = int(row[CSV_DATA_SIZE_INDEX])
            while row[CSV_DATA_SIZE_INDEX] < 8:
                row.insert(len(row) - 1, CAN_DATA_PADDER)
                row[CSV_DATA_SIZE_INDEX] += 1
            unique_data.append(row)
            """
            processed_row = [(int(row[1], 16))] # CAN ID field
            processed_row.append(int(row[2]))  # number of data fields
            for j in range(processed_row[1]):
                processed_row.append(int(row[j+3], 16))

            processed_row.append(row[-1])  # save the label
            if processed_row not in unique_data:
                unique_data.append(processed_row)

    # save the data to a pickle file with the same name but pickle extension
    output_filename = (DATA_PATH + filename).split('.csv')[0] + PICKLE_EXTENSION
    with open(output_filename, 'wb') as f:
        pickle.dump(unique_data, f)

    injected = 0
    normal = 0
    for sample in unique_data:
        if sample[-1] == 'R':
            normal += 1
        elif sample[-1] == 'T':
            injected += 1

    print('total: {}\nInjected: {}\nnormal: {}\n'.format(len(unique_data), injected, normal))
