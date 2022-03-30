#!/usr/bin/python
import sys
import csv
from collections import defaultdict


def open_csv(path):
    f = open(path, 'r')
    data = csv.DictReader(f)
    return data


def merge(data_1, data_2, column, diff, mode):

    for row_1 in data_1:
        match = 0
        for row_2 in data_2:
            if row_1[column] == row_2[column]:
                row_1.update(row_2)
                match = 1
            if match == 0 and len(diff) > 0:
                for elem in diff:
                    row_1[elem] = 'NaN'
        print(row_1)
    return data_1


if __name__ == "__main__":
    arguments = sys.argv
    data_1read = open_csv(arguments[1])
    data_2read = open_csv(arguments[2])
    data_1 = [row for row in data_1read]
    data_2 = [row for row in data_2read]
    column = arguments[3]
    mode = arguments[4]
    if mode == 'LEFT':
        diff = [name for name in data_2read.fieldnames if not(name in data_1read.fieldnames)]
        merge(data_1, data_2, column, diff, mode)
    elif mode == 'RIGHT':
        diff = [name for name in data_1read.fieldnames if not (name in data_2read.fieldnames)]
        merge(data_2, data_1, column, diff, mode)
    else:
        diff = []
        merge(data_1, data_2, column, diff, mode)

