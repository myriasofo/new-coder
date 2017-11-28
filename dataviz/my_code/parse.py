
#import collections
import csv
#import matplotlib.pyplot as plt
#import numpy as np

MY_FILE = "data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    parsed_data = []
    with open(raw_file) as f:
        csv_data = csv.reader(f, delimiter=delimiter)
        column_names = next(csv_data)
        for row in csv_data:
            parsed_data.append(dict(zip(column_names, row)))
    return parsed_data

def main():
    parsed = parse(MY_FILE, ',')
    print(len(parsed))

if __name__ == '__main__':
    main()
