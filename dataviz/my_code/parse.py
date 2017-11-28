
import csv

CSV_FILE_PATH = "data/sample_sfpd_incident_all.csv"

def parseCsvAsJsonList(file_path):
    jsonList = []
    with open(file_path) as f:
        csv_file = csv.reader(f, delimiter=',')
        column_names = next(csv_file)
        for row in csv_file:
            column_row_tuples = zip(column_names, row)
            column_row_json = dict(column_row_tuples) 
            jsonList.append(column_row_json)
    return jsonList

def main():
    parsed = parseCsvAsJsonList(CSV_FILE_PATH)
    print('data type of output:', type(parsed))
    print("data type of output's elements:", type(parsed[0]))
    print(parsed[0])
    print(len(parsed))

if __name__ == '__main__':
    main()
