#!/usr/bin/python
import sys
import csv


# Function to get data from csv file
def open_csv(path):
    f = open(path, 'r')
    data = csv.DictReader(f)            # I use DictReader, because the data from csv is presented as list of dict:
    return data                         # key (name of column) and value


# Function to join files
# data_1 and data_2 are lists of dictionaries that contains rows of given csv files
# column is string name of column that is center of joining files
# diff list of strings- names of columns that are not in both csv
# mode - string name method of joining files
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
        if match == 1:
            print(row_1)
        elif mode == 'RIGHT' or mode == 'LEFT':
            print(row_1)


if __name__ == "__main__":
    arguments = sys.argv                    # Handling arguments from console
    try:
        data_1read = open_csv(arguments[1])     # Getting data from files
        data_2read = open_csv(arguments[2])
        data_1 = [row for row in data_1read]  # Rewriting data to list to get access multiple times to one row
        data_2 = [row for row in data_2read]
        column = arguments[3]                   # Getting name of column
        mode = arguments[4]                     # Getting mode
        if column not in data_1read.fieldnames:
            print('Provide right column name')
        else:
            # Handling method to join files with given args
            if mode == 'LEFT':
                diff = [name for name in data_2read.fieldnames if not (name in data_1read.fieldnames)]
                merge(data_1, data_2, column, diff, mode)
            elif mode == 'RIGHT':
                diff = [name for name in data_1read.fieldnames if not (name in data_2read.fieldnames)]
                merge(data_2, data_1, column, diff, mode)
            # I choose INNER join as default mode
            else:
                diff = []
                merge(data_1, data_2, column, diff, mode)
    except FileNotFoundError:
        print('Provide right arguments')
    except IndexError:
        print('Not all args was given')

    # I tested my solution on borrowed.csv and loan.csv

